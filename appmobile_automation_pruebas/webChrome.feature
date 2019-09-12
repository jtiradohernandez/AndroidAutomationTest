@android

Feature: UI Automatione exercies

  @Importante
  Scenario: Add a product on the basket correctly
    Given Go to Zatro.es
    And Click the search button
    And Search for "adidas"
    And Click the item "2"
    And Select the second available shoe size
    And Add it to the shopping cart
    And Click Tramitar Pedido
    When Click on Mi Cesta
    Then the "1" item on the basket is the same as you clicked