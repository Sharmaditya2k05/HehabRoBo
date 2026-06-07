import random
import time

def read_sensors():
    return {
        "gas": random.randint(380, 460),
        "sound": random.randint(20, 90),
        "vibration": random.choice([0, 1]),
        "lidar": round(random.uniform(0.5, 3.0), 2),
        "ultrasonic": random.randint(50, 200),
        "imu": [0.1, 0.2, 9.8],
        "timestamp": time.time()
    }
