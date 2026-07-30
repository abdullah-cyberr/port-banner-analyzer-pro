def calculate_risk_score(risk_data):
    """
    Calculate numeric risk score based on detected issues
    """

    score = 0

    reasons = risk_data.get("reasons", [])
    cves = risk_data.get("cves", [])
    level = risk_data.get("level", "LOW")


    # CVE based scoring
    if cves:
        score += len(cves) * 20


    # Reason based scoring
    score += len(reasons) * 10


    # Existing risk level influence
    level_score = {
        "LOW": 10,
        "MEDIUM": 30,
        "HIGH": 60,
        "CRITICAL": 90
    }


    score = max(score, level_score.get(level, 0))


    # Maximum limit
    if score > 100:
        score = 100


    # Severity mapping

    if score <= 20:
        severity = "LOW"

    elif score <= 50:
        severity = "MEDIUM"

    elif score <= 80:
        severity = "HIGH"

    else:
        severity = "CRITICAL"


    return {
        "score": score,
        "severity": severity
    }