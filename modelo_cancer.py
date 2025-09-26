from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import joblib

X, y = load_breast_cancer(return_X_y=True)
model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, 'modelo_breast_cancer.pkl')