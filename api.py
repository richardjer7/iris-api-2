"""API Flask para servir un modelo de clasificación Iris."""

from flask import Flask, request, jsonify
import joblib
import numpy as np
import logging
import os

# --------------------------------------------------
# Configuración de logging
# --------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --------------------------------------------------
# Inicializar la aplicación
# --------------------------------------------------
app = Flask(__name__)

# --------------------------------------------------
# Carga del modelo al iniciar la app
# --------------------------------------------------
MODEL_FILENAME = 'modelo_iris.pkl'
model = None
if os.path.exists(MODEL_FILENAME):
    try:
        model = joblib.load(MODEL_FILENAME)
        logger.info("Modelo cargado: %s", MODEL_FILENAME)
    except Exception as exc:  # pylint: disable=broad-except
        logger.error("No se pudo cargar el modelo: %s", exc)
else:
    logger.warning("Archivo de modelo no encontrado: %s", MODEL_FILENAME)


# --------------------------------------------------
# Endpoint de salud
# --------------------------------------------------
@app.route('/', methods=['GET'])
@app.route('/health', methods=['GET'])
def health_check():
    """Devuelve el estado de la API y del modelo."""
    status = 'ok' if model is not None else 'model-missing'
    code = 200 if model is not None else 500
    return jsonify({'status': status}), code


# --------------------------------------------------
# Endpoint de predicción
# --------------------------------------------------
@app.route('/predict', methods=['POST'])
def predict():
    """Realiza una predicción a partir de un JSON con 'features'."""
    if model is None:
        return jsonify({'error': 'Modelo no disponible'}), 500

    # Verificar tipo de contenido
    if not request.is_json:
        return jsonify({
            'error': 'Content-Type debe ser application/json'
        }), 400

    data = request.get_json(silent=True)
    if not data:
        return jsonify({'error': 'Body vacío'}), 400

    # Validar existencia de features
    if 'features' not in data:
        return jsonify({'error': 'Campo "features" requerido'}), 400

    features = data['features']
    if not isinstance(features, list):
        return jsonify({'error': 'Features debe ser lista'}), 400
    if len(features) != 4:
        return jsonify({'error': 'Se requieren 4 features'}), 400

    # Convertir a floats
    try:
        features = [float(x) for x in features]
    except (ValueError, TypeError):  # Datos no numéricos
        return jsonify({
            'error': 'Todas las features deben ser numéricas'
        }), 400

    # Predicción
    arr = np.array(features).reshape(1, -1)
    try:
        pred = model.predict(arr)[0]
    except Exception as exc:  # pylint: disable=broad-except
        logger.error('Error durante la predicción: %s', exc)
        return jsonify({'error': 'Error interno en predicción'}), 500

    class_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    result = int(pred)
    logger.info('Predicción realizada: %d', result)
    return jsonify({'prediction': result, 'class_name': class_names[result]})


# --------------------------------------------------
# Punto de entrada
# --------------------------------------------------
if __name__ == '__main__':  # pragma: no cover
    app.run(host='0.0.0.0', port=5000)
