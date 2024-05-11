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

#    Input Text  css:input#email     770212456
#    Input Text  css:input#pass      12654898
#    Input Text  css:input.inputtext     770212456
#    Input Text  css:input.inputtext     12654898
     Input Text  css:input[data-testid='royal_email']     12654898
#     Input Text  css:[data-testid='data-testid']     12654898

