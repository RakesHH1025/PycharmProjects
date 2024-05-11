*** Settings ***

Library     SeleniumLibrary
Library     SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.nopcommerce.com/

*** Test Cases ***
Test Cases
    Set Selenium Speed  1seconds
    Open Browser    ${url}  ${browser}
    Maximize Browser Window
#    Input Text  name:q  Lenovo Thinkpad X1 Carbon Laptop
#    Input Text  id:small-searchterms    Lenovo Thinkpad X1 Carbon Laptop
#    Input Text  id:small-searchterms    Lenovo Thinkpad X1 Carbon Laptop
#    Click Element   class:button-1

#    Click Element   Link:Register
    Click Element   Partiallink:Reg