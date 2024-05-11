*** Settings ***
Library           SeleniumLibrary


*** Test Cases ***
Example Test
    Open Browser
    Go To    https://admin-demo.nopcommerce.com/login
    Maximize Browser Window

    ${emailbox}    Get WebElements    id:Email
    Input Text    ${emailbox}[0]    abc@yourstore.com
    Sleep    5s

    ${result_text}:    Call Method    ${emailbox}[0]    get_attribute    value
    Log    result of get_attribute(): ${result_text}

    Close Browser
