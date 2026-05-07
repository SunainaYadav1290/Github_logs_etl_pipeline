# GitHub Logs ETL Pipeline
## 🔹 Overview

This project builds an end-to-end ETL pipeline using PySpark to extract issue data from the GitHub API, clean and transform nested JSON data, and store the processed output in partitioned Parquet format for analytics.

## 🔹 Tech Stack
```
Python
PySpark
REST API (GitHub API)
Parquet
Logging
```
## 🔹 Project Structure

```
github-logs-etl-pipeline/
│
├── src/
│   ├── extract.py
│   ├── preprocess.py
│   ├── transform.py
│   ├── load.py
│   ├── utils.py
│   ├── main.py
│
├── output/
├── README.md
├── requirements.txt
├── .gitignore
```
### Features
Retry strategy for API failures
Data cleaning using PySpark
Lazy evaluation with Spark transformations
Partitioned Parquet storage
Modular ETL architecture
Logging for monitoring pipeline execution

### 1. Extract
Fetch data from GitHub API using requests
Implemented retry mechanism for failed API calls
Handle API errors and logging
Extract nested JSON data

### 2. Preprocess
Clean raw API data
Handle missing values and duplicates
Prepare data for transformation

### 3. Transform
Convert timestamps to proper format
Flatten/select required fields from nested JSON
Extract features like day and hour
Classify logs into ERROR / INFO
Aggregate logs using PySpark groupBy

### 4. Load
Store processed data in partitioned Parquet format
Partition data by date for optimized querying

🔹 Utilities
Reusable helper functions and logging utilities are maintained in utils.py for better modularity and maintainability.

### Output Structure
output/
   date=2026-05-07/
       part-0000.parquet
