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
#    Input Text  xpath://input[@id='small-searchterms']  Lenovo Thinkpad X1 Carbon Laptop
#    Click Element   xpath://button[normalize-space()='Search']
#    Input Text   xpath://input[@name='q' or @id='small-searchterms']    Lenovo Thinkpad X1 Carbon Laptop
#    Input Text   xpath://input[@placeholder='Search store' and @name='q']    Lenovo Thinkpad X1 Carbon Laptop
#    Input Text   xpath://input[contains(@id,'small-searchterms')]    Lenovo Thinkpad X1 Carbon Laptop
    Input Text   xpath://a[starts-with(text(), 'Search')]    Lenovo Thinkpad X1 Carbon Laptop