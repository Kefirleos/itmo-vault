@echo off
chcp 65001 > nul
echo ========================================================
echo 🔄 Синхронизация конспектов Obsidian (Git)
echo ========================================================
cd /d "%~dp0\.."

echo 📥 Получение обновлений (git pull)...
git pull origin main

echo 📝 Добавление изменений...
git add .

set /p msg="Введите описание коммита (или нажмите Enter для авто): "
if "%msg%"=="" set msg=Update notes and study materials: %date% %time%

git commit -m "%msg%"

echo 📤 Отправка в удаленный репозиторий (git push)...
git push origin main

echo ========================================================
echo ✅ Синхронизация завершена!
echo ========================================================
pause