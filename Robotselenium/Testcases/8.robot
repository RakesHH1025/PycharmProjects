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
    Wait Until Page Contains Element    id=small-searchterms
    ${elements}=    Get WebElements    css: .product-item
    FOR    ${element}    IN    @{elements}
        Log    ${element.text}
    END
    Close Browser
