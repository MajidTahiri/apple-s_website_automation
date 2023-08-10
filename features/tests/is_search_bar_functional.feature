# Created by macbookpro at 8/3/23
Feature: Search Bar Functionality Test Case

  Scenario: Verify Search Functionality
    Given the user is on Apple's homepage
    When the user clicks the search icon
    And enters 'iPhone 14' in the search bar
    Then the user is redirected to search results page
    And the search results contain 'iPhone 14'