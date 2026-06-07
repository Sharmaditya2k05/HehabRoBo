import time
from simulation.mock_sensors import read_sensors
from fusion.fusion_engine import normalize, weighted_fusion
from ml.inference import predict
from decision.decision_engine import decide
from communication.alert_manager import send_alert
from logger import log
from config import LOOP_DELAY, DEFAULT_GPS

log("Disaster Management Robot Software Started")

while True:
    sensor = read_sensors()
    log(f"Sensor data: {sensor}")

    norm = normalize(sensor)
    fusion_score = weighted_fusion(norm)

    features = list(norm.values())
    ml_confidence = predict(features)

    status, confidence = decide(
        ml_confidence,
        fusion_score,
        thermal_presence=1  # simulated
    )

    log(f"Status={status} | Confidence={confidence}")

    if status == "HUMAN_CONFIRMED":
        send_alert(DEFAULT_GPS, confidence)

    time.sleep(LOOP_DELAY)


'''
python ml/train.py
python -m runner.main_runner
'''