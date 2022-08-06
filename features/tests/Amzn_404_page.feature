# Created by sbt at 8/5/22
Feature: Test Case for Amazon 404 page
  # Enter feature description here

  Scenario: User is able to navigate to blog from the 404 page
    Given Open Amazon Product B087GDYLS232454311 page
    And Store Original Window
    When Click on the Dog Image
    And Switch to New Window
    Then Verify the Blog is opened
    And Close the blog
    And Return to Original Window