#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт проверки безопасности репозитория перед отправкой на GitHub (Pre-Push Security Check).
Проверяет отсутствие решений лабораторных, секретов, токенов и личных данных.
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

FORBIDDEN_PATH_PATTERNS = [
    re.compile(r'lab[s0-9]?', re.IGNORECASE),
    re.compile(r'лабораторн', re.IGNORECASE),
    re.compile(r'решени', re.IGNORECASE),
    re.compile(r'solutions?', re.IGNORECASE),
    re.compile(r'private', re.IGNORECASE),
    re.compile(r'личн', re.IGNORECASE),
    re.compile(r'secret', re.IGNORECASE),
    re.compile(r'\.env', re.IGNORECASE),
    re.compile(r'\.key$', re.IGNORECASE),
    re.compile(r'\.token$', re.IGNORECASE),
    re.compile(r'credentials\.json$', re.IGNORECASE),
]

FORBIDDEN_CONTENT_PATTERNS = [
    (re.compile(r'ghp_[a-zA-Z0-9]{36}'), "GitHub Personal Access Token"),
    (re.compile(r'BEGIN (RSA|OPENSSH|EC|DSA) PRIVATE KEY'), "SSH Private Key"),
    (re.compile(r'(?i)api[_-]?key\s*[:=]\s*[\'"][a-zA-Z0-9_\-]{16,}'), "API Key"),
    (re.compile(r'(?i)password\s*[:=]\s*[\'"][^\'"]{6,}'), "Hardcoded Password"),
]

def check_security():
    print("=" * 60)
    print("🛡️  Запуск проверки безопасности репозитория itmo-vault")
    print("=" * 60)
    
    # 1. Проверяем отслеживаемые Git файлы
    try:
        output = subprocess.check_output(['git', 'ls-files'], text=True, encoding='utf-8')
        tracked_files = [line.strip() for line in output.splitlines() if line.strip()]
    except Exception as e:
        print(f"❌ Ошибка вызова git ls-files: {e}")
        return False

    issues = []

    # 2. Проверка имен файлов
    for path in tracked_files:
        # Проверяем, не попали ли папки/файлы лабораторных или секретов
        for pat in FORBIDDEN_PATH_PATTERNS:
            # Исключаем учебные материалы, где просто упоминаются регламенты лаб
            if any(allowed in path for allowed in ['Полезные ресурсы', 'README', 'tasks.html', 'TODO', 'GEMINI.md', 'AGENTS.md']):
                continue
            if pat.search(os.path.basename(path)):
                # Если файл содержит слово лаб в названии конспекта - это конспект, а не решение
                if "конспект" in path.lower() or "лекция" in path.lower() or "практика" in path.lower():
                    continue
                issues.append(f"⚠️ Подозрительное имя отслеживаемого файла: {path}")

    # 3. Проверка содержимого файлов на ключи и секреты
    for path in tracked_files:
        if not os.path.exists(path):
            continue
        if path.endswith(('.pdf', '.png', '.jpg', '.jpeg', '.exe', '.dll', '.canvas')):
            continue
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                for pat, desc in FORBIDDEN_CONTENT_PATTERNS:
                    if pat.search(content):
                        issues.append(f"❌ Обнаружен потенциальный секрет ({desc}) в файле: {path}")
        except Exception as e:
            pass

    # 4. Проверка автора коммитов
    try:
        author_info = subprocess.check_output(['git', 'config', 'user.email'], text=True, encoding='utf-8').strip()
        print(f"👤 Текущий git user.email: {author_info or 'не задан локально'}")
    except Exception:
        pass

    print(f"\n📊 Проверено файлов: {len(tracked_files)}")
    if issues:
        print("🚨 ОБНАРУЖЕНЫ ПРОБЛЕМЫ:")
        for iss in issues:
            print("  " + iss)
        print("\n❌ Пуш НЕ рекомендуется до устранения замечаний.")
        return False
    else:
        print("✅ Проверка пройдена! Репозиторий содержит исключительно открытые учебные материалы.")
        print("🔒 Никаких секретов, паролей или запрещенных решений не обнаружено.")
        return True

if __name__ == "__main__":
    success = check_security()
    sys.exit(0 if success else 1)
