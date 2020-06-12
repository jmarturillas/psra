<h1>Features</h1>

* The automation runs in <b>RobotFramework for Selenium in Python programming language</b>
* The test file can be seen in the `/psera/tests/loginpage/TestLoginpage.robot`
* Has own `chromedriver` and `geckodriver` versions within the repository so you won't need to install it
* This has the capability to run your `chrome` and/or `firefox` regardless of your platform (Mac, Linux or Windows) 
* This generates a report log after the execution. The log can be seen in the root directory (`/psera`)
* The report consists of 3 files : 
1. `log.html`
2. `output.xml`
3. `report.html`<br>
Note : You can either open the `log.html` or the `report.html`. They both give the result statistics. Only in different presentation format.

<h1>Requirements</h1>

* Python 3.6.2 (or any version of Python 3.6)
* pyenv (install this so the dependencies will just be stored in the virtual environment)
* Chrome version 83.* 
* Firefox version 77.* <br>
Note : Versions of the browsers are strictly required because the automation might fail to run if not met.

<h1>Installation</h1>

* Make sure the `pyenv` is properly installed.
* Create a virtual environment
1. Run `pyenv virtualenv <version of your python> <name of your virtualenv>` | e.g `pyenv virtualenv 3.6.2 psra`
2. Activate the created virtual environment : `source activate psra`
3. The name of your virtual environment should be prepended in the next line of the terminal.

* Clone the repository

1. `git clone git@github.com:jmarturillas/psra.git`
* `cd` to repository's root directory (`/psera`)
* Run `pip install -r requirements.txt`

<h1>Running the tests</h1>

<h3>As a Whole Test Suite</h3>

* `cd` to the repository's root directory
* Run `robot ./tests/homepage/TestLoginpage.robot`

<h3>Per Test Case</h3>

* Run `robot --test "<name of the test case>" ./tests/homepage/TestLoginpage.robot` (refer to the `TestLoginpage.robot` to check what are the different names of test cases – they are under the `*** Test Cases ***` header; to be specific, line 16 is a sample of a test case name : `Validate login page with elements required present`)


<h3>Note</h3>

* After the execution, there will 3 files generated related to result of the test. To see the report, open the `log.html` from the root directory of this repository to your desired browser.
* The 3 files are rewritten everytime you re-run the test.
