# Disaster Management Robot 🤖

An autonomous disaster-response robot software system that detects human presence in hazardous or post-disaster environments through multi-sensor fusion and a machine learning inference engine. When a human is confirmed, it triggers a real-time GPS-tagged alert.

---

## Overview

The system runs a continuous sensing loop that:
1. Reads data from four simulated sensors (gas, sound, vibration, LiDAR).
2. Normalizes and fuses sensor readings into a single confidence score.
3. Passes normalized features through a pre-trained ML classifier (`human_detector.pkl`).
4. Combines ML confidence and fusion score in a decision engine.
5. Fires a GPS-tagged alert if a human is confirmed above the set threshold.

---

## Features

- **Multi-sensor fusion** — Weighted combination of gas, sound, vibration, and LiDAR readings.
- **ML inference** — A pre-trained `RandomForestClassifier` (scikit-learn) that classifies whether human presence is detected from the fused sensor features.
- **Configurable decision threshold** — Confidence threshold and sensor weights are tunable via `config.py`.
- **Thermal presence integration** — Decision engine accepts a thermal flag as an additional input alongside ML and fusion scores.
- **Alert dispatch** — On human confirmation, an alert is sent with GPS coordinates and confidence level.
- **Timestamped logging** — All events are logged with ISO-format timestamps at INFO/WARNING levels.

---

## Project Structure

```
├── main.py                        # Main sensing loop entry point
├── config.py                      # Sensor weights, threshold, GPS default, loop delay
├── logger.py                      # Timestamped logging utility
├── ml/
│   ├── train.py                   # Model training script
│   └── inference.py               # predict() — loads human_detector.pkl and runs inference
├── simulation/
│   └── mock_sensors.py            # read_sensors() — simulates sensor hardware
├── fusion/
│   └── fusion_engine.py           # normalize(), weighted_fusion()
├── decision/
│   └── decision_engine.py         # decide() — combines ML + fusion + thermal
├── communication/
│   └── alert_manager.py           # send_alert() — dispatches GPS-tagged alerts
├── runner/
│   └── main_runner.py             # Alternative module-based entry point
└── human_detector.pkl             # Pre-trained RandomForestClassifier model
```

---

## Configuration

All tunable parameters live in `config.py`:

```python
LOOP_DELAY = 2                      # Seconds between sensing cycles

SENSOR_WEIGHTS = {
    "gas":       0.25,
    "sound":     0.25,
    "vibration": 0.20,
    "lidar":     0.30               # LiDAR weighted highest
}

HUMAN_CONFIDENCE_THRESHOLD = 0.65   # Minimum confidence to trigger alert

DEFAULT_GPS = (28.6139, 77.2090)    # Default coordinates (New Delhi) for simulation
```

---

## ML Model

The model file `human_detector.pkl` is a scikit-learn `RandomForestClassifier`. It takes 4 normalized sensor values (gas, sound, vibration, LiDAR) as input features and outputs a binary classification confidence for human presence.

To retrain the model:

```bash
python ml/train.py
```

---

## Running

### Prerequisites

```bash
pip install scikit-learn
```

(Add any other dependencies your sensor simulation and alert modules require.)

### Run the main loop

```bash
python main.py
```

### Run via the module runner

```bash
python -m runner.main_runner
```

### Example log output

```
[INFO] 2025-04-19 08:03:12 : Disaster Management Robot Software Started
[INFO] 2025-04-19 08:03:12 : Sensor data: {'gas': 0.72, 'sound': 0.41, 'vibration': 0.55, 'lidar': 0.88}
[INFO] 2025-04-19 08:03:12 : Status=HUMAN_CONFIRMED | Confidence=0.81
```

---

## Decision Logic

The `decide()` function in `decision/decision_engine.py` combines three signals:

| Input | Source |
|---|---|
| `ml_confidence` | RandomForest prediction probability |
| `fusion_score` | Weighted sum of normalized sensor readings |
| `thermal_presence` | Simulated thermal camera flag (0 or 1) |

If the combined confidence exceeds `HUMAN_CONFIDENCE_THRESHOLD` (default `0.65`), the status is set to `HUMAN_CONFIRMED` and an alert is dispatched via `send_alert()`.

---

## Sensor Weights

LiDAR is given the highest weight (0.30) as it provides the most reliable spatial data for detecting human-sized objects. Gas and sound sensors are weighted equally (0.25 each) and vibration slightly lower (0.20), reflecting their higher susceptibility to environmental noise.

---

## Use Case

Designed for post-disaster search-and-rescue scenarios (collapsed buildings, flood zones, etc.) where direct human entry is unsafe. The robot patrols an area, continuously evaluates sensor readings, and alerts rescue teams to any confirmed human presence with GPS coordinates.

---

## License

No license is explicitly specified in this repository.
