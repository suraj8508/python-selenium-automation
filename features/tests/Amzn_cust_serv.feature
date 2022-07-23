# Created by sbt at 7/22/22
Feature: Scenario Opening the Today's Deal Page and Verify links
  # Enter feature description here

  Scenario: Amazon Customer Service Page Verification
    Given Open Amazon Page
    When User Open Customer Service Page
    Then User Verifies 9  Links