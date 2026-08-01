# 🔍 Port Banner Analyzer Pro

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Security](https://img.shields.io/badge/Focus-Cyber%20Security-red)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-Educational-green)
![Status](https://img.shields.io/badge/Project-Active-success)

..

A professional Python-based cybersecurity reconnaissance tool for TCP port scanning, banner grabbing, service fingerprinting, risk assessment, vulnerability detection, and security reporting.

---

# 📌 Overviewgit status

Port Banner Analyzer Pro is an advanced network reconnaissance and security analysis tool developed using Python.

The tool scans TCP ports, collects service banners, identifies running services, detects software versions, analyzes security risks, detects known vulnerabilities, and generates detailed security reports.

This project demonstrates practical implementation of Python for Cyber Security concepts including:

- Network Programming
- TCP Socket Communication
- Multi-threading
- Banner Grabbing
- Service Fingerprinting
- Vulnerability Detection
- Risk Assessment Automation


---

# 🎬 Demo


<p align="center">
  <img src="screenshots/demo.gif" alt="Port Banner Analyzer Pro Demo" width="900">
</p>



# 🚀 Features

## 🔹 Network Scanning

Perform fast and efficient TCP port scanning with concurrent execution for improved performance.

✅ TCP Port Scanner  
✅ Multi-threaded scanning using ThreadPoolExecutor  
✅ Fast concurrent port scanning  
✅ Custom port range support  
✅ Timeout control  
✅ Live scan progress counter  


## 🔹 Banner Grabbing & Analysis

Collect and analyze service banners to identify running services and extract useful information.

✅ TCP Banner Collection  
✅ Smart HTTP Request Handling  
✅ SSH Banner Handling  
✅ Banner Cleaning & Truncation  
✅ Automatic service detection  


## 🔹 Service Fingerprinting

Identify software, versions, vendors, and operating system hints using banner fingerprinting.

✅ Regex-based service detection  
✅ Software identification  
✅ Version extraction  
✅ Vendor detection  
✅ Operating system hint detection  


## 🔹 Security Risk Analysis

Analyze detected services for known risks, vulnerabilities, CVEs, and calculate security severity.

✅ Service Risk Detection  
✅ CVE Detection  
✅ Security Risk Reporting  
✅ Risk Score Engine  
✅ Severity Calculation  
✅ Security Recommendation System  


Risk Levels:

- LOW
- MEDIUM
- HIGH
- CRITICAL


## 🔹 Reporting System

Generate structured reports for documentation and further security analysis.

✅ JSON Report Export  
✅ CSV Report Export  
✅ Timestamped Reports  
✅ Risk Score Export  
✅ Severity Report Export  


## 🔹 Professional CLI

Provide a clean and user-friendly command-line interface with robust error handling.

✅ argparse based command interface  
✅ Version system  
✅ Colored terminal output using Colorama  
✅ Invalid hostname handling  
✅ Error handling  
✅ KeyboardInterrupt handling  
✅ Global exception handling  


## 🔹 Logging System

Maintain detailed logs for debugging, troubleshooting, and scan history.

✅ Professional logging system  
✅ Scan activity logging  
✅ Error tracking  
✅ Debug information storage  


---

# 🧪 Testing

Port Banner Analyzer Pro includes automated testing using **pytest**.

Run tests:

```bash
pytest


# 🗂️ Project Architecture


```text
PortBannerAnalyzerPro/

│
├── banner_analyzer.py
│       Main CLI Application
│
├── banner_test_server.py
│       Local Banner Testing Server
│
├── core/
│
│   ├── scanner.py
│   │       TCP Port Scanning Engine
│   │
│   ├── banner.py
│   │       Banner Grabbing Module
│   │
│   ├── analyzer.py
│   │       Service Fingerprinting & Analysis Engine
│   │
│   ├── risk.py
│   │       Security Risk Detection Module
│   │
│   ├── risk_score.py
│   │       Risk Score Calculation Engine
│   │
│   ├── cve_db.py
│   │       Vulnerability Database
│   │
│   ├── exporter.py
│   │       JSON & CSV Report Exporter
│   │
│   ├── logger.py
│   │       Logging System
│   │
│   ├── colors.py
│   │       CLI Color Management
│   │
│   └── utils.py
│           Utility Functions
│
├── tests/
│   └── test_analyzer.py
│       Automated Pytest Tests
│
├── sample_reports/
│   ├── sample_scan_report.csv
│   └── sample_scan_report.json
│
├── screenshots/
│   ├── demo.gif
│   ├── report-export.png
│   └── risk-analysis.png
│
├── reports/
│       Generated Scan Reports (Ignored)
│
├── logs/
│       Application Logs (Ignored)
│
├── pytest.ini
│       Pytest Configuration
│
└── requirements.txt
        Project Dependencies

# 📸 Screenshots

## 📸 Screenshots

### 🔍 Risk Analysis

![Risk Analysis](screenshots/risk-analysis.png)


### 📊 Report Export

![Report Export](screenshots/report-export.png)

# 🛠 Technologies Used

- Python 3.14
- TCP Socket Programming
- ThreadPoolExecutor
- Argparse CLI
- Colorama
- Regular Expressions
- JSON & CSV Reporting
- Pytest


# ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/abdullah-cyberr/port-banner-analyzer-pro.git