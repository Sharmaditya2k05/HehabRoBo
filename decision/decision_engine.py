HUMAN_CONFIDENCE_THRESHOLD = 0.65

def decide(ml_confidence, fusion_score, thermal_presence=1):
    final_conf = (ml_confidence * 0.7) + (fusion_score * 0.3)

    if final_conf >= HUMAN_CONFIDENCE_THRESHOLD:
        return "HUMAN_CONFIRMED", round(final_conf, 2)

    return "NO_HUMAN", round(final_conf, 2)
