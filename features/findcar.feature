Feature: Find Car

  Scenario: List cars
    Given I am on the home page
    Then I should see a list of the most recently listed cars

  Scenario: Filter list
    Given I am on the list car form
    When I apply a make or year filter
    Then only matching car should be shown

  Scenario: Filter List - no result
    Given I am on the home page with filtered result
    When There are no match
    Then I should see a message showing "No results found for your filter"

  Scenario: Pagination
    Given I am on the home page and there are no more than 10 results
    When I click on page number
    Then I should be taken to that page and the pagination bar should reflect this
