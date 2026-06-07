import joblib
import os
from model import create_model

X = [
    [0.42, 0.75, 1, 0.3],
    [0.38, 0.20, 0, 1.1],
    [0.46, 0.85, 1, 0.4],
    [0.37, 0.25, 0, 1.3],
    [0.44, 0.80, 1, 0.5],
    [0.39, 0.30, 0, 1.0]
]

y = [1, 0, 1, 0, 1, 0]

model = create_model()
model.fit(X, y)


joblib.dump(model, os.path.join("ml", "human_detector.pkl"))
print(" ML model trained")
