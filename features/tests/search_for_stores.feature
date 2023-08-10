# Created by macbookpro at 8/4/23
Feature: Apple Store Locator

  Scenario: Search for stores by location
    Given the user is on Apple's homepage
    When the user clicks on the Store link in the navigation
    And clicks find a store
    Then the user is redirected to the Apple Store locator page
    And the user can search for stores by location
    And the user can switch back to the original window