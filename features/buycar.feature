Feature: Buy Car

  Scenario: Buy car button
    Given I am on the home page
    When I click the buy button next to a listing
    Then I should be taken to the buy form

  Scenario: Complete buy form
    Given I am on the buy form filled with valid details
    When I click buy
    Then I should be redirect to a thankyou page and car should mark as sold

  Scenario: Sold car
    Given a car has been sold
    When I visit the listing page
    Then the car should be marked as sold and there should be no "BUY" button next to the car

  Scenario: Email Iron Mike
    Given I am on the buy form filled with valid details
    When I click buy
    Then mike@example.org should receive an email

