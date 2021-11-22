*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jukka  password123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  pazsword123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ju  password123
    Output Should Contain  Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Input Credentials  jukka  pass
    Output Should Contain  Password must be at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  jukka  passpasska
    Output Should Contain  Password must also contain characters other than letters



*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input New Command
