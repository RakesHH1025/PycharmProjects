*** Settings ***

Library  SeleniumLibrary
Library     SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://admin-demo.nopcommerce.com/login
${exp_title}    Admin area demo
${actual_title}    ${EMPTY}

*** Test Cases ***
Test Cases
    Set Selenium Speed  1seconds
    Open Browser    ${url}  ${browser}
    Maximize Browser Window
    Input Text  name:Email      admin@yourstore.com
    Input Text  id:Password     admin


    Click Element   xpath://button[normalize-space()='Log in']
    ${actual_title}=    Get Title
    Run Keyword If    '${actual_title}' == '${exp_title}'    Log    Test case passed    ELSE    Log    Test case failed

*** Keywords ***
