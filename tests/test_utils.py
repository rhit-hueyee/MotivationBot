import pytest
from io import StringIO

from src import get_random_message_by_username


# Function to mock reading from a CSV file
def mock_csv_read(data):
    file = StringIO(data)
    file.name = "mocked.csv"
    return file


@pytest.fixture
def mock_csv(monkeypatch):
    def mock_open(mock_data):
        def open_func(file, mode='r', newline=None):
            if "r" in mode:
                return mock_csv_read(mock_data)
            else:
                raise IOError("File not found")
        monkeypatch.setattr("builtins.open", open_func)
    return mock_open


def test_multiple_messages(mock_csv):
    csv_data = "applause7,Message1\napplause7,Message2\napplause7,Message3\n"
    mock_csv(csv_data)
    result = get_random_message_by_username('applause7', 'mocked.csv')
    assert result in ["Message1", "Message2", "Message3"]


def test_single_message(mock_csv):
    csv_data = "applause7,Message1\n"
    mock_csv(csv_data)
    result = get_random_message_by_username('applause7', 'mocked.csv')
    assert result == "Message1"


def test_no_messages_for_user(mock_csv):
    csv_data = "applause7,Message1\nbarry12,Message2\n"
    mock_csv(csv_data)
    result = get_random_message_by_username('unknownuser', 'mocked.csv')
    assert result == "No messages found for this user."


def test_no_messages_in_file(mock_csv):
    csv_data = ""
    mock_csv(csv_data)
    result = get_random_message_by_username('applause7', 'mocked.csv')
    assert result == "No messages found for this user."


def test_file_not_found():
    with pytest.raises(IOError):
        get_random_message_by_username('applause7', 'nonexistent.csv')
