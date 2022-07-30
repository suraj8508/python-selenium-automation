# Created by sbt at 7/15/22
Feature: Test Scenario for the Amazon SignIn
  # User select Order and Sign In page Opens Up

  Scenario: Amazon Sign In Page Verification
    Given Open Amazon page
    When Click on Order button
    Then Varify Sign In page opened
    Then User see email field

 Scenario: Open Sign In Page from Sign In popup
   Given Open Amazon Page
   When Click on the Sign In pop up
   Then Varify Sign In page opened



