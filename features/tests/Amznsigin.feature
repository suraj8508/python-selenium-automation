# Created by sbt at 7/15/22
Feature: Test Scenario for the Amazon SignIn
  # User select Order and Sign In page Opens Up

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click on Order button
    Then Varify Sign In page opened
#    Then User see email field

 Scenario: Open Sign In Page from Sign In popup
   Given Open Amazon Page
   When Click on the Sign In pop up
   Then Varify Sign In page opened


 Scenario: Users can see the Amazon Sign in Button
   Given Open Amazon Page
   Then Verify Sign In Clickable
   When Wait for 8 Sec
#   Then Verify Sign In Clickable
   Then Sign In disappears


