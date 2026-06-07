import random

def read_sensors():
    return {
        "gas": random.randint(350, 480),
        "sound": random.randint(20, 90),
        "vibration": random.choice([0, 1]),
        "lidar": round(random.uniform(0.5, 3.0), 2)
    }
