@echo off
echo Activando entorno virtual...
call env\Scripts\activate.bat

echo Instalando dependencias...
pip install -r requirements.txt

echo Iniciando servidor Django...
python manage.py runserver

pause
