# Created by sbt at 8/19/22
Feature: This Feature file only to test the dynamic locator
  # Enter feature description here

  Scenario: User select Computers dept and search Laptop
    Given Open Amazon Page
    When Select the Dept by alias computers
    And Search for Laptop
    Then Verify the pc Dept selected


    """
    In the result page it is showing as Computers ,
    but in the DOM under Select segment the data category is mentioned as "pc".
    When I inserted in Computers in the verification step the verification step was failing
    so when i changed to "pc" it worked.
    """

