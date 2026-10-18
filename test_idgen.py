from unittest.mock import Mock
from idgen import IdGeneratorUser

def test_multiple_ids():
    generator = Mock()
    generator.next_id.side_effect = [1, 2, 3]
    service = IdGeneratorUser(generator)
    assert service.create_three_ids() == [1, 2, 3]
