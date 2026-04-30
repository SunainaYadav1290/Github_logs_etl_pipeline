# GitHub Logs ETL Pipeline
## 🔹 Overview

This project extracts issue data from the GitHub API, processes it using PySpark, and stores it in Parquet format for analysis.

## 🔹 Tech Stack
```
Python
PySpark
REST API (GitHub API)
```
## 🔹 Project Structure

```
github-logs-etl-pipeline/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── main.py
│
├── README.md
├── requirements.txt
├── .gitignore  

```
## 🔹 ETL Flow

### 1. Extract
- Fetch data from GitHub API using `requests`
- Handle API errors and log responses

### 2. Transform
- Convert timestamps to proper format
- Extract features like day and hour
- Classify logs into ERROR / INFO
- Aggregate data for analysis

### 3. Load
- Store processed data in Parquet format for optimized querying
## 🔹 How to Run

```bash id="k8d3pn"
pip install -r requirements.txt
python -m src.main
```
## 🔹 Output
Cleaned and aggregated logs stored in Parquet format