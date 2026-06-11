"""Esqueleto de modelado para el repo principal.

Funciones mínimas:
- build_pipeline()
- train_and_evaluate(pipeline, X_train, y_train, X_test, y_test)
- save_model(model, path)
"""
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib


def build_pipeline() -> Pipeline:
    pipe = Pipeline([
        ('imputer', SimpleImputer()),
        ('scaler', StandardScaler()),
        ('clf', LogisticRegression(max_iter=1000))
    ])
    return pipe


def train_and_evaluate(pipeline, X_train, y_train, X_test, y_test):
    pipeline.fit(X_train, y_train)
    score = pipeline.score(X_test, y_test)
    return {'accuracy': score}


def save_model(model, path: str):
    joblib.dump(model, path)
