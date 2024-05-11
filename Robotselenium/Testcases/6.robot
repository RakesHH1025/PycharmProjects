*** Settings ***

Library     SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  https://www.facebook.com/

*** Test Cases ***
Test Cases
    Set Selenium Speed  1seconds
    Open Browser    ${url}  ${browser}
    Maximize Browser Window
    ${title}    Get Title
    Log    ${title}
    ${url}    Get Location
    Log    ${url}
    ${source}=    Execute Javascript    return document.documentElement.outerHTML
    Log    ${source}

    Close Browser