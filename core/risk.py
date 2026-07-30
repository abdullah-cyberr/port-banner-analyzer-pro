from core.cve_db import VULNERABILITY_DB



def detect_risk(service, software, version):

    risk_data = {

        "level": "LOW",

        "reasons": [],

        "cves": [],

        "details": []

    }


    # -----------------------------
    # CVE Database Detection
    # -----------------------------

    if software in VULNERABILITY_DB:

        software_db = VULNERABILITY_DB[software]


        if version in software_db:

            vuln = software_db[version]


            risk_data["level"] = vuln["severity"]


            risk_data["reasons"].append(
                vuln["description"]
            )


            risk_data["cves"].append(
                vuln["cve"]
            )


            risk_data["details"].append(
                {
                    "cve": vuln["cve"],

                    "issue": vuln["description"],

                    "recommendation": vuln["recommendation"]
                }
            )



    # -----------------------------
    # Manual Security Rules
    # -----------------------------

    if service == "SSH":

        if version.startswith("6."):

            risk_data["level"] = "MEDIUM"


            reason = (
                "Old OpenSSH version detected"
            )


            recommendation = (
                "Upgrade OpenSSH to latest version"
            )


            if reason not in risk_data["reasons"]:

                risk_data["reasons"].append(
                    reason
                )


            existing_recommendations = [

                item.get("recommendation")

                for item in risk_data["details"]

            ]


            if recommendation not in existing_recommendations:

                risk_data["details"].append(
                    {
                        "issue": reason,

                        "recommendation": recommendation
                    }
                )



    # -----------------------------
    # Remove Duplicate CVEs
    # -----------------------------

    risk_data["cves"] = list(
        set(risk_data["cves"])
    )


    # -----------------------------
    # Remove Duplicate Reasons
    # -----------------------------

    risk_data["reasons"] = list(
        set(risk_data["reasons"])
    )


    return risk_data