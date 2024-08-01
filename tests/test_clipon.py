
from pbpastesrc.clipcon import get_clipboard_content_tkinter 
from unittest.mock import patch

def test_get_clipboard_content_tkinter():
    # Mock the clipboard content
    mock_clipboard_content = "Test clipboard content"

    with patch('tkinter.Tk') as MockTk:
        # Set up the mock instance and its return values
        mock_instance = MockTk.return_value
        mock_instance.clipboard_get.return_value = mock_clipboard_content

        # Call the function
        get_clipboard_content_tkinter()

        # Assertions
        mock_instance.withdraw.assert_called_once()
        mock_instance.clipboard_get.assert_called_once()
        mock_instance.destroy.assert_called_once()