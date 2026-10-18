from unittest.mock import Mock
from login import LoginService

def test_login_logs_message():
    logger = Mock()
    service = LoginService(logger)
    service.login("Alice")
    logger.info.assert_called_once_with("Alice logged in")
