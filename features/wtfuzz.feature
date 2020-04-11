Feature: Data initialisation

  Scenario: Send basic request

    Given a configured wtfuzz
    When I send a request to a valid endpoint
    Then I expect to receive a valid http code

  Scenario: Send verb request

    Given a configured wtfuzz
    When I send a HEAD request to a valid endpoint
    Then I expect to receive a valid http code

  Scenario: Send full request

    Given a configured wtfuzz
    When I send a HEAD full request to a valid endpoint
    Then I expect to receive a full response

