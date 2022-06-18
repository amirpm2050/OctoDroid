*** Settings ***
Library          ../customLibrary/OctoDriodGeneric.py
Library          ../customLibrary/Issue.py
Library          ../customLibrary/SideMenu.py
Library          ../customLibrary/Search.py

*** Test Cases ***
create_issue_and_close
    [Tags]    createIssue
    [Setup]     open application
    check user is loged in
    ${is_in_main_page}=     is in main page
    should be true  ${is_in_main_page}
    open search menu
    search project and open     project_name=cafebazaar/AdContainer
    click on issue in project
    open new issue page
    add issue from search     title=issueForTest1    desc=description for test2
    ${is_issue_added}=    is issue added
    should be true  ${is_issue_added}
    close issue
    ${is_issue_closed}=    check issue is close
    should be true    ${is_issue_closed}
    [Teardown]  close application

add comment to issue
    [Tags]    updateIssue
    [Setup]     open application
    check user is loged in
    ${is_in_main_page}=     is in main page
    should be true  ${is_in_main_page}
    open search menu
    search project and open     project_name=cafebazaar/AdContainer
    click on issue in project
    scroll to find issue    This project seems to be outdated
    add_comment_to_issue    this comment is for test
    ${check}=   check comment added     this comment is for test
    should not be true    ${check}
    [Teardown]  close application



