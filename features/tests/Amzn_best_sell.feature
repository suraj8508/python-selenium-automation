# Created by sbt at 7/21/22
Feature: Scenario Opening the Best Sellers Page and Verify Header links
  # Enter feature description here

  Scenario: Amazon Best Sellers Page Verification
    Given Open Amazon Page
    When User Select Best Sellers
    Then User Verifies 5  Links