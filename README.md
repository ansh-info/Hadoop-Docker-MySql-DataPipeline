# Property and Crime Data Analysis

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup and Environment](#setup-and-environment)
- [Data Collection](#data-collection)
- [Data Storage in HDFS](#data-storage-in-hdfs)
- [Data Processing](#data-processing)
- [Failure Test](#failure-test)
- [Data Ingestion into MySQL](#data-ingestion-into-mysql)
- [Business Insights](#business-insights)
- [Challenges and Solutions](#challenges-and-solutions)

## Introduction
This project involves setting up a data engineering pipeline to collect, store, process, and analyze property and crime data using Hadoop, Docker, MySQL, Tailscale, and Selenium.

## Project Overview
- **Objective:** Analyze property and crime data to derive meaningful insights.
- **Scope:** Collect data through web scraping, store in HDFS, process using Hadoop, and analyze with MySQL.

## Technologies Used
- Hadoop
- Docker
- MySQL
- Tailscale
- Selenium
- Python

## Setup and Environment
### Virtual Machines Setup
- **Step:** Installed Ubuntu on VirtualBox for each VM.
- **Action:** Configured each VM with necessary packages including Docker and Docker Compose.

### Networking with Tailscale
- **Step:** Installed and configured Tailscale on all VMs.
- **Action:** Created a secure virtual network to enable communication between VMs.

### Docker Swarm Initialization
- **Step:** Initialized Docker Swarm on the master node and joined worker nodes.
- **Action:** Used Docker Swarm for container orchestration.

### Image of Setup Process
![Setup Process](path/to/setup_image.png)

## Data Collection
### Web Scraping with Selenium
- **Step:** Installed Selenium and Chrome WebDriver.
- **Action:** Developed scripts to scrape property and crime data from various websites.

### Data Collection Process
![Data Collection Process](path/to/data_collection_image.png)

## Data Storage in HDFS
- **Step:** Configured HDFS on the Hadoop cluster.
- **Action:** Stored scraped data in HDFS with appropriate partitioning and replication.

## Data Processing
### Hadoop Job Development
- **Step:** Developed and executed Hadoop jobs for data cleaning and transformation.
- **Action:** Used MapReduce for distributed processing.

## Failure Test
- **Step:** Conducted data read/write operations while intentionally shutting down a worker node.
- **Action:** Verified system resilience and fault tolerance.

## Data Ingestion into MySQL
### Database Design
- **Step:** Created a relational database schema in MySQL.
- **Action:** Developed scripts to ingest data from HDFS to MySQL.

### Image of Database Schema
![Database Schema](/images/datamodeling.png)

## Business Insights
### Query Development
- **Step:** Developed SQL queries to extract insights from the database.
- **Action:** Generated graphs and tables to present the results.

### Business Insights Visualization
![Business Insights](path/to/business_insights_image.png)

## Challenges and Solutions
- **Setting Up the Environment:**
  - **Challenge:** Ensuring all VMs were correctly configured and able to communicate.
  - **Solution:** Thoroughly followed installation and configuration guidelines for Ubuntu, Docker, and Tailscale.
  
- **Docker Swarm Initialization:**
  - **Challenge:** Properly initializing Docker Swarm and ensuring all worker nodes joined without issues.
  - **Solution:** Carefully followed the steps and used diagnostic tools to resolve issues.

- **Data Collection:**
  - **Challenge:** Handling dynamic content and pagination on websites while scraping data.
  - **Solution:** Utilized Selenium’s capabilities and implemented robust error handling.

- **Storing Data in HDFS:**
  - **Challenge:** Ensuring data was correctly partitioned and replicated in HDFS.
  - **Solution:** Configured HDFS with appropriate settings and verified data storage.

- **Performing a Failure Test:**
  - **Challenge:** Simulating node failure and ensuring the system remained operational.
  - **Solution:** Conducted controlled shutdowns of worker nodes and verified the system’s fault tolerance.

- **Data Ingestion into MySQL:**
  - **Challenge:** Ensuring data integrity and handling large volumes of data during ingestion.
  - **Solution:** Developed a robust Python script with batch processing and error handling.

- **Developing Business Insights and Queries:**
  - **Challenge:** Formulating meaningful queries and interpreting results to derive insights.
  - **Solution:** Conducted thorough data analysis and used SQL queries to extract relevant data.

## Video Demonstration
[Watch the video](video/Video.mov)

---
