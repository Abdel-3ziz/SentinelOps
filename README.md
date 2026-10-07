# 🛡️ SentinelOps

### Intelligent Network Intrusion Detection & Prevention System

SentinelOps is a graduation project that combines **Machine Learning, Network Security, and DevOps** to build an intelligent system for detecting malicious network traffic and automatically responding to detected attacks.

The system is designed to analyze network traffic, extract relevant features, classify traffic using a Machine Learning model, and perform automated prevention actions such as blocking malicious source IP addresses through firewall rules.

---

## 🎯 Project Objectives

SentinelOps aims to:

* Detect malicious network traffic using Machine Learning.
* Identify different types of network attacks.
* Analyze real network traffic using Scapy.
* Extract network traffic features for ML inference.
* Automatically respond to detected attacks.
* Block malicious source IP addresses using firewall rules.
* Generate security alerts.
* Provide an API for detection and system integration.
* Containerize the system using Docker.
* Deploy the system using Kubernetes.
* Automate CI/CD using Jenkins.
* Monitor the system using Prometheus and Grafana.

---

# 🏗️ System Architecture

```text
                         Network Traffic
                                │
                                ▼
                     ┌─────────────────────┐
                     │        Scapy        │
                     │  Traffic Collector  │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ Feature Extraction  │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │   ML Detection      │
                     │   Random Forest     │
                     └──────────┬──────────┘
                                │
                       ┌────────┴────────┐
                       │                 │
                    BENIGN             ATTACK
                       │                 │
                       ▼                 ▼
                     Allow      ┌─────────────────┐
                                │ Response Engine │
                                └────────┬────────┘
                                         │
                                ┌────────┴────────┐
                                │                 │
                                ▼                 ▼
                           Firewall Block      Alert
                           Source IP          Security
                                │
                                ▼
                         Monitoring System
                       Prometheus + Grafana
```

---

# 🧠 Machine Learning Pipeline

The Machine Learning pipeline prepares the CICIDS2017 dataset and trains the intrusion detection model.

```text
CICIDS2017 Dataset
        │
        ▼
Data Validation
        │
        ▼
Data Cleaning
        │
        ▼
Duplicate Removal
        │
        ▼
Feature Processing
        │
        ▼
Feature Selection
        │
        ▼
Train / Test Split
        │
        ▼
Random Forest Training
        │
        ▼
Model Evaluation
```

---

# 📊 Dataset

The project currently uses the **CICIDS2017** dataset for Machine Learning training and evaluation.

The dataset contains both benign traffic and different types of network attacks.

The project works with multiple attack classes, including:

* BENIGN
* DDoS
* PortScan
* DoS GoldenEye
* DoS Hulk
* DoS Slowhttptest
* DoS slowloris
* FTP-Patator
* SSH-Patator
* Bot
* Heartbleed
* Infiltration
* Web Attacks

> The exact classes used by the final model depend on the preprocessing and classification configuration.

---

# 📁 Project Structure

```text
SentinelOps/
│
├── README.md
├── .gitignore
│
├── preprocessing.py
├── validate_data.py
├── train_test_split.py
├── feature_selection.py
├── train_model.py
├── train_balanced_rf.py
├── evaluate_model.py
├── feature_importance.py
├── analyze_errors.py
├── analyze_top_features.py
├── class_distribution.py
├── distribution_analysis.py
├── confusion_matrix.py
└── eda.py
```

### Dataset and model directories

The following directories/files are intentionally excluded from GitHub because of their large size:

```text
data/raw/
data/processed/
archive.zip
models/*.pkl
```

They should be provided separately.

---

# 🔍 Data Validation

Before training the model, the dataset is checked for common data-quality problems.

The validation process checks:

* Dataset shape
* Label column
* Missing values
* Infinite values
* Duplicate rows
* Data types
* Class distribution

Run:

```bash
python validate_data.py
```

---

# 🧹 Data Preprocessing

The preprocessing stage prepares the raw CICIDS2017 files for Machine Learning.

Main operations include:

* Loading the dataset files.
* Combining the required data.
* Cleaning the data.
* Handling missing values.
* Handling infinite values.
* Removing duplicate records.
* Converting features to numeric values.
* Preparing the target label.

Run:

```bash
python preprocessing.py
```

---

# 🎯 Feature Selection

Feature selection is used to identify the most useful network traffic features and reduce unnecessary features.

Run:

```bash
python feature_selection.py
```

The selected features are then used during model training.

---

# 🌲 Machine Learning Model

The main Machine Learning algorithm currently used by SentinelOps is:

## Random Forest

Random Forest was selected because it is well suited for tabular network traffic data and can handle nonlinear relationships between network features.

Advantages include:

* Good performance for classification.
* Works well with numerical network traffic features.
* Handles nonlinear relationships.
* Relatively robust to noisy data.
* Provides feature importance.
* Suitable for multiclass classification.

---

# 🏋️ Model Training

Train the main Random Forest model:

```bash
python train_model.py
```

A balanced Random Forest implementation is also available:

```bash
python train_balanced_rf.py
```

The trained models are stored locally under:

```text
models/
```

---

# 📈 Model Evaluation

The project contains several scripts for analyzing the trained model.

### Evaluate the model

```bash
python evaluate_model.py
```

### Confusion Matrix

```bash
python confusion_matrix.py
```

### Feature Importance

```bash
python feature_importance.py
```

### Error Analysis

```bash
python analyze_errors.py
```

### Top Features

```bash
python analyze_top_features.py
```

### Class Distribution

```bash
python class_distribution.py
```

### Distribution Analysis

```bash
python distribution_analysis.py
```

### Exploratory Data Analysis

```bash
python eda.py
```

---

# 📊 Current ML Pipeline

The current ML pipeline has successfully reached the training stage.

The current training dataset contains approximately:

```text
Samples: 2,016,638
Input Features: 70
```

The primary classifier is:

```text
Random Forest
```

The project also contains a balanced Random Forest implementation for handling class imbalance.

---

# 🌐 Real-Time Detection

The final system is designed to move from offline dataset-based classification to real-time network traffic detection.

The planned real-time workflow is:

```text
Live Network Traffic
        │
        ▼
      Scapy
        │
        ▼
Feature Extraction
        │
        ▼
ML Model
        │
        ▼
Prediction
        │
        ├───────────────┐
        │               │
      BENIGN          ATTACK
        │               │
        ▼               ▼
      Allow      Response Engine
                        │
                 ┌──────┴──────┐
                 │             │
                 ▼             ▼
             Firewall       Alert
               Block
```

Scapy will be responsible for capturing network packets and collecting the information required to generate the ML features.

---

# 🛡️ Intrusion Prevention

SentinelOps is designed as both an **IDS and IPS**.

### IDS

The system detects and classifies suspicious traffic using Machine Learning.

```text
Traffic
   ↓
Feature Extraction
   ↓
ML Prediction
   ↓
Attack Detection
```

### IPS

After an attack is detected, the system can perform an automated prevention action.

```text
Attack Detected
      ↓
Extract Source IP
      ↓
Verify Prediction
      ↓
Firewall Rule
      ↓
Block Source IP
      ↓
Generate Alert
```

The prevention mechanism will use **Firewall rules** to block malicious source IP addresses.

---

# 🐍 Scapy

Scapy is used in the real-time traffic collection layer.

Its responsibilities include:

* Capturing packets.
* Reading packet information.
* Identifying network protocols.
* Extracting source and destination information.
* Collecting traffic statistics.
* Preparing information required for ML feature extraction.

Scapy connects the real network environment with the Machine Learning detection pipeline.

---

# ⚡ FastAPI

FastAPI will provide the API layer between the different system components.

The API is designed to support:

* Traffic analysis requests.
* ML predictions.
* Detection results.
* Alert information.
* System health checks.
* Integration with other services.

Expected flow:

```text
Scapy
  │
  ▼
FastAPI
  │
  ▼
ML Model
  │
  ▼
Prediction
  │
  ▼
Response Engine
```

---

# 🐳 Docker

The system components will be containerized using Docker.

Expected services include:

```text
Docker
│
├── Traffic Collector
├── Detection API
├── ML Model Service
├── Response Engine
└── Monitoring
```

Docker provides:

* Reproducible environments.
* Easier deployment.
* Dependency isolation.
* Portable services.

---

# ☸️ Kubernetes

Kubernetes will be used to deploy and manage the containerized components.

Expected architecture:

```text
Kubernetes Cluster
│
├── Traffic Collector
│
├── Detection API
│
├── ML Service
│
├── Response Engine
│
└── Monitoring
    ├── Prometheus
    └── Grafana
```

Kubernetes provides:

* Container orchestration.
* Scaling.
* Service discovery.
* Deployment management.
* Self-healing.
* Resource management.

---

# 🔄 CI/CD with Jenkins

Jenkins will automate the CI/CD pipeline.

```text
Developer
    │
    ▼
GitHub
    │
    ▼
Jenkins
    │
    ├── Build
    ├── Test
    ├── Docker Build
    ├── Image Push
    │
    ▼
Kubernetes
    │
    ▼
SentinelOps
```

The goal is to automatically build, test, package, and deploy changes.

---

# 📊 Monitoring

SentinelOps will use:

* **Prometheus** for metrics collection.
* **Grafana** for monitoring and visualization.

Possible metrics include:

* Packets processed.
* Number of detected attacks.
* Number of blocked IPs.
* Detection latency.
* Model inference time.
* API health.
* Container health.
* System resource usage.

Example:

```text
SentinelOps
     │
     ▼
Metrics
     │
     ▼
Prometheus
     │
     ▼
Grafana
     │
     ▼
Security Dashboard
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Abdel-3ziz/SentinelOps.git
cd SentinelOps
```

## 2. Install Python Dependencies

If a virtual environment is preferred:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

> `requirements.txt` should contain the Python dependencies required by the current implementation.

---

# 📥 Dataset Setup

The CICIDS2017 dataset is **not included in this repository** because of its large size.

Download the dataset separately and place the CSV files inside:

```text
data/raw/
```

Expected structure:

```text
data/
└── raw/
    ├── Monday-WorkingHours.pcap_ISCX.csv
    ├── Tuesday-WorkingHours.pcap_ISCX.csv
    ├── Wednesday-workingHours.pcap_ISCX.csv
    ├── Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
    ├── Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
    ├── Friday-WorkingHours-Morning.pcap_ISCX.csv
    ├── Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
    └── Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
```

---

# 🚀 Running the ML Pipeline

Run the following steps in order.

### Step 1 — Validate

```bash
python validate_data.py
```

### Step 2 — Preprocess

```bash
python preprocessing.py
```

### Step 3 — Feature Selection

```bash
python feature_selection.py
```

### Step 4 — Train/Test Split

```bash
python train_test_split.py
```

### Step 5 — Train Random Forest

```bash
python train_model.py
```

### Step 6 — Evaluate

```bash
python evaluate_model.py
```

---

# 👥 Team Workflow

Clone the repository:

```bash
git clone https://github.com/Abdel-3ziz/SentinelOps.git
```

Each team member should obtain the dataset separately and place it inside:

```text
data/raw/
```

Do **not** commit the dataset to GitHub.

Before pushing changes:

```bash
git status
```

Make sure that datasets, generated files, credentials, and large files are not included.

Then:

```bash
git add .
git commit -m "Describe your changes"
git push
```

---

# 🚫 Files Not Stored in GitHub

The following are intentionally excluded:

```text
data/raw/
data/processed/
archive.zip
models/*.pkl
```

These files should be distributed separately using shared storage when required.

This keeps the GitHub repository lightweight and focused on source code.

---

# 🔐 Security

Never commit sensitive information to the repository.

Do not upload:

* API keys
* Passwords
* AWS credentials
* Private keys
* Access tokens
* `.env` files
* Database passwords
* Personal credentials

Use environment variables or a proper secret-management system instead.

---

# 🗺️ Project Roadmap

## ✅ Completed

* [x] CICIDS2017 dataset preparation
* [x] Data validation
* [x] Missing-value checking
* [x] Infinite-value checking
* [x] Duplicate removal
* [x] Data preprocessing
* [x] Feature selection
* [x] Train/test preparation
* [x] Random Forest training
* [x] Balanced Random Forest implementation
* [x] Model evaluation scripts
* [x] Confusion matrix analysis
* [x] Feature importance analysis
* [x] Error analysis
* [x] Class distribution analysis

## 🚧 In Progress / Planned

* [ ] Real-time network traffic collection using Scapy
* [ ] Real-time feature extraction
* [ ] FastAPI detection service
* [ ] ML inference integration
* [ ] Firewall-based automated prevention
* [ ] Security alert system
* [ ] Docker containerization
* [ ] Kubernetes deployment
* [ ] Jenkins CI/CD pipeline
* [ ] Prometheus monitoring
* [ ] Grafana dashboard
* [ ] End-to-end system integration
* [ ] Final security testing
* [ ] Performance testing

---

# 🎓 Graduation Project

SentinelOps is a graduation project focused on integrating:

* Machine Learning
* Network Security
* Intrusion Detection Systems
* Intrusion Prevention Systems
* Network Traffic Analysis
* Automated Firewall Response
* Docker
* Kubernetes
* Jenkins
* Prometheus
* Grafana

The project aims to demonstrate how AI and DevOps can be combined to create an automated, scalable, and monitorable network security platform.

---

# 🔗 Repository

GitHub:

https://github.com/Abdel-3ziz/SentinelOps

---

# 🚀 Project Vision

The final goal of SentinelOps is to evolve from an offline Machine Learning classifier into a complete intelligent security platform.

```text
                       SENTINELOPS
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
      Detection         Prevention        Monitoring
          │                 │                 │
          ▼                 ▼                 ▼
         ML             Firewall         Prometheus
          │                 │                 │
          └─────────────────┼─────────────────┘
                            │
                            ▼
                       Kubernetes
                            │
                            ▼
                         Jenkins
                            │
                            ▼
                    Automated Security
```

### Detect → Analyze → Prevent → Monitor → Automate
