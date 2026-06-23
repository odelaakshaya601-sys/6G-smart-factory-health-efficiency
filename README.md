# Manufacturing Process Health and Operational Efficiency Analysis in 6G-Enabled Smart Factories

## 📌 Project Overview
This data analytics and machine learning repository evaluates real-time Industrial IoT (IIoT) sensor telemetry streaming through a high-speed 6G network framework. The project aims to minimize unscheduled factory downtime and maximize production line output.

## 🎯 Strategic Modules

### 1. Process Health & Predictive Maintenance (`notebooks/01_exploratory_analysis.py`)
* Automatically scans incoming raw factory telemetry logs.
* Monitors mechanical fluctuations (vibrations, temperatures, voltage levels) to pinpoint equipment anomalies before a physical breakdown occurs.

### 2. Operational Efficiency & OEE Analysis (`notebooks/02_operational_efficiency.py`)
* Computes production timeline distributions based on active machine states.
* Tracks micro-stoppages to calculate the plant's **Overall Equipment Effectiveness (OEE)** and Availability rates.

### 3. Machine Learning Predictive Modeling (`notebooks/03_risk_prediction.py`)
* Implements an intelligent **Random Forest Classification** algorithm.
* Analyzes high-frequency sensor readings to predict production risk profiles (`High`, `Medium`, `Low`) to guide factory maintenance schedules.

## 📂 Project Architecture
* `data/raw/` - Houses the raw `Thales_Group_Manufacturing.csv` industrial dataset.
* `notebooks/` - Contains the Python execution scripts for cleaning, OEE calculations, and predictive modeling.
* `requirements.txt` - Configuration file defining the required library versions (Pandas, Scikit-Learn, Matplotlib, Seaborn).

## 🛠️ Technology Stack
* **Core Language:** Python 3.10+
* **Data Pipelines & Visualization:** Pandas, NumPy, Matplotlib, Seaborn
* **Predictive AI Framework:** Scikit-Learn (Random Forest Engine)
*
