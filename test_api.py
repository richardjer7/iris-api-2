#!/usr/bin/env python3
"""Script de prueba para verificar la API de Iris ML."""
import requests

# Configuración
BASE_URL = "http://localhost:5000"


def test_health_check():
    """Probar el endpoint de health check"""
    print("🔍 Probando health check...")
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se puede conectar a la API. ¿Está ejecutándose?")
        return False


def test_predict():
    """Probar el endpoint de predicción"""
    print("\n🔍 Probando predicción...")
    
    # Datos de prueba (Iris-setosa)
    test_data = {
        "features": [5.1, 3.5, 1.4, 0.2]
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/predict",
            json=test_data,
            headers={'Content-Type': 'application/json'},
            timeout=5
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se puede conectar a la API.")
        return False


def test_invalid_data():
    """Probar con datos inválidos"""
    print("\n🔍 Probando validación de datos...")
    
    # Datos inválidos (solo 3 features)
    invalid_data = {
        "features": [5.1, 3.5, 1.4]
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/predict",
            json=invalid_data,
            headers={'Content-Type': 'application/json'},
            timeout=5
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 400
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se puede conectar a la API.")
        return False


if __name__ == "__main__":
    print("🚀 Iniciando pruebas de la API...")
    print("=" * 50)
    
    # Ejecutar pruebas
    health_ok = test_health_check()
    predict_ok = test_predict()
    validation_ok = test_invalid_data()
    
    # Resumen
    print("\n" + "=" * 50)
    print("📊 RESUMEN DE PRUEBAS:")
    print(f"✅ Health Check: {'PASS' if health_ok else 'FAIL'}")
    print(f"✅ Predicción: {'PASS' if predict_ok else 'FAIL'}")
    print(f"✅ Validación: {'PASS' if validation_ok else 'FAIL'}")
    
    if all([health_ok, predict_ok, validation_ok]):
        print("\n🎉 ¡Todas las pruebas pasaron!")
    else:
        print("\n⚠️  Algunas pruebas fallaron.")

