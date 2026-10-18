# Flipping the Metric: A Time-Series-First Approach to Applied Econometrics

[![License: Open Source](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)

This repository hosts the official turn-key curriculum architecture, scaffolded lab infrastructure, and programmatic frameworks for the **"Flipped Metric"** approach to undergraduate and terminal Master's econometrics. 

---

## ⚙️ Faculty Installation & Local Deployment Guide

### 1. Install Computational Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Access Keys
```bash
# macOS / Linux
export FRED_API_KEY="your_actual_api_key_here"

# Windows (PowerShell)
$env:FRED_API_KEY="your_actual_api_key_here"
```

### 3. Run the Master Orchestration Pipeline
```bash
python flipped_metric_master_template.py
```