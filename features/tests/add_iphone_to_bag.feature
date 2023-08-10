# Created by majidtahiri at 7/23/23
Feature: Add an iPhone to the shopping bag on Apple's website

  Scenario: User can choose an iPhone model and add it to shopping bag
    Given the user is on Apple's homepage
    When the user clicks the 'iPhone' link
    And clicks the 'Shop iPhone' link
    And select an iPhone model
    And the user selects iphone 14
    And select iphone color
    And select iphone storage
    And select 'No trade-in'
    And select payment option
    And choose a carrier
    And choose a coverage
    And add iPhone to cart
    Then review bag