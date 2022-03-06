# Jobsity-QAChallenge
Automation suite challenge for evaluation purposes for Jobsity

# Requeriments to run test

* Install Python3+
* Install pip (makes installing everything else easier)
* Install allure-pytest
    * `pip3 install allure-pytest`
* Install selenium
    * `pip3 install -U selenium`
* Install chromium-chromedriver
    * `apt-get install chromium-chromedriver`

# Commands to run the tests

Run all tests:
```
python3 -m pytest testcases/
```

Run a specific test suite:
```
python3 -m pytest testcases/<testsuite>

#example:
python3 -m pytest testcases/test_contactform.py
```

Run a specific test:
```
python3 -m pytest testcases/<testsuite> -k <test_name>

#example:
python3 -m pytest testcases/test_contactform.py -k test_contact_us_order_reference_validation_for_empty_message
```

Create a summary file after running tests:
```
python3 -m pytest testcases/ --alludir <output_folder>

#example:
python3 -m pytest testcases/ --alludir ./results/
```
