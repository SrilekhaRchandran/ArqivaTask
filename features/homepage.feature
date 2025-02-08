Feature: Arqiva website testing
  Scenario: Verify homepage and main tabs
    Given the homepage is loaded
    Then the title should be "Arqiva"
    When I navigate through the main tabs from 0 to 6
    Then I should verify all tabs load correctly
