#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub Actions CI Safety & Integrity Validator for itmo-vault
Runs automatically on push and pull_request to guarantee repository safety.
"""

import os
import re
import sys
import urllib.parse

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

print("=" * 70)
print("🛡️  GITHUB ACTIONS: ITMO-VAULT REPOSITORY CI SAFETY AUDIT")
print("=" * 70)

errors = []
warnings = []

# ----------------------------------------------------------------------
# Pass 1: Blacklisted Paths & Files (Anti-Plagiarism & Privacy)
# ----------------------------------------------------------------------
print("\n🔍 [Pass 1/4] Checking repository file paths...")
FORBIDDEN_DIR_PATTERNS = [
    r'(?:^|[\\/])labs?(?:[\\/]|$)',
    r'(?:^|[\\/])лабораторные?(?:[\\/]|$)',
    r'(?:^|[\\/])solutions?(?:[\\/]|$)',
    r'(?:^|[\\/])my_solutions?(?:[\\/]|$)',
    r'(?:^|[\\/])temp(?:[\\/]|$)',
    r'(?:^|[\\/])personal(?:[\\/]|$)',
    r'(?:^|[\\/])секреты(?:[\\/]|$)',
]

FORBIDDEN_FILE_PATTERNS = [
    r'\.env(?:\..*)?$',
    r'.*\.key$',
    r'.*\.token$',
    r'.*\.pem$',
    r'id_rsa.*',
    r'id_ed25519.*',
    r'credentials\.json$',
    r'.*TODO.*\.md$',
    r'.*tasks.*\.html$',
    r'.*личный_?план.*\.md$',
    r'.*USER_PREFERENCES.*',
]

tracked_files = []
all_vault_files = set()
all_vault_basenames = set()

for root, dirs, files in os.walk('.'):
    if any(k in root for k in ['.git', 'temp', 'personal']):
        continue
    for f in files:
        rel_path = os.path.normpath(os.path.join(root, f)).replace('\\', '/')
        tracked_files.append(rel_path)
        all_vault_files.add(rel_path)
        all_vault_files.add(os.path.relpath(os.path.join(root, f), '.').replace('\\', '/'))
        all_vault_basenames.add(f)
        if f.endswith('.md'):
            all_vault_basenames.add(f[:-3])

for path in tracked_files:
    for pat in FORBIDDEN_DIR_PATTERNS:
        if re.search(pat, path, re.I):
            errors.append(f"[FORBIDDEN DIRECTORY] File '{path}' violates anti-plagiarism / privacy policy.")
    
    basename = os.path.basename(path)
    for pat in FORBIDDEN_FILE_PATTERNS:
        if re.search(pat, basename, re.I):
            errors.append(f"[FORBIDDEN FILE] File '{path}' violates repository policy.")

if not errors:
    print("  ✅ Pass 1 Passed: No forbidden directories or sensitive files found.")
else:
    print(f"  ❌ Pass 1 Failed: Found {len(errors)} forbidden file violations.")

# ----------------------------------------------------------------------
# Pass 2: Secret Scanning & Token Detection
# ----------------------------------------------------------------------
print("\n🔒 [Pass 2/4] Scanning file content for leaked secrets and private keys...")
SECRET_REGEXES = [
    (r'ghp_[A-Za-z0-9]{36}', "GitHub Personal Access Token (PAT)"),
    (r'github_pat_[A-Za-z0-9_]{82}', "GitHub Fine-Grained PAT"),
    (r'BEGIN (?:RSA |OPENSSH )?PRIVATE KEY', "SSH Private Key"),
    (r'sk-[a-zA-Z0-9]{32,}', "OpenAI / LLM API Key"),
    (r'(?:AIza[0-9A-Za-z-_]{35})', "Google Gemini API Key"),
]

for path in tracked_files:
    if path.endswith(('.png', '.jpg', '.jpeg', '.pdf', '.ico', '.svg')):
        continue
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
        for regex, desc in SECRET_REGEXES:
            if re.search(regex, content):
                errors.append(f"[SECRET LEAK] Possible {desc} detected in '{path}'.")
    except Exception as e:
        warnings.append(f"Could not read {path}: {e}")

if len(errors) == 0:
    print("  ✅ Pass 2 Passed: No leaked secrets, tokens, or private keys detected.")
else:
    print(f"  ❌ Pass 2 Failed: Secret leak detected!")

# ----------------------------------------------------------------------
# Pass 3: Markdown Links & Obsidian [[...]] Integrity
# ----------------------------------------------------------------------
print("\n🔗 [Pass 3/4] Validating internal links and cross-references...")
broken_links = 0
code_block_pat = re.compile(r'```[\s\S]*?```')
inline_code_pat = re.compile(r'`[^`\n]+`')
wiki_link_pat = re.compile(r'\[\[([^\]|#\\]+)(?:#[^\]|\\]+)?(?:\\?\|[^\]]+)?\]\]')
md_link_pat = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

for path in tracked_files:
    if not path.endswith('.md'):
        continue
    # Skip raw templates
    basename = os.path.basename(path)
    if basename.startswith('_') or 'шаблон' in basename.lower():
        continue

    dirpath = os.path.dirname(path)
    with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
        raw_content = fp.read()
    
    # Strip code blocks and inline code so examples are not treated as real links
    content = code_block_pat.sub('', raw_content)
    content = inline_code_pat.sub('', content)

    # Check [[WikiLink]]
    for target in wiki_link_pat.findall(content):
        t = target.strip().rstrip('\\').strip()
        if not t or (t.startswith('{{') and t.endswith('}}')):
            continue
        base = os.path.basename(t)
        base_no_ext = base[:-3] if base.endswith('.md') else base
        if base_no_ext not in all_vault_basenames and base not in all_vault_basenames:
            full_check = os.path.normpath(os.path.join(dirpath, t)).replace('\\', '/')
            if full_check not in all_vault_files and (full_check + '.md') not in all_vault_files:
                errors.append(f"[BROKEN WIKILINK] In '{path}': [[{target}]] does not exist.")
                broken_links += 1

    # Check [Text](Path)
    for text, target in md_link_pat.findall(content):
        if target.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        raw_path = target.split('#')[0]
        if not raw_path:
            continue
        decoded = urllib.parse.unquote(raw_path)
        resolved = os.path.normpath(os.path.join(dirpath, decoded))
        if not os.path.exists(resolved):
            errors.append(f"[BROKEN MD LINK] In '{path}': [{text}]({target}) -> '{resolved}' does not exist.")
            broken_links += 1

if broken_links == 0:
    print("  ✅ Pass 3 Passed: All Obsidian and Markdown links point to valid targets.")
else:
    print(f"  ❌ Pass 3 Failed: Found {broken_links} broken links.")

# ----------------------------------------------------------------------
# Pass 4: Math Delimiter Integrity
# ----------------------------------------------------------------------
print("\n📐 [Pass 4/4] Checking LaTeX display math syntax...")
unclosed_math = 0
for path in tracked_files:
    if not path.endswith('.md'):
        continue
    with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
        lines = fp.readlines()
    in_code_block = False
    in_math_block = False
    block_start = 0
    for i, line in enumerate(lines, 1):
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        
        # Check $$ block
        cnt = line.count('$$')
        if cnt % 2 != 0:
            in_math_block = not in_math_block
            if in_math_block:
                block_start = i
    if in_math_block:
        warnings.append(f"[UNCLOSED MATH] In '{path}': unclosed $$ block starting at line {block_start}.")
        unclosed_math += 1

if unclosed_math == 0:
    print("  ✅ Pass 4 Passed: Display LaTeX math blocks are balanced.")
else:
    print(f"  ⚠️ Pass 4 Warning: {unclosed_math} potentially unclosed math blocks.")

# ----------------------------------------------------------------------
# Summary & Exit
# ----------------------------------------------------------------------
print("\n" + "=" * 70)
if errors:
    print(f"❌ CI AUDIT FAILED with {len(errors)} error(s):")
    for e in errors[:20]:
        print(f"  - {e}")
    if len(errors) > 20:
        print(f"  ... and {len(errors) - 20} more errors.")
    sys.exit(1)
else:
    print("🎉 ALL CI AUDIT CHECKS PASSED SUCCESSFULLY!")
    if warnings:
        print(f"⚠️ {len(warnings)} warning(s) observed.")
    sys.exit(0)
