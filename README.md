# Progression Outcome Prediction System

## 🚀 Project Overview
The Progression Outcome Prediction System is a Python-based application designed to predict academic progression outcomes for students based on their credit scores. The system allows users to input credit values across different categories and returns an outcome that indicates whether the student progresses, needs to retrieve modules, or faces exclusion. 

This application is intended for educational institutions or administrative staff who need a straightforward tool to process and analyze student progression data. It provides a simple interface for both students and staff to interact with, offers clear validation checks on data entry, and generates a visual histogram to summarize results across multiple students.

The system emphasizes accurate input validation, ease of use, and data management through persistent storage and retrieval mechanisms. It also features a graphical summary that provides a high-level overview of progression outcomes distribution.

---

## 🛠️ Key Features
### ✅ Input and Validation
- Prompts the user to enter credit values for **Pass**, **Defer**, and **Fail** categories.
- Validates:
  - **Integer inputs** (rejects invalid data types).
  - **Credit values** restricted to valid multiples: 0, 20, 40, 60, 80, 100, 120.
  - **Total credit sum** must equal 120, ensuring data integrity.

### ✅ Outcome Prediction
The system evaluates the credit distribution and categorizes students into four distinct outcomes:
1. **Progress**
2. **Progress (module trailer)**
3. **Module retriever**
4. **Exclude**

### ✅ Multi-Entry Support
- Offers staff the ability to input multiple records in a single session.
- Continues accepting data until the user chooses to exit and view the summary.

### ✅ Graphical Histogram Visualization
- Generates a histogram to visually represent the distribution of progression outcomes.
- Leverages the `graphics.py` module for rendering the graphical output.
- Displays:
  - Total number of students processed.
  - Count of each outcome type represented by colored bars.

### ✅ Data Storage & Retrieval
- Saves the progression records into a list for internal tracking.
- Exports results to a timestamped text file, preserving a permanent log.
- Reads from the file and displays the stored data for review.

---
## 🏗️ Tech Stack
| Technology  | Description                                     |
|-------------|-------------------------------------------------|
| **Python 3.x** | Core programming language for application logic, data validation, and input/output processing |
| **graphics.py** | External Python module for drawing graphical histograms |
| **datetime module** | Built-in Python module used to timestamp saved text files |
| **Command-line Interface (CLI)** | Text-based user interaction for students and staff |
