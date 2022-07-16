# Created by sbt at 7/15/22
Feature: Test Scenario for the Amazon SignIn and Empty Cart
  # User select Order and Sign In page Opens Up

  Scenario: Amazon Sign In Page Verification
    Given Open Amazon page
    When selecting the Order Button from top right side
    Then User sees Sign In page
    Then User see email field


  Scenario: Amazon Cart Verification
    Given Open Amazon Page
    When Selecting cart from homepage
    Then User see Empty Cart page
