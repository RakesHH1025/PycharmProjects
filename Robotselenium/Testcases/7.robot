*** Settings ***

Library     SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  https://demo.nopcommerce.com/register

*** Test Cases ***
Test Cases
    Set Selenium Speed  1seconds
    Open Browser    ${url}  ${browser}
    Maximize Browser Window
    ${search_box}    Get WebElement    id:small-searchterms
    ${is_displayed}    Call Method    ${search_box}    is_displayed
    Log    Search Box is Displayed: ${is_displayed}

    ${is_enabled}    Call Method    ${search_box}    is_enabled
    Log To Console   Search Box is Enabled: ${is_enabled}

    ${rd_male}    Get WebElement    id:gender-male
    ${is_selected}    Call Method    ${rd_male}    is_selected
    Log To Console    Radio Button Male is Selected: ${is_selected}

    Close Browser