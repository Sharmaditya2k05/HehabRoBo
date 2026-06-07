

import time

from simulation.sensors import read_sensors
from fusion.fusion_engine import normalize, weighted_fusion
from ml.inference import predict
from decision.decision_engine import decide
from config import LOOP_DELAY, DEFAULT_GPS
from logger import log


def main():
    log("Disaster Management Robot Software Started")

    while True:
        # 1. Read sensor data (ESP32 or simulation)
        sensor_data = read_sensors()
        log(f"Sensor Data: {sensor_data}")

        # 2. Normalize + fuse sensor data
        normalized = normalize(sensor_data)
        fusion_score = weighted_fusion(normalized)

        # 3. ML inference
        features = list(normalized.values())
        ml_confidence = predict(features)

        # 4. Decision engine
        status, confidence = decide(
            ml_confidence,
            fusion_score,
            thermal_presence=1  # thermal flag can come from camera later
        )

        log(f"Decision: {status} | Confidence: {confidence}")

        # 5. Alert
        if status == "HUMAN_CONFIRMED":
            log(f"🚨 ALERT SENT | Location: {DEFAULT_GPS}", level="ALERT")

        time.sleep(LOOP_DELAY)


if __name__ == "__main__":
    main()
