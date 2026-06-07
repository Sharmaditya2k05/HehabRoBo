from config import SENSOR_WEIGHTS

def normalize(sensor):
    gas_n = sensor["gas"] / 1000
    sound_n = sensor["sound"] / 100
    vibration = sensor["vibration"]
    lidar_n = sensor["lidar"] / 5

    return {
        "gas": gas_n,
        "sound": sound_n,
        "vibration": vibration,
        "lidar": lidar_n
    }

def weighted_fusion(norm):
    score = 0.0
    for key in SENSOR_WEIGHTS:
        score += norm[key] * SENSOR_WEIGHTS[key]
    return score
