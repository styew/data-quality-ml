\# Data Quality \& Machine Learning Application



\## 1. Project Description



This project is a web-based application for analyzing and cleaning datasets, with a focus on data quality.



The user can upload a dataset, for example in CSV format. The application analyzes the data and detects common data quality problems such as missing values, duplicate rows, invalid values, incorrect data types and inconsistent formats.



The detected problems are presented to the user in an understandable way. The user can then review the detected problems and apply appropriate cleaning operations.



After cleaning the dataset, the application provides basic statistics and visualizations to help the user understand the data.



As an additional feature, the application can provide basic Machine Learning functionality, such as using Linear Regression to make predictions based on the cleaned dataset.



\---



\## 2. Problem Statement



Datasets, especially CSV files, can contain various data quality problems.



Examples include:



\* Missing values

\* NaN values

\* Duplicate rows

\* Incorrect data types

\* Invalid values

\* Inconsistent formats

\* Incorrect or unexpected values



These problems often require manual inspection and cleaning before the data can be used for analysis or Machine Learning.



Users without programming or Python knowledge may have difficulties identifying and correcting these problems.



The project aims to provide a simple interface that helps users understand and improve the quality of their datasets without requiring them to write Python code.



\---



\## 3. Why Is This Problem Important?



Data quality is important because incorrect or incomplete data can lead to incorrect analysis and unreliable Machine Learning results.



Machine Learning models depend on the quality of the data used to train them. Problems such as missing values, incorrect formats or invalid values can negatively affect the results of a model.



The application therefore provides an intermediate layer between raw data and data analysis.



Instead of manually inspecting a dataset using programming tools, the user can upload the data and receive an understandable overview of its quality and the problems that need attention.



\---



\## 4. Proposed Solution



The application provides a workflow for data quality analysis and cleaning:



```text

Upload Dataset

&#x20;     ↓

Analyze Dataset

&#x20;     ↓

Detect Data Quality Problems

&#x20;     ↓

Show Problems to User

&#x20;     ↓

User Reviews / Selects Cleaning Operations

&#x20;     ↓

Apply Cleaning

&#x20;     ↓

Statistics \& Visualization

&#x20;     ↓

Export Cleaned Dataset

```



The system should guide the user through this process without requiring knowledge of Python or data-processing libraries.



\---



\## 5. Goals



\### G1. Dataset Upload



The system allows the user to upload a supported dataset, for example a CSV file.



\### G2. Data Quality Analysis



The system analyzes the uploaded dataset and provides an overview of its quality.



\### G3. Data Quality Issue Detection



The system identifies common problems in the dataset, such as:



\* Missing values

\* NaN values

\* Duplicate rows

\* Invalid values

\* Incorrect data types

\* Inconsistent formats



\### G4. Data Cleaning



The system allows the user to review detected problems and apply appropriate cleaning operations.



\### G5. Data Visualization and Statistics



The system provides basic statistics and visualizations to help the user understand the dataset.



\### G6. Dataset Export



The system allows the user to export the cleaned dataset.



\### G7. Basic Machine Learning



The system provides basic Machine Learning functionality using the cleaned dataset.



For example, the user can select suitable variables and use a basic model such as Linear Regression to make predictions.



\---



\## 6. Non-Goals



\### NG1. Replacement of Professional Data Analysis Systems



The system is not intended to replace professional data analysis or data science platforms.



\### NG2. Big Data



The system is not designed for Big Data or extremely large datasets.



\### NG3. Support for Every Data Format



The system will not support every possible data format. The initial implementation will focus on common and manageable formats such as CSV.



\### NG4. Advanced Machine Learning



The system will not provide complex Machine Learning functionality such as Deep Learning or highly specialized models.



The focus is on demonstrating basic Machine Learning functionality.



\---



\## 7. Target Users



\### TG1. Beginner Data Analysts



Users who have basic knowledge of data analysis but limited experience with programming or data-cleaning tools.



\### TG2. Small Businesses / Small Manufacturing Companies



Small organizations that work with datasets but do not necessarily have dedicated Data Science or Data Engineering teams.



\### TG3. Students



Students who want to analyze datasets and experiment with Machine Learning without implementing the entire data-cleaning process themselves.



\### TG4. Developers



Developers who want a simple tool for inspecting and preparing datasets before using them in their own applications or Machine Learning projects.



\---



\# 8. Functional Requirements



\## FR01. Dataset Upload



The system shall allow the user to upload a dataset for analysis.



The initial version shall support CSV files.



\---



\## FR02. File Format Validation



The system shall validate whether the uploaded file has a supported format.



If the uploaded file is not supported or cannot be processed, the system shall inform the user about the problem.



\---



\## FR03. Dataset Structure Analysis



The system shall analyze the structure of the uploaded dataset.



The analysis shall include, at minimum:



\* Number of rows

\* Number of columns

\* Column names

\* Data types

\* Number of values per column



\---



\## FR04. Missing Value Detection



The system shall detect missing values in the dataset.



The system shall provide information about which columns contain missing values and how many missing values were detected.



\---



\## FR05. Duplicate Value Detection



The system shall detect duplicate rows in the dataset.



The system shall inform the user about the number of duplicate rows detected.



\---



\## FR06. Invalid Format Detection



The system shall detect incorrect or inconsistent data formats within the dataset.



Examples include:



\* Different date formats

\* Unexpected data types

\* Values that do not match the expected format of a column



\---



\## FR07. Data Summary



The system shall provide the user with a summary of the uploaded dataset.



The summary shall contain basic statistical information, depending on the data type of the columns.



Examples include:



\* Number of rows

\* Number of columns

\* Mean

\* Minimum and maximum values

\* Median

\* Standard deviation

\* Number of missing values



\---



\## FR08. Cleaning Method Selection



The system shall allow the user to review detected data quality problems and select how they should be handled.



Depending on the detected problem, the system shall provide suitable cleaning options.



Examples include:



\* Remove rows

\* Replace missing values

\* Replace invalid values

\* Remove duplicate rows

\* Convert data types



The system shall not modify the dataset without the user's confirmation.



\---



\## FR09. Data Visualization



The system should provide basic visualizations of the dataset.



Possible visualizations include:



\* Histograms

\* Scatter plots

\* Bar charts

\* Correlation matrices



The available visualizations shall depend on the structure and data types of the dataset.



\---



\## FR10. Dataset Export



The system should allow the user to export the processed dataset.



The exported dataset shall contain the changes that were confirmed by the user during the cleaning process.



\---



\## FR11. Basic Machine Learning



The system could provide basic Machine Learning functionality using the processed dataset.



The user could select suitable variables and apply a basic Machine Learning model, such as Linear Regression, to make predictions.



Machine Learning functionality is considered an optional feature and is not required for the core data-cleaning workflow.



\# 9. Actors



The system has one primary actor:



\### A01. User



The User interacts with the application through the web interface.



The User can:



\* Upload a dataset

\* Review the dataset structure

\* Review detected data quality problems

\* Review statistics

\* Select and apply cleaning operations

\* Visualize the data

\* Export the cleaned dataset

\* Optionally use basic Machine Learning functionality



The User represents all target groups defined in the project, including beginner data analysts, students, small businesses and developers.



\---



\# 10. User Stories



\## US01. Upload Dataset



\*\*As a User, I want to upload a CSV dataset so that I can analyze its data quality.\*\*



\### Acceptance Criteria



\* The user can select a CSV file.

\* The system accepts the file if it is supported.

\* The system rejects unsupported or invalid files.

\* The system informs the user if the upload was unsuccessful.



\---



\## US02. View Dataset Structure



\*\*As a User, I want to see the structure of my dataset so that I can understand its basic organization.\*\*



\### Acceptance Criteria



\* The system displays the number of rows.

\* The system displays the number of columns.

\* The system displays the column names.

\* The system displays the detected data types.



\---



\## US03. Detect Missing Values



\*\*As a User, I want the system to detect missing values so that I know which parts of my dataset require attention.\*\*



\### Acceptance Criteria



\* The system detects missing values.

\* The system identifies the affected columns.

\* The system displays the number of missing values.

\* The detected problems are presented clearly to the user.



\---



\## US04. Detect Duplicate Rows



\*\*As a User, I want the system to detect duplicate rows so that I can decide whether they should be removed.\*\*



\### Acceptance Criteria



\* The system detects duplicate rows.

\* The system displays the number of duplicate rows.

\* The user can review the detected duplicates before cleaning them.



\---



\## US05. Detect Invalid or Inconsistent Data



\*\*As a User, I want the system to detect invalid or inconsistent data so that I can identify possible errors in my dataset.\*\*



\### Acceptance Criteria



\* The system analyzes the values of the dataset.

\* The system identifies defined types of invalid or inconsistent data.

\* The system informs the user about detected problems.

\* The system provides information about the affected data.



\---



\## US06. View Data Summary



\*\*As a User, I want to see basic statistics about my dataset so that I can quickly understand its characteristics.\*\*



\### Acceptance Criteria



\* The system displays basic statistical information.

\* The system provides statistics appropriate to the data type.

\* The user can identify important characteristics of the dataset.



Possible statistics include:



\* Mean

\* Median

\* Minimum

\* Maximum

\* Standard deviation

\* Number of values

\* Number of missing values



\---



\## US07. Choose a Cleaning Operation



\*\*As a User, I want to choose how detected problems should be handled so that I remain in control of the cleaning process.\*\*



\### Acceptance Criteria



\* The system displays available cleaning options.

\* The available options depend on the detected problem.

\* The user can select a cleaning operation.

\* The system does not modify the dataset without user confirmation.



\---



\## US08. Apply Data Cleaning



\*\*As a User, I want to apply my selected cleaning operations so that I can create a cleaner dataset.\*\*



\### Acceptance Criteria



\* The user can confirm a selected cleaning operation.

\* The system applies the selected operation.

\* The system updates the dataset.

\* The system can provide information about the performed changes.



\---



\## US09. Visualize Data



\*\*As a User, I want to visualize my dataset so that I can better understand relationships and distributions in the data.\*\*



\### Acceptance Criteria



\* The system provides suitable visualization options.

\* The system generates visualizations based on the selected data.

\* The system does not offer incompatible visualizations for unsuitable data.



Possible visualizations include:



\* Histogram

\* Scatter plot

\* Bar chart

\* Correlation matrix



\---



\## US10. Export Dataset



\*\*As a User, I want to export my processed dataset so that I can use it in another application.\*\*



\### Acceptance Criteria



\* The user can export the processed dataset.

\* The exported dataset contains the confirmed cleaning changes.

\* The exported file can be opened as a supported data file.



\---



\## US11. Use Basic Machine Learning



\*\*As a User, I want to apply a basic Machine Learning model to my cleaned dataset so that I can make simple predictions.\*\*



\### Acceptance Criteria



\* The user can select a supported Machine Learning method.

\* The user can select the relevant variables.

\* The system validates whether the selected data is suitable for the model.

\* The system trains the model.

\* The system presents the prediction or result to the user.



The initial implementation may support Linear Regression.



\## Flow



&#x20;                        ┌───────────────────────┐

&#x20;                        │        USER           │

&#x20;                        └───────────┬───────────┘

&#x20;                                    │

&#x20;            ┌───────────────────────┼──────────────────────┐

&#x20;            │                       │                      │

&#x20;            ▼                       ▼                      ▼

&#x20;     Upload Dataset         Analyze Dataset        View Summary

&#x20;                                    │

&#x20;                                    ▼

&#x20;                        Detect Data Quality Problems

&#x20;                                    │

&#x20;                         ┌──────────┴──────────┐

&#x20;                         │                     │

&#x20;                         ▼                     ▼

&#x20;               Select Cleaning        View Visualization

&#x20;                    Operation

&#x20;                         │

&#x20;                         ▼

&#x20;                 Apply Cleaning

&#x20;                         │

&#x20;                         ├──────────────► Export Dataset

&#x20;                         │

&#x20;                         └──────────────► Machine Learning





\### Planned System Architecture



&#x20;                   USER

&#x20;                    │

&#x20;                    ▼

&#x20;             ┌─────────────┐

&#x20;             │    React    │

&#x20;             │  Frontend   │

&#x20;             └──────┬──────┘

&#x20;                    │

&#x20;                 REST API

&#x20;                    │

&#x20;                    ▼

&#x20;             ┌─────────────┐

&#x20;             │   FastAPI   │

&#x20;             │   Python    │

&#x20;             └──────┬──────┘

&#x20;                    │

&#x20;         ┌──────────┼──────────┐

&#x20;         ▼          ▼          ▼

&#x20;     ┌────────┐ ┌───────┐ ┌──────────┐

&#x20;     │ Pandas │ │  ML   │ │PostgreSQL│

&#x20;     │        │ │       │ │ Metadata │

&#x20;     └────┬───┘ └───────┘ └──────────┘

&#x20;          │

&#x20;          ▼

&#x20;     ┌─────────────┐

&#x20;     │ CSV Storage │

&#x20;     │             │

&#x20;     │ original/   │

&#x20;     │ processed/  │

&#x20;     └─────────────┘





