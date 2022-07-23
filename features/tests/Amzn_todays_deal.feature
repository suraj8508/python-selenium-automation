# Created by sbt at 7/22/22
Feature: Scenario Opening the Today's Deal Page and Verify links
  # Enter feature description here

  Scenario: Amazon Best Sellers Page Verification
    Given Open Amazon Page
    When User Select Today's Deal
    Then User Verifies 6  Links