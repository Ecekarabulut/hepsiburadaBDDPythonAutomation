# language: en
Feature: Hepsiburada Website Automation
  As a user, I want to perform various actions on the Hepsiburada website
  so that I can test my shopping experience

  Scenario: Home page load check
    Given the Hepsiburada home page is opened

  Scenario: Accept cookies
    Then cookies should be accepted

  Scenario: Click button by xpath
    When the user clicks the button by xpath
    Then wait 3 seconds and log

  Scenario: Click add to cart button
    When the user clicks the add to cart button
    Then the product should be in the basket
    Then wait 3 seconds and log

  Scenario: Click go to cart button
    When the user clicks the go to cart button
    Then wait 3 seconds and log

  Scenario: Click selected checkbox
    When the user clicks the selected checkbox
     Then wait 3 seconds and log

  Scenario: Verify total price is zero
    Then the total price should be zero and wait 3 seconds



