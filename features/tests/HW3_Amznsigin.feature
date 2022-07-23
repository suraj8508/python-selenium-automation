# Created by sbt at 7/15/22
Feature: Test Scenario for the Amazon SignIn
  # User select Order and Sign In page Opens Up

  Scenario: Amazon Sign In Page Verification
    Given Open Amazon page
    When Click on Order button
    Then User sees Sign In page
    Then User see email field



