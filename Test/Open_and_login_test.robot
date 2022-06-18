*** Settings ***
Library          ../customLibrary/OctoDriodGeneric.py
Library          ../customLibrary/SideMenu.py

*** Test Cases ***
successful_login
    [Tags]   login
    [Setup]     open application   full_reset=${true}  no_reset=${false}
    login to github
    ${is_in_main_page}=     is in main page
    should be true  ${is_in_main_page}
    logout user
    ${is_in_login_page}=    is in unauthrized page
    should be true  ${is_in_login_page}
    [Teardown]  close application



