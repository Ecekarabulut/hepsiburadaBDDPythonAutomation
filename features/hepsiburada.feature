# language: en
Feature: Hepsiburada Website Automation
  As a user, I want to perform various actions on the Hepsiburada website
  so that I can test my shopping experience

  Scenario: Home page load check
    Given the Hepsiburada home page is opened

  Scenario: Accept cookies
    Then cookies should be accepted

  Scenario: Login flow
    When the user clicks the login button
    And the user enters the username
    And the user enters the password
    And the user enters the password

    # Then the login page should be displayed (isteğe bağlı, eklenebilirss)

  



