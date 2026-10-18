from unittest.mock import Mock
from verification import VerificationService

def test_send_code():
    gateway = Mock()
    gateway.send.return_value = "SENT"
    service = VerificationService(gateway)
    assert service.send_code("0812345678") == "SENT"
