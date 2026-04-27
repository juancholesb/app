#!/usr/bin/env python3
"""
Script automático para desplegar StockMaster en Render
"""

import os
import sys
import subprocess
import time

def print_step(msg):
    print(f"\n{'='*50}")
    print(f"  {msg}")
    print(f"{'='*50}\n")

def main():
    print_step("🚀 DESPLIEGUE AUTOMÁTICO DE STOCKMASTER")
    
    print("Este script te ayudará a desplegar la app en Render (GRATIS)")
    print("\nPasos:")
    print("1. Ve a https://render.com y crea una cuenta (Google)")
    print("2. Ve a Dashboard > New > Web Service")
    print("3. Selecciona 'Upload a ZIP file'")
    print("4. Sube el archivo: StockMaster-Web.zip")
    print("5. Configura:")
    print("   - Name: stockmaster-tuNombre")
    print("   - Build Command: pip install -r server/requirements.txt")
    print("   - Start Command: python server/server.py")
    print("6. Click en 'Create Web Service'")
    print("7. Espera ~3 minutos")
    print("8. ¡Listo! Tu link será como:")
    print("   https://stockmaster-tuNombre.onrender.com")
    
    print("\n" + "="*50)
    print("  Archivos preparados:")
    print("="*50)
    
    files = [
        "index.html",
        "app.js", 
        "styles.css",
        "server/server.py",
        "server/requirements.txt",
        "Procfile",
        "runtime.txt",
        "StockMaster-Web.zip"
    ]
    
    for f in files:
        path = f"c:\\Users\\JUAN PC\\Downloads\\Empresa\\{f}"
        if os.path.exists(path):
            size = os.path.getsize(path)
            print(f"  ✅ {f} ({size:,} bytes)")
        else:
            print(f"  ❌ {f} - NO ENCONTRADO")
    
    print("\n" + "="*50)
    print("  URL de la app (cuando desplegues):")
    print("="*50)
    print("  https://stockmaster-TUNOMBRE.onrender.com")
    
    print("\n" + "="*50)
    print("  Credenciales de acceso:")
    print("="*50)
    print("  Admin: admin / admin123")
    print("  Empleado: empleado / emp123")

if __name__ == "__main__":
    main()