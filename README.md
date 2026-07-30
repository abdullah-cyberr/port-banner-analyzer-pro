# 🔍 Port Banner Analyzer Pro

![Python](https://img.shields.io/badge/Python-3-blue)
![Security](https://img.shields.io/badge/Focus-Cyber%20Security-red)
![License](https://img.shields.io/badge/License-Educational-green)

A professional Python-based cybersecurity reconnaissance tool for TCP port scanning, banner grabbing, service fingerprinting, risk assessment, vulnerability detection, and security reporting.

---

# 📌 Overview

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

# 🚀 Features

## 🔹 Network Scanning

✅ TCP Port Scanner  
✅ Multi-threaded scanning using ThreadPoolExecutor  
✅ Fast concurrent port scanning  
✅ Custom port range support  
✅ Timeout control  
✅ Live scan progress counter  


## 🔹 Banner Grabbing & Analysis

✅ TCP Banner Collection  
✅ Smart HTTP Request Handling  
✅ SSH Banner Handling  
✅ Banner Cleaning & Truncation  
✅ Automatic service detection  


## 🔹 Service Fingerprinting

✅ Regex-based service detection  
✅ Software identification  
✅ Version extraction  
✅ Vendor detection  
✅ Operating system hint detection  


## 🔹 Security Risk Analysis

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

✅ JSON Report Export  
✅ CSV Report Export  
✅ Timestamped Reports  
✅ Risk Score Export  
✅ Severity Report Export  


## 🔹 Professional CLI

✅ argparse based command interface  
✅ Version system  
✅ Colored terminal output using Colorama  
✅ Invalid hostname handling  
✅ Error handling  
✅ KeyboardInterrupt handling  
✅ Global exception handling  


## 🔹 Logging System

✅ Professional logging system  
✅ Scan activity logging  
✅ Error tracking  
✅ Debug information storage  


---

# 🏗️ Project Architecture

```text
PortBannerAnalyzerPro/

│
├── banner_analyzer.py
│       Main CLI Application
│
├── core/
│
│   ├── scanner.py
│   │       TCP Port Scanner Engine
│   │
│   ├── banner.py
│   │       Banner Grabbing Module
│   │
│   ├── analyzer.py
│   │       Service Fingerprinting Engine
│   │
│   ├── risk.py
│   │       Risk Score & Security Analysis Engine
│   │
│   ├── colors.py
│   │       CLI Color Management
│   │
│   └── logger.py
│           Logging System
│
├── reports/
│       JSON & CSV Reports
│
├── logs/
│       Application Logs
│
├── test_server.py
│       Local Testing Server
│
└── requirements.txt
```

# 📸 Screenshots