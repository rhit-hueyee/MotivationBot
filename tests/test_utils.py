import pytest
from io import StringIO

from src import get_random_message_by_username, get_user_message_by_time


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


def test_message_at_specific_time(mock_csv):
    mock_data = "applause7,Test1,x\napplause7,Test2,x\napplause7,Test3s,\napplause7,Test Message,10:15\n"
    mock_csv(mock_data)  # Apply the mock with data
    actual_message = get_user_message_by_time("applause7", "10:15", "mocked.csv")
    assert actual_message == "Test Message"


def test_no_message_if_time_does_not_match(mock_csv):
    """
    Test that no message is returned if there is no match for the time.
    """
    mock_data = "applause7,Should not be found,10:14\n"
    mock_csv(mock_data)
    assert get_user_message_by_time("applause7", "10:15", "mocked.csv") is None


def test_no_message_if_user_does_not_match(mock_csv):
    """
    Test that no message is returned if there is no match for the username.
    """
    mock_data = "differentUser,Message,10:15\n"
    mock_csv(mock_data)
    assert get_user_message_by_time("applause7", "10:15", "mocked.csv") is None


def test_error_on_file_not_found(monkeypatch, mock_csv):
    """
    Test that None is returned if there is an error opening the file.
    """
    # Simulate file open error
    def mock_open(file, mode='r', newline=None):
        with pytest.raises(IOError):
            assert get_user_message_by_time("applause7", "10:15", "non_existent.csv") is None
