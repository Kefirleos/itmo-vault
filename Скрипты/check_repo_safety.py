#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт многоступенчатой проверки безопасности и целостности репозитория перед отправкой на GitHub (Multi-Pass Pre-Push Protocol).
Проверяет:
  Pass 1: Отсутствие решений лабораторных работ, контестов и приватных папок (Anti-Plagiarism)
  Pass 2: Отсутствие секретов, токенов, API-ключей и персональных данных (Secrets & Privacy)
  Pass 3: Целостность перекрестных ссылок Obsidian [[...]] (Vault Integrity)
  Pass 4: Настройки Git (нейтральный автор коммитов, core.quotepath false)
"""

import os
import sys
import re
import subprocess

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

VAULT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

FORBIDDEN_PATH_PATTERNS = [
    re.compile(r'lab[s0-9]?', re.IGNORECASE),
    re.compile(r'лабораторн', re.IGNORECASE),
    re.compile(r'решени', re.IGNORECASE),
    re.compile(r'solutions?', re.IGNORECASE),
    re.compile(r'private', re.IGNORECASE),
    re.compile(r'личн', re.IGNORECASE),
    re.compile(r'secret', re.IGNORECASE),
    re.compile(r'\.env$', re.IGNORECASE),
    re.compile(r'\.key$', re.IGNORECASE),
    re.compile(r'\.token$', re.IGNORECASE),
    re.compile(r'credentials\.json$', re.IGNORECASE),
    re.compile(r'tasks?(\.html|\.md)?$', re.IGNORECASE),
    re.compile(r'TODO(\.md)?$', re.IGNORECASE),
    re.compile(r'личный\s*план', re.IGNORECASE),
]

FORBIDDEN_CONTENT_PATTERNS = [
    (re.compile(r'ghp_[a-zA-Z0-9]{36}'), "GitHub Personal Access Token"),
    (re.compile(r'BEGIN (RSA|OPENSSH|EC|DSA) PRIVATE KEY'), "SSH Private Key"),
    (re.compile(r'(?i)api[_-]?key\s*[:=]\s*[\'"][a-zA-Z0-9_\-]{16,}'), "API Key"),
    (re.compile(r'(?i)password\s*[:=]\s*[\'"][^\'"]{6,}'), "Hardcoded Password"),
    (re.compile(r'd:\\\\Личная', re.IGNORECASE), "Personal local path (d:\\Личная)"),
]

def check_pass_1_paths(tracked_files):
    print("\n🔍 [Pass 1/4] Проверка путей и структуры файлов на отсутствие лабораторных и решений...")
    issues = []
    for path in tracked_files:
        base = os.path.basename(path)
        for pat in FORBIDDEN_PATH_PATTERNS:
            if any(allowed in path for allowed in ['Полезные ресурсы', 'README', 'GEMINI.md', 'AGENTS.md', 'check_repo_safety.py']):
                continue
            if pat.search(base):
                if any(ok in path.lower() for ok in ["конспект", "лекция", "практика", "регламент"]):
                    continue
                issues.append(f"⚠️ Подозрительное имя файла или папки: {path}")
    if issues:
        for iss in issues:
            print("  " + iss)
        return False
    print("  ✅ Pass 1 пройден: готовых решений и закрытых папок не обнаружено.")
    return True

def check_pass_2_secrets(tracked_files):
    print("\n🔒 [Pass 2/4] Сканирование содержимого на наличие секретов, ключей и персональных данных...")
    issues = []
    for rel_path in tracked_files:
        full_path = os.path.join(VAULT_ROOT, rel_path)
        if not os.path.exists(full_path):
            continue
        if rel_path.endswith(('.pdf', '.png', '.jpg', '.jpeg', '.exe', '.dll', '.canvas', 'check_repo_safety.py')):
            continue
        try:
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                for pat, desc in FORBIDDEN_CONTENT_PATTERNS:
                    if pat.search(content):
                        issues.append(f"❌ Обнаружен потенциальный секрет ({desc}) в файле: {rel_path}")
        except Exception as e:
            pass
    if issues:
        for iss in issues:
            print("  " + iss)
        return False
    print("  ✅ Pass 2 пройден: секреты, токены и приватные ключи отсутствуют.")
    return True

def check_pass_3_links():
    print("\n🔗 [Pass 3/4] Проверка целостности перекрестных ссылок Obsidian [[...]]...")
    all_files = set()
    for root, dirs, files in os.walk(VAULT_ROOT):
        if '.git' in root or '.system_generated' in root or 'temp' in root:
            continue
        for f in files:
            base, _ = os.path.splitext(f)
            rel = os.path.relpath(os.path.join(root, f), VAULT_ROOT).replace('\\', '/')
            rel_no_ext = os.path.splitext(rel)[0]
            all_files.add(f)
            all_files.add(base)
            all_files.add(rel)
            all_files.add(rel_no_ext)

    link_pat = re.compile(r'\[\[([^\]|#\n]+)(?:#[^\]|\n]*)?(?:\|[^\]\n]*)?\]\]')
    code_block_pat = re.compile(r'```.*?```', re.DOTALL)
    inline_code_pat = re.compile(r'`[^`\n]+`')

    broken = []
    for root, dirs, files in os.walk(VAULT_ROOT):
        if '.git' in root or '.system_generated' in root or 'temp' in root:
            continue
        for f in files:
            if not f.endswith('.md'):
                continue
            # Пропускаем шаблоны заметок Obsidian
            if f.startswith('_') or 'шаблон' in f.lower():
                continue
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                    text = fp.read()
                text = code_block_pat.sub('', text)
                text = inline_code_pat.sub('', text)
                for t in link_pat.findall(text):
                    t = t.strip()
                    # Игнорируем плейсхолдеры шаблонизатора {{...}}
                    if t.startswith('{{') and t.endswith('}}'):
                        continue
                    # Нормализуем слеши
                    norm_t = t.replace('\\', '/')
                    if norm_t not in all_files and t not in all_files:
                        broken.append((os.path.relpath(path, VAULT_ROOT), t))
            except Exception:
                pass

    if broken:
        print(f"  ❌ Найдено битых ссылок: {len(broken)}")
        for src, tgt in broken[:10]:
            print(f"    {src} -> [[{tgt}]]")
        return False
    print("  ✅ Pass 3 пройден: все перекрестные ссылки [[...]] указывают на существующие заметки.")
    return True

def check_pass_4_git():
    print("\n⚙️  [Pass 4/4] Проверка конфигурации Git и автора коммитов...")
    ok = True
    try:
        email = subprocess.check_output(['git', 'config', 'user.email'], text=True, encoding='utf-8', cwd=VAULT_ROOT).strip()
        name = subprocess.check_output(['git', 'config', 'user.name'], text=True, encoding='utf-8', cwd=VAULT_ROOT).strip()
        quotepath = subprocess.check_output(['git', 'config', 'core.quotepath'], text=True, encoding='utf-8', cwd=VAULT_ROOT).strip()

        print(f"  👤 Git user.name: '{name}'")
        print(f"  📧 Git user.email: '{email}'")
        print(f"  🔤 Git core.quotepath: '{quotepath}'")

        if email != "student@itmo.ru":
            print("  ⚠️ Внимание: рекомендуется нейтральный email 'student@itmo.ru'")
        if quotepath.lower() != "false":
            print("  ❌ Ошибка: core.quotepath должен быть false для корректной поддержки кириллицы!")
            ok = False
    except Exception as e:
        print(f"  ⚠️ Не удалось прочитать git config: {e}")

    if ok:
        print("  ✅ Pass 4 пройден: параметры Git настроены согласно регламенту.")
    return ok

def main():
    print("=" * 70)
    print("🛡️  МНОГОСТУПЕНЧАТАЯ ПРОВЕРКА РЕПОЗИТОРИЯ ITMO-VAULT (PRE-PUSH PROTOCOL)")
    print("=" * 70)

    try:
        output = subprocess.check_output(['git', 'ls-files'], text=True, encoding='utf-8', cwd=VAULT_ROOT)
        tracked_files = [line.strip() for line in output.splitlines() if line.strip()]
    except Exception as e:
        print(f"❌ Ошибка вызова git ls-files: {e}")
        return False

    print(f"📦 Всего отслеживаемых файлов в репозитории: {len(tracked_files)}")

    p1 = check_pass_1_paths(tracked_files)
    p2 = check_pass_2_secrets(tracked_files)
    p3 = check_pass_3_links()
    p4 = check_pass_4_git()

    print("\n" + "=" * 70)
    if p1 and p2 and p3 and p4:
        print("🎉 ВСЕ 4 ЭТАПА ПРОВЕРКИ УСПЕШНО ПРОЙДЕНЫ!")
        print("🚀 Репозиторий полностью безопасен, целостен и готов к отправке (git push).")
        print("=" * 70)
        return True
    else:
        print("🚨 ОБНАРУЖЕНЫ ЗАМЕЧАНИЯ! ПУШ ЗАБЛОКИРОВАН ДО ИХ УСТРАНЕНИЯ.")
        print("=" * 70)
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
