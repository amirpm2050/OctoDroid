# OctoDroid

This project is for implementing E2E and functional tests.

## Requirments
- Python
- Robot Framework
- Appium
- Android Sdk


## Configuration

- In config_variables(variables package) file we have a variable whit name appuim_host which you should set your started Appium session URL there.
- In config_variables we have another variable with name udid which you should set the cellphone udid there. To find udid enter below command :

```bash
adb devices 
```

## How to run test case 

For all test cases, we have tags. for running the test you should enter this command :
```bash
python3 -m robot --include <tag>
```
 
## Reports
After every each test runs reports will be generated in root of the project and  You can add -d switch on run command for path of reports like:
```bash
python3 -m robot -d <path> --include <tag>
```
There is three report file first one is 'report.html' which you can get all the information of test run (test name, test status, test execution time ), second one is 'log.html' which have 'report.html' information too and including the information for every each step of test case . 


