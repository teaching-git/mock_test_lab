from unittest.mock import patch
from greetings import greeting

@patch("greetings.get_name")
def test_greeting(mock_name):
    mock_name.return_value = "Alice"
    assert greeting() == "Hello Alice"
