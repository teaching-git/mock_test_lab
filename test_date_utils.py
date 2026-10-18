from unittest.mock import patch
from date_utils import report_name

def test_report_name():
    with patch("date_utils.current_year") as mock_year:
        mock_year.return_value = 2030
        assert report_name() == "Report-2030"
