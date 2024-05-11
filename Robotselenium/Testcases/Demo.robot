*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Clear Input Box Test
    Open Browser  https://example.com  Chrome
    Input Text  css=input[type="text"]  Some Text
    Clear Element Text  css=input[type="text"]
    Close Browser
