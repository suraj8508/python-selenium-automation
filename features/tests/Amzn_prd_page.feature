# Created by sbt at 7/29/22
Feature: Testing the Iteration over the products list
  # Enter feature description here

  Scenario Outline: User Can select different Colors
    Given Open Amazon Product <Amzn_Prd_ID> page
    Then Verify User can Click over the Colors
    Examples:
    |   Amzn_Prd_ID      |
    |   B07QH1QH34      |
    |   B07BJKRR25       |
    |   B081YS2F7N       |

 Scenario: User Can select different Colors
    Given Open Amazon Product B07BJKRR25 page
    Then Verify User can Click over the Colors


 Scenario: User Can select different Colors
    Given Open Amazon Product B081YS2F7N page
    Then Verify User can Click over the Colors