# GitHub Logs ETL Pipeline
🔹 Overview

This project extracts issue data from the GitHub API, processes it using PySpark, and stores it in Parquet format for analysis.

🔹 Tech Stack
Python,
PySpark,
REST API (GitHub API)
## 🔹 Project Structure


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


# 🔹 ETL Flow
## Extract
Fetch data from GitHub API using requests
Handle errors and log responses
## Transform
Convert timestamps
Extract day and hour
Classify logs (ERROR / INFO)
Aggregate logs
## Load
Store output in Parquet format
