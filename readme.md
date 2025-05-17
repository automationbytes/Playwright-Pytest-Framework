# Pytest Page Object Model (POM) Automation Framework

A test automation framework implementing Page Object Model using Pytest and Playwright.


## Prerequisites

- Python 3.9+
- pip package manager
- Allure command-line tool (for reporting)

## Installation

1. **Clone repository**
   ```bash
   git clone https://github.com/your-username/PYTestPOM_Sep24-master.git
   cd PYTestPOM_Sep24-master

2. **Create virtual environment**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    playwright install

4. **Edit Config File**

    *Update Config/config.ini with your environment settings:*
    ```bash
   [common]
    baseURL = https://your-app-url.com
    username = testuser
    password = testpass

5. **Configure test data**

    * Add test users in test_data/test_users.csv


6. **Execution**

   *Run All Tests* 
   ```bash
   pytest TestCases/ --app-browser chrome --html=Reports/results.html --junitxml=Reports/results.xml --alluredir=allure-results
   ```
   *Common Options*

   * --app-browser: Browser selection (chrome|edge|firefox)
   
   * --app-headed: Run in visible browser mode
   
   * -n NUM: Parallel execution (e.g., -n 4 for 4 workers)
   
   **Execution Examples**
   ```bash
   # Firefox with visible browser
   pytest TestCases/ --app-browser firefox --app-headed
   
   # Specific test file with Edge
   pytest TestCases/test_demo.py --app-browser edge
   
   # Parallel execution with Chrome
   pytest TestCases/ --app-browser chrome -n 4
   ```
7. **Reporting**
   Allure Reports
```bash
   # Generate interactive report
   allure serve allure-results/
   
   # Generate HTML report
   allure generate allure-results/ -o Reports/allure-report --clean
   ```
*
   HTML Report
   Automatically generated at:
   Reports/results.html
  
8. **Logging**

   Test execution logs are maintained in:
   Logs/demo.log
