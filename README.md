# 🛡️ SentinelOps — Intelligent Network Intrusion Detection & Prevention System

> **AI-powered IDS/IPS for network attack detection, analysis, and automated prevention**

SentinelOps is a graduation project that combines **Machine Learning, Network Security, and DevOps** to build an intelligent system capable of detecting suspicious network traffic and taking automated prevention actions.

The system analyzes network traffic, extracts relevant features, classifies the traffic using a Machine Learning model, and can automatically respond to detected attacks by applying firewall blocking rules and generating alerts.

---

## 🎯 Project Objectives

The main objectives of SentinelOps are:

* Detect malicious network traffic using Machine Learning.
* Identify different types of network attacks.
* Analyze network traffic using packet-level information.
* Automatically respond to detected attacks.
* Block malicious source IP addresses using firewall rules.
* Generate security alerts.
* Containerize the system using Docker.
* Deploy and manage components using Kubernetes.
* Automate the CI/CD workflow using Jenkins.
* Monitor the system using Prometheus and Grafana.
* Provide a scalable architecture suitable for real-world environments.

---

## 🏗️ High-Level Architecture

```text
                    ┌─────────────────────┐
                    │   Network Traffic   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       Scapy         │
                    │ Traffic Collector   │
                    └──────────┬──────────┘
                               │
                               │ Features
                               ▼
                    ┌─────────────────────┐
                    │    ML Detection     │
                    │  Random Forest      │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                 Normal                Attack
                    │                     │
                    ▼                     ▼
                  Allow          ┌─────────────────┐
                                 │ Response Engine │
                                 └────────┬────────┘
                                          │
                             ┌────────────┴────────────┐
                             │                         │
                             ▼                         ▼
                       Firewall Block             Alert
                       Source IP                  Security
                             │
                             ▼
                    ┌─────────────────────┐
                    │ Monitoring / Logs   │
                    │ Prometheus/Grafana  │
                    └─────────────────────┘
```

---

# 🧠 Machine Learning Pipeline

The Machine Learning pipeline is responsible for transforming raw network traffic into a format that can be processed by the detection model.

```text
Raw CICIDS2017 Dataset
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

SentinelOps currently uses the **CICIDS2017** dataset for Machine Learning training and evaluation.

The dataset contains benign network traffic as well as multiple attack categories.

### Main attack categories used by the project include:

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

> The exact classes depend on the preprocessing and classification configuration used in the current project version.

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
├── eda.py
│
├── data/
│   ├── raw/
│   │   └── CICIDS2017 CSV files
│   │
│   └── processed/
│       ├── cicids2017_clean.csv
│       ├── cicids2017_features_selected.csv
│       ├── train.csv
│       └── test.csv
│
└── models/
    ├── random_forest.pkl
    └── balanced_random_forest.pkl
```

> `data/` and trained model files are excluded from the GitHub repository because of their large size.

---

# 🔍 Data Validation

Before training, the dataset is validated to ensure that it is suitable for Machine Learning.

The validation process checks:

* Dataset shape
* Label column existence
* Missing values
* Infinite values
* Duplicate records
* Data types
* Label/class distribution

Run:

```bash
python validate_data.py
```

---

# 🧹 Data Preprocessing

The preprocessing stage prepares the CICIDS2017 dataset for Machine Learning.

Main operations include:

* Combining dataset files
* Cleaning column names
* Removing invalid values
* Handling infinite values
* Handling missing values
* Removing duplicate rows
* Converting features to numeric format
* Preparing the target label

Run:

```bash
python preprocessing.py
```

---

# 🎯 Feature Selection

Feature selection is used to reduce unnecessary features and keep the most useful network traffic characteristics for the Machine Learning model.

Run:

```bash
python feature_selection.py
```

The selected features are then used for model training.

---

# 🌲 Machine Learning Model

The current main detection model is based on:

### Random Forest

Random Forest was selected because it:

* Works well with tabular network traffic data.
* Handles nonlinear relationships.
* Supports many numerical features.
* Is relatively robust to noisy data.
* Provides feature importance.
* Performs well for classification problems.

Training:

```bash
python train_model.py
```

A balanced Random Forest training pipeline is also available:

```bash
python train_balanced_rf.py
```

---

# 📈 Model Evaluation

The trained model can be evaluated using:

```bash
python evaluate_model.py
```

Additional analysis tools are available for:

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

### Top Feature Analysis

```bash
python analyze_top_features.py
```

### Class Distribution

```bash
python class_distribution.py
```

### Exploratory Data Analysis

```bash
python eda.py
```

---

# 🧪 Current ML Training Results

The current project pipeline has successfully reached the Machine Learning training stage.

The training dataset contains approximately:

```text
2,016,638 samples
70 input features
```

The current primary classifier is:

```text
Random Forest
```

The trained model is saved locally as:

```text
models/random_forest.pkl
```

A balanced Random Forest implementation is also included:

```text
models/balanced_random_forest.pkl
```

---

# 🌐 Real-Time Traffic Detection

The final SentinelOps system is designed to move from offline dataset-based detection to real network traffic detection.

The planned flow is:

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
Machine Learning Model
        │
        ▼
Prediction
        │
        ├── BENIGN
        │      │
        │      ▼
        │    Allow
        │
        └── ATTACK
               │
               ▼
        Response Engine
               │
          ┌────┴────┐
          ▼         ▼
       Firewall    Alert
        Block
```

Scapy will be responsible for capturing packets and extracting the network information required by the ML detection pipeline.

---

# 🛡️ IPS Response

When malicious traffic is detected, SentinelOps is designed to move beyond detection and perform an automatic prevention action.

Example:

```text
Attack detected
      │
      ▼
Extract source IP
      │
      ▼
Verify prediction
      │
      ▼
Apply firewall rule
      │
      ▼
Block attacker IP
      │
      ▼
Generate alert
```

The prevention layer will use **Firewall rules** to block malicious source IP addresses.

---

# 🐳 DevOps Architecture

SentinelOps is designed using DevOps practices to make the system reproducible, deployable, and monitorable.

Main technologies:

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | ML and backend development   |
| Scapy      | Network traffic capture      |
| FastAPI    | API layer                    |
| Docker     | Containerization             |
| Kubernetes | Container orchestration      |
| Jenkins    | CI/CD automation             |
| Prometheus | Metrics collection           |
| Grafana    | Monitoring and visualization |
| Firewall   | Automated prevention         |

---

# 🔄 CI/CD Pipeline

Jenkins will automate the build, test, and deployment process.

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
    │
    ├── Test
    │
    ├── Docker Build
    │
    ├── Image Push
    │
    ▼
Kubernetes
    │
    ▼
SentinelOps
    │
    ▼
Monitoring
Prometheus + Grafana
```

---

# ☸️ Kubernetes

The system is designed to run as containerized workloads inside Kubernetes.

Expected components include:

```text
Kubernetes Cluster
│
├── Detection Service
│
├── Traffic Collector
│
├── Response Engine
│
└── Monitoring
    ├── Prometheus
    └── Grafana
```

Kubernetes provides:

* Container orchestration
* Scaling
* Service discovery
* Deployment management
* Self-healing
* Resource management

---

# 📊 Monitoring

Prometheus and Grafana will be used to monitor the operational state of SentinelOps.

Possible metrics include:

* Packets processed
* Detection requests
* Attack count
* Normal traffic count
* Detection latency
* Model response time
* Blocked IP count
* API availability
* Container health

Example monitoring flow:

```text
SentinelOps
     │
     │ Metrics
     ▼
Prometheus
     │
     ▼
Grafana
     │
     ▼
Security / Operations Dashboard
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Abdel-3ziz/SentinelOps.git
cd SentinelOps
```

---

## 2. Install Python Dependencies

Create a Python environment if desired:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not available yet, the project dependencies should be added before the final release.

---

# 📥 Dataset Setup

The CICIDS2017 dataset is **not included in the GitHub repository** because of its large size.

After downloading the dataset, place the CSV files inside:

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

Run the steps in the following order:

### Step 1 — Validate Dataset

```bash
python validate_data.py
```

### Step 2 — Preprocess Dataset

```bash
python preprocessing.py
```

### Step 3 — Select Features

```bash
python feature_selection.py
```

### Step 4 — Split Dataset

```bash
python train_test_split.py
```

### Step 5 — Train Random Forest

```bash
python train_model.py
```

### Step 6 — Evaluate Model

```bash
python evaluate_model.py
```

---

# 👥 Team Workflow

Each team member should:

```bash
git clone https://github.com/Abdel-3ziz/SentinelOps.git
```

Then obtain the dataset separately and place it inside:

```text
data/raw/
```

Do **not** commit the dataset to GitHub.

Before pushing code:

```bash
git status
```

Make sure large datasets and generated files are not included.

Then:

```bash
git add .
git commit -m "Describe your changes"
git push
```

---

# 🚫 Files Excluded from GitHub

The following files/directories are intentionally excluded:

```text
data/raw/
data/processed/
archive.zip
models/*.pkl
```

These files can be distributed separately using a shared storage location such as Google Drive or another dataset/model storage service.

---

# 🔐 Security Notes

Do not commit sensitive information such as:

* API keys
* Passwords
* Tokens
* AWS credentials
* Private keys
* `.env` files
* Personal access tokens

Use environment variables or secret-management solutions instead.

---

# 🗺️ Development Roadmap

### ✅ Completed

* [x] CICIDS2017 dataset collection
* [x] Dataset validation
* [x] Data cleaning
* [x] Duplicate removal
* [x] Feature preprocessing
* [x] Feature selection
* [x] Train/test preparation
* [x] Random Forest training
* [x] Model evaluation scripts
* [x] Feature importance analysis
* [x] Error analysis

### 🚧 In Progress / Planned

* [ ] Real-time traffic collection using Scapy
* [ ] Real-time feature extraction
* [ ] FastAPI detection API
* [ ] ML inference service
* [ ] Firewall-based automated prevention
* [ ] Security alert system
* [ ] Docker containerization
* [ ] Kubernetes deployment
* [ ] Jenkins CI/CD pipeline
* [ ] Prometheus monitoring
* [ ] Grafana dashboard
* [ ] End-to-end integration
* [ ] Final system testing

---

# 🎓 Academic Project

SentinelOps is developed as a **graduation project** combining:

* Network Security
* Intrusion Detection Systems
* Intrusion Prevention Systems
* Machine Learning
* Network Traffic Analysis
* DevOps
* Containerization
* Kubernetes
* Monitoring

The project aims to demonstrate how Machine Learning and DevOps can be combined to build an automated and scalable network security platform.

---

# 👨‍💻 Repository

**GitHub:**
https://github.com/Abdel-3ziz/SentinelOps

---

## ⭐ Project Vision

SentinelOps aims to evolve from a traditional offline Machine Learning classifier into a complete intelligent security platform:

```text
              SENTINELOPS
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
   Detection    Prevention   Monitoring
       │           │           │
       ▼           ▼           ▼
      ML        Firewall    Prometheus
       │           │           │
       └───────────┼───────────┘
                   ▼
              Kubernetes
                   │
                   ▼
                Jenkins
                   │
                   ▼
            Automated Security
```

**Detect → Analyze → Prevent → Monitor → Automate**
