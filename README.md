# xetra-etl-project - data engineering project

# A production-ready ETL program using Object-Oriented Programming(OOP) method

-  Tools used for programming: Python 3.10, Jupyter Notebook, Git and Github, Visual Studio Code, and the Python packages Pandas, boto3, pyyaml, awscli, jupyter, pylint, moto, coverage and the memory-profiler


The ETL project used the Xetra dataset. Xetra stands for Exchange Electronic Trading and it is the trading platform of the Deutsche Börse Group.

The ETL Pipeline extracts the Xetra dataset from the AWS S3 source bucket on a scheduled basis, create a report using transformations and load the transformed data to another AWS S3 target bucket.

The production environment for the ETL pipeline for consists or will consist of 
- [x] a GitHub Code repository
- [ ]  a DockerHub Image Repository
- [ ]  an execution platform (Kubernetes) 
- [ ]  an Orchestration tool (the container-native Kubernetes workflow engine Argo Workflows / Apache Airflow)
