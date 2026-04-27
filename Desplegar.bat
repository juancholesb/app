@echo off
title StockMaster - Despliegue en Internet
color 0A

echo ========================================
echo    STOCKMASTER - DESPLIEGUE EN INTERNET
echo ========================================
echo.
echo Este script te llevara a desplegar tu
echo aplicacion en Render (GRATIS).
echo.
echo IMPORTANTE: Necesitas una cuenta de 
echo Google para continuar.
echo.
echo.
pause

echo.
echo 1. Abriendo Render...
start https://dashboard.render.com/new/select?type=web

echo.
echo 2. En la pagina de Render:
echo    - Selecciona "Upload a ZIP file"
echo    - Sube: StockMaster-Web.zip
echo.
echo 3. Configura asi:
echo    - Name: stockmaster
echo    - Build: pip install -r server/requirements.txt
echo    - Start: python server/server.py
echo.
echo 4. Click en "Create Web Service"
echo    - Espera ~3 minutos
echo.
echo 5. Cuando diga "Live", copia la URL
echo.
echo ========================================
echo.
echo Tu aplicacion estara en:
echo https://stockmaster-XXXX.onrender.com
echo.
echo Credenciales:
echo   Admin: admin / admin123
echo   Empleado: empleado / emp123
echo.
pause