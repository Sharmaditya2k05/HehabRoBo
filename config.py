# ================= CONFIGURATION =================

# Main loop delay (seconds)
LOOP_DELAY = 2

# Sensor fusion weights
SENSOR_WEIGHTS = {
    "gas": 0.25,
    "sound": 0.25,
    "vibration": 0.20,
    "lidar": 0.30
}

# Decision threshold
HUMAN_CONFIDENCE_THRESHOLD = 0.65

# Default GPS (simulation)
DEFAULT_GPS = (28.6139, 77.2090)
