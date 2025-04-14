Feature: User Login

  Scenario Outline: Login with invalid error message
    Given I open the login page
    When I enter username "<username>"
    When I enter password "<password>"
    When I press submit button
    Then I verify login failed error message

    Examples:
     | username        | password        |
     | tutorial        | invalid_password|
     | invalid_username| invalid_password|
     | invalid_username| tutorial        |
     | tutorial        | None            |
     | None            | tutorial        |

  Scenario Outline: Login with correct username and password
    Given I open the login page
    When I enter username "<username>"
    When I enter password "<password>"
    When I press submit button
    Then I verify login successfully message
    Then I verify login successfully title

    Examples:
    | username        | password        |
    | tutorial        | tutorial        |
    | tutorial#       | tutorial#       |

  Scenario Outline: Login with username or password having more than 32 characters
    Given I open the login page
    When I enter username "<username>"
    When I enter password "<password>"
    When I press submit button
    Then I verify login failed error message

    Examples:
    | username                           | password                          |
    | 111111122222223333334444455555666  | 111111122222223333334444455555666 |

  Scenario Outline: Login with username or password having 32 characters or below
    Given I open the login page
    When I enter username "<username>"
    When I enter password "<password>"
    When I press submit button
    Then I verify login successfully message
    Then I verify login successfully title
    Examples:
    | username                           | password                          |
    | 11111112222222333333444445555566   | 11111112222222333333444445555566  |
    | 1111111222222233333344444555556    | 1111111222222233333344444555556   |