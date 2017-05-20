Feature: Group feature
  Description

  Scenario Outline: Add new group
    Given a group list
    Given a group with <name>, <header>, <footer>
    When I add a new group  to the list
    Then a new group list is equal to the old list with the new group

    Examples:
    | name | header | footer |
    | as dfr |gjh | ihyu |
    | рпрп | клурге | коао7 |
    | 67| dkuhf| jdvj5р|

