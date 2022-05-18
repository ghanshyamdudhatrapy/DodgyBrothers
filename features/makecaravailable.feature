Feature: Make car available

  Scenario: Make available
    Given I am on the home page with sold car and logged in
    When I click "Make available"
    Then the car should appear as available for sale again

  Scenario: Not logged in cant make available
    Given I am on the home page with sold car and not logged in
    Then there should not be a make available button

  Scenario: available cars dont have button
    Given I am on the home page with unsold car and logged in
    Then there should not be a make available button
