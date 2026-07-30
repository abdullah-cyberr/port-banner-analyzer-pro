import re

from core.risk import detect_risk
from core.risk_score import calculate_risk_score


SERVICE_PATTERNS = {

    "SSH": {
        "pattern": r"SSH-\d\.\d-OpenSSH[_\-](\S+)",
        "software": "OpenSSH",
        "vendor": "OpenSSH Project"
    },

    "HTTP": {
        "pattern": r"(Apache|nginx)/([\d\.]+)",
        "software": None,
        "vendor_map": {
            "Apache": "Apache Software Foundation",
            "nginx": "NGINX Inc."
        }
    },

    "FTP": {
        "pattern": r"(FileZilla|vsftpd|ProFTPD)",
        "software": None,
        "vendor": None
    }

}


def analyze_banner(banner):

    result = {
        "service": "Unknown",
        "software": "Unknown",
        "version": "Unknown",
        "vendor": "Unknown",
        "os_hint": "Unknown",
        "risk": {
            "level": "LOW",
            "reasons": [],
            "cves": [],
            "details": []
        },
        "risk_score": 0,
        "severity": "LOW"
    }

    if not banner:
        return result

    for service, data in SERVICE_PATTERNS.items():

        match = re.search(
            data["pattern"],
            banner,
            re.IGNORECASE
        )

        if match:

            result["service"] = service

            if data["software"]:
                result["software"] = data["software"]
            else:
                result["software"] = match.group(1)

            if "vendor_map" in data:

                result["vendor"] = data["vendor_map"].get(
                    result["software"],
                    "Unknown"
                )

            elif data.get("vendor"):

                result["vendor"] = data["vendor"]

            if match.lastindex:
                result["version"] = match.group(match.lastindex)

            break

    os_patterns = [
        "Ubuntu",
        "Debian",
        "CentOS",
        "Red Hat",
        "Windows",
        "FreeBSD",
        "OpenBSD"
    ]

    for os_name in os_patterns:

        if os_name.lower() in banner.lower():
            result["os_hint"] = os_name
            break

    # -----------------------------
    # Step 14.1 - Risk Detection
    # -----------------------------

    risk = detect_risk(
        result["service"],
        result["software"],
        result["version"]
    )

    result["risk"] = risk

    # -----------------------------
    # Step 14.3 - Risk Score Engine
    # -----------------------------

    # -----------------------------
    # Step 14.3 - Risk Score Engine
    # -----------------------------

    risk_score = calculate_risk_score(
         risk
    )

    result["risk"]["score"] = risk_score["score"]
    result["risk"]["severity"] = risk_score["severity"]

    result["risk_score"] = risk_score["score"]
    result["severity"] = risk_score["severity"]

    return result