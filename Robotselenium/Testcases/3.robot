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
    ${elements}     Get WebElements     //a[@class='nivo-imageLink']
    FOR   ${element}  IN  @{elements}
       ${text}=    Get Text    ${element}
       Log    ${text}
    END
    Close Browser


#    FOR   ${element}  IN  @{elements}
#        Log    ${element.text}
#    END

    Close Browser



