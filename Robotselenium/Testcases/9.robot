*** Settings ***

Library     SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  https://demo.nopcommerce.com/


*** Test Cases ***
Test Cases
    Set Selenium Speed  1seconds
    Open Browser    ${url}  ${browser}
    Maximize Browser Window

    Go To    https://www.snapdeal.com
    Sleep    1s

    Maximize Browser Window

    Go To    http://www.amazon.com
    Sleep    1s

    Go Back
    Sleep    1s

    Go Forward
    Sleep    1s

    Refresh Page
    Sleep    1s

    Close Browser
