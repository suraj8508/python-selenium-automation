# Created by sbt at 7/21/22
Feature: Test Scenario for the Amazon Cart
  # Cart verification

  Scenario Outline: User can Search any Products
    Given Open Amazon Page
    When Search for <product> on amazon
    Then User sees the <search_result>
    Examples:
      | product   | search_result  |
      | mug         |  "mug"              |
      | coffee      |  "coffee"          |
      | laptop      |   "laptop"         |
      | pencil       |  "pencil"          |



  Scenario Outline: User can search product and add to Cart
  """ Always showing the below error message at the first run and second run onwards test run will be failing at different steps each time.
  error message(1st time): selenium.common.exceptions.WebDriverException: Message: unknown error: cannot determine loading status
from unknown error: unexpected command response
  (Session info: chrome=103.0.5060.134)"""
    Given Open Amazon Page
    When Search for <product> on amazon
    And Click on the first product
    And Store product name
    And Click on add to Cart button
    And Open the Cart page
    Then  Verify Cart has 1 item(s)
    And Verify cart has correct product
    Examples:
    | product     |
    | laptop        |
    | bag             |
    | coffee        |
    | pencil        |


  Scenario: Verify Hamburger Menu is visible to Users
    Given Open Amazon Page
    Then Verify Hamburger Menu displayed

  Scenario: Verify all Amazon Footer Links
    Given Open Amazon Page
    Then Verify 38 footer links