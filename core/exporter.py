import json
import csv
import os
from datetime import datetime


REPORT_DIR = "reports"


def create_report_directory():
    """
    Create reports directory if it does not exist.
    """
    os.makedirs(REPORT_DIR, exist_ok=True)


def generate_filename(extension):
    """
    Generate timestamped filename.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(
        REPORT_DIR,
        f"scan_{timestamp}.{extension}"
    )


def export_json(results):
    """
    Export scan results to JSON.
    """

    create_report_directory()

    filename = generate_filename("json")

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    return filename


def export_csv(results):
    """
    Export scan results to CSV.
    """

    create_report_directory()

    filename = generate_filename("csv")

    if not results:
        return filename


    csv_results = []

    for item in results:

        risk = item.get("risk", {})

        csv_results.append({

            "port": item.get("port"),
            "service": item.get("service"),
            "software": item.get("software"),
            "version": item.get("version"),
            "vendor": item.get("vendor"),
            "os_hint": item.get("os_hint"),

            "risk_level": risk.get(
                "level",
                "LOW"
            ),

            "risk_score": risk.get(
                "score",
                0
            ),

            "severity": risk.get(
                "severity",
                "LOW"
            ),

            "cves": ", ".join(
                risk.get("cves", [])
            ),

            "recommendations": ", ".join(
                [
                    detail.get("recommendation")
                    for detail in risk.get("details", [])
                    if detail.get("recommendation")
                ]
            )
        })


    headers = csv_results[0].keys()


    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=headers
        )

        writer.writeheader()

        writer.writerows(csv_results)


    return filename