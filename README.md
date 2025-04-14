# Python Selenium automation test
The test framework we've implemented is mainly built on Behave. 
The framework also integrates Allure reporting framework to generate descriptive test execution reports.

## Set up test environment
### Installation
The test framework is running against Python 3, please make sure you have Python 3.7 (or above) and Pip3 installed on your computer. Once you create a local copy from this repo, you can go into it and install dependent python libraries by shooting below command:

> pip install pipenv (install pipenv if it's not installed)
>
> pipenv install (--skip-lock)

You need to use allure command-line to resolve allure results and present test report in browsers, you can install it with Homebrew

> brew install allure

To develop your test cases, you may choose PyCharm(Recommended!) as your IDE

> Go to Preferences > Project Interpreter > Add > Pipenv Environment > Ok
>
> (refer https://www.jetbrains.com/help/pycharm/pipenv.html for more details)

## Run test cases
This test framework is built on Behave which supports several ways to run and select tests from the command-line.
> behave -f allure_behave.formatter:AllureFormatter -o reports/ features/

## Generate report
    
> allure generate "./reports/" -o ./allure_result/ --clean
>
> allure open allure_result