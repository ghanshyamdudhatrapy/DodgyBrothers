Feature: Login form

  Scenario: View Login Form
    Given I am on home page without login
    When I click the login button
    Then I should be shown the login form

  Scenario: Login successfully
    Given I am on the login form filled valid details
    When I click on login
    Then I should be redirect to home page and login button should replace with a logout button

  Scenario: Login Failure
    Given I am on the login form filled invalid details
    When I click on login
    Then I should be shown an error

