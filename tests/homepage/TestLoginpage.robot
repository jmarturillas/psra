*** Settings ***
Library     Loginpage.py  browser=chrome
Test Setup  Run Keyword     open browser
Test Teardown  Run Keyword  close browser

*** Variables ***
${username}     jamesmart2991@gmail.com
${password}     Jamlie29!
${login_url}    https://bank.paysera.com/en/login


*** Test Cases ***


# POSITIVE TEST CASES
Validate login page with elements required present
    assert url                  url=${login_url}
    assert LOGIN header is present in the page
    assert input box for email or mobile number is present in the page
    assert "Register Now!" element is present in the page
    assert language option links are present in the page
    assert "Privacy Policy" footer link is present in the page
    assert "Service Agreements" footer link is present in the page
    assert "Recommendations for the safe usage" footer link is present in the page

Validate successful input of the valid user identifier
    input username  username=${username}
    click login
    assert username label is present in the page
    assert avatar is present in the page

Validate user identifier value is editable after successful input
    input username  username=${username}
    click login
    click edit username
    assert username is in input field   username=${username}

Validate login methods are present in the page after successfully inputted a valid user identifier
    input username  username=${username}
    click login
    assert login method container is present in the page
	assert MOBILE APP header is present in the page
	assert PASSWORD header is present in the page

Validate user credential login method contains textbox and login button
    input username  username=${username}
    click login
    click password header to select it as login method
    assert password field is present when the PASSWORD header is clicked

Validate forgot password is present in the page
    input username  username=${username}
    click login
    click password header to select it as login method
    assert forgot password link is present in the page

Validate successful login via web app
    input username  username=${username}
    click login
    #TODO :: fix this part
    click password header to select it as login method
    input password   password=${password}
    login with web app
    assert logout is present in the page
    click logout


# NEGATIVE TEST CASES
Validate error when invalid user identifier value was inputted
    input username  username=@#^%&$^@#%$
    click login
    assert error is present in the page     error_type=invalid user

Validate error when wrong password was inputted
    input username  username=${username}
    click login
    #TODO :: fix this part
    click password header to select it as login method
    input password   password=@&#%^*&@#^%&^@#$*%
    login with web app
    assert error is present in the page     error_type=wrong password




*** Keywords ***
assert input box for email or mobile number is present in the page
    assert element is present in the page   element=input box

assert "Register Now!" element is present in the page
    assert element is present in the page   element=Register Now!

assert language option links are present in the page
    assert element is present in the page   element=language option links

assert "Privacy Policy" footer link is present in the page
    assert element is present in the page   element=Privacy Policy

assert "Service Agreements" footer link is present in the page
    assert element is present in the page   element=Service Agreements

assert "Recommendations for the safe usage" footer link is present in the page
    assert element is present in the page   element=Recommendations for the safe usage

assert LOGIN header is present in the page
    assert element is present in the page   element=login label

assert username label is present in the page
    assert element is present in the page   element=username label

assert avatar is present in the page
    assert element is present in the page   element=avatar

assert username is in input field
    [Arguments]  ${username}
    assert input element contains text   element=username field      text=${username}

assert login method container is present in the page
    assert element is present in the page   element=login method

assert MOBILE APP header is present in the page
    assert element is present in the page   element=mobile app header

assert PASSWORD header is present in the page
    assert element is present in the page   element=password header

assert password field is present when the PASSWORD header is clicked
    assert element is present in the page   element=password field

assert forgot password link is present in the page
    assert element is present in the page   element=forgot password

assert logout is present in the page
    assert element is present in the page   element=logout

assert error is present in the page
    [Arguments]  ${error_type}
    assert element is present in the page   element=${error_type}
