# Iris ML Model API

Este proyecto implementa un modelo de Machine Learning para la clasificación del dataset Iris usando Random Forest, con una API REST construida con Flask y configuración para despliegue en Kubernetes.

## 📋 Descripción

El proyecto incluye:
- **Modelo de ML**: Random Forest Classifier entrenado con el dataset Iris
- **API REST**: Endpoint Flask para realizar predicciones
- **Containerización**: Dockerfile para crear imagen Docker
- **Kubernetes**: Archivos YAML para despliegue en K8s

## 🚀 Estructura del Proyecto

```
├── modelo_iris.py      # Script para entrenar el modelo
├── modelo_iris.pkl     # Modelo entrenado serializado
├── api.py             # API Flask con endpoint /predict
├── test_api.py        # Script de pruebas para la API
├── requirements.txt   # Dependencias del proyecto
├── Dockerfile         # Imagen Docker
├── deployment.yaml    # Deployment de Kubernetes
├── service.yaml       # Servicio de Kubernetes
└── README.md          # Este archivo
```

## 🛠️ Instalación y Uso Local

### Prerrequisitos
- Python 3.7+
- pip

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd <nombre-del-repositorio>
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Entrenar el modelo (opcional)
El modelo ya está entrenado, pero puedes re-entrenarlo:
```bash
python modelo_iris.py
```

### 4. Ejecutar la API
```bash
python api.py
```

La API estará disponible en `http://localhost:5000`

### 5. Probar la API (opcional)
```bash
python test_api.py
```

## 📡 API Usage

### Endpoint: POST /predict

Realiza predicciones sobre nuevos datos de flores Iris.

**URL**: `http://localhost:5000/predict`

**Método**: `POST`

**Parámetros del cuerpo (JSON)**:
```json
{
    "features": [5.1, 3.5, 1.4, 0.2]
}
```

Los features corresponden a:
- `sepal_length` (cm)
- `sepal_width` (cm) 
- `petal_length` (cm)
- `petal_width` (cm)

**Respuesta exitosa**:
```json
{
    "prediction": 0
}
```

**Respuesta de error**:
```json
{
    "error": "Mensaje de error"
}
```

### Clases de predicción:
- `0`: Iris-setosa
- `1`: Iris-versicolor  
- `2`: Iris-virginica

### Ejemplo con curl:
```bash
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

## 🐳 Docker

### Construir imagen
```bash
docker build -t iris-ml-api .
```

### Ejecutar contenedor
```bash
docker run -p 5000:5000 iris-ml-api
```

## ☸️ Despliegue en Kubernetes

## 🔄 CI/CD: Flujo Simplificado de Deploy

Se ha configurado un pipeline de GitHub Actions en `.github/workflows/ci-cd.yml` que demuestra un flujo completo de CI/CD para modelos de ML:

### 🔄 Proceso automatizado

**En cada push a `main`:**

1. **Tests** 🧪
   - Instala dependencias Python
   - Lanza la API en background
   - Prueba endpoint `/health`
   - Prueba endpoint `/predict` con datos reales
   - Termina la API limpiamente

2. **Build & Deploy** 🚀 (solo si tests pasan)
   - Construye imagen Docker
   - Sube a Docker Hub con dos tags:
     - `latest`
     - `<commit-sha>` (trazabilidad)

### ⚙️ Configuración requerida

En tu repositorio de GitHub: **Settings > Secrets > Actions**

Crea estos secretos:
- `DOCKERHUB_USERNAME`: tu usuario de Docker Hub  
- `DOCKERHUB_TOKEN`: token de acceso (Docker Hub > Account Settings > Security)

### ▶️ Uso

```bash
# Ejecución manual desde GitHub Actions tab
# O simplemente: git push origin main

# Descargar imagen publicada
docker pull tu_usuario/iris-ml-api:latest
docker run -p 5000:5000 tu_usuario/iris-ml-api:latest
```

### 📚 Valor educativo

Este pipeline enseña:
- Tests de integración básicos con curl
- Manejo de procesos en background en CI
- Docker build y publish automático  
- Dependencias entre jobs (`needs: tests`)
- Gestión de secretos en GitHub Actions


### 1. Aplicar deployment
```bash
kubectl apply -f deployment.yaml
```

### 2. Aplicar servicio
```bash
kubectl apply -f service.yaml
```

### 3. Verificar despliegue
```bash
kubectl get pods
kubectl get services
```

## 🧪 Pruebas de Ejemplo

Puedes probar diferentes tipos de flores Iris:

```bash
# Iris-setosa (esperado: 0)
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'

# Iris-versicolor (esperado: 1) 
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [6.4, 3.2, 4.5, 1.5]}'

# Iris-virginica (esperado: 2)
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [6.3, 3.3, 6.0, 2.5]}'
```

## 📚 Tecnologías Utilizadas

- **Python 3.x**
- **scikit-learn**: Machine Learning
- **Flask**: API REST
- **joblib**: Serialización del modelo
- **numpy**: Computación numérica
- **Docker**: Containerización
- **Kubernetes**: Orquestación de contenedores

## 📝 Notas

- El modelo Random Forest fue entrenado con el dataset completo de Iris (150 muestras)
- La precisión del modelo es cercana al 100% debido a la naturaleza simple del dataset Iris
- Este proyecto es con fines educativos y demostrativos

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea tu feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la branch (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.