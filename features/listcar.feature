Feature: List Car

  Scenario: Show the form
    Given I am on the home page
    When I click the List Car button
    Then I should be shown the form

  Scenario: List a car
    Given I am on the list car form
    When I fill the details and click submit
    Then I should be shown the thankyou page

  Scenario: Incomplete form
    Given: I am on the list car form
    When I have filled in some if the details and click submit
    Then the form should show an error and the parts of the form that are missing or incorrect should be highlighted
