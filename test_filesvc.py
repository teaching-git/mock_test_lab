from unittest.mock import Mock
from filesvc import FileService

def test_disk_failure():
    storage = Mock()
    storage.write.side_effect = IOError("Disk full")
    service = FileService(storage)
    assert service.save("data") == "FAILED"
