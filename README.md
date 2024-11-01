## DecentraLab QA Home Assignment

## QA Home Assignment Overview

This home assignment is part of the recruitment process for the position of QA Automation Engineer in DecentraLab.
The home assignment is comprised of manual and automation tasks, and it took 6 hours to complete. The manual task of
creating a test suit was created within an Excel sheet, and the remaining tasks were written on a task file. The
automation tasks were built in Python using Selenium and the Pytest framework, alongside fixtures from a conftest file.
Reports of the runs were built using the Allure reports framework. The automation tasks (task number 2 and bonus task)
were built using the page object model design in an infrastructure structure.

## Test Execution

**Allure Reports**: Generates detailed and interactive reports, providing insights into test results and facilitating
debugging failures.

### How to Run Tests

To execute the tests through the terminal using Allure commands:

**Run tests:**

pytest -s -v test_cases/test_hord.py --alluredir=./allure-results

pytest -s -v test_cases/test_revenue_share.py --alluredir=./allure-results

**Generate reports:**

allure serve allure-results
