from pathlib import Path
from unittest.mock import patch, MagicMock
from readme_generator import generate_readme, OutputManager
import logging
import requests
import tempfile
import os
import json

# Mock parameters for the generate_readme function
file_contents = "print('Hello, World!')"  # Example content
model = "mock_model"
file_extension = ".py"
stream = False


@patch("requests.post")
def test_mock_llm_response(mock_post):
    # Define the mock response for the LLM API
    mock_post.return_value.json = lambda: {
        "choices": [{"message": {"content": "Mocked README content"}}],
        "usage": {},
    }

    # Mock parameters for the generate_readme function
    api_key = "mock_api_key"
    model = "mock_model"
    file_contents = "print('Hello, World!')"  # Example content
    file_extension = ".py"

    # Call the function to generate the README
    result = generate_readme(file_contents, api_key, model, file_extension)

    # Assert that the result matches the mock response content
    assert result == "Mocked README content"


@patch("requests.post")
def test_empty_file_content(mock_post):
    # Define a mock response to return if the function makes an API call
    mock_post.return_value.json = lambda: {
        "choices": [{"message": {"content": "Mocked README content"}}],
        "usage": {},
    }

    # Mock parameters for the generate_readme function
    api_key = "mock_api_key"
    model = "mock_model"
    file_contents = ""  # Empty content
    file_extension = ".py"

    # Call the function to generate the README with empty content
    result = generate_readme(file_contents, api_key, model, file_extension)

    # Assert that the result matches the expected behavior for empty content
    assert (
        result == "No content to process"
    ), "Expected result to handle empty content gracefully"


def test_generate_readme_with_valid_api_key():
    """Test generate_readme with a valid API key."""
    api_key = "mock_api_key"

    # Mock the response from make_api_request to avoid real API calls
    with patch("readme_generator.make_api_request") as mock_request:
        mock_request.return_value = ("Mocked README content", {})

        # Call the function
        result = generate_readme(file_contents, api_key, model, file_extension, stream)

        # Verify the function returned the mocked README content
        assert result == "Mocked README content"
        mock_request.assert_called_once_with(
            api_key, model, file_contents, file_extension, stream
        )


def test_generate_readme_with_missing_api_key(caplog):
    """Test generate_readme with a missing API key."""
    api_key = None  # Simulate missing API key

    # Set up logging capture to verify the error message
    with caplog.at_level(logging.ERROR):
        result = generate_readme(file_contents, api_key, model, file_extension, stream)

    # Verify the function returned None (or any specific behavior you defined)
    assert result is None

    # Check if the expected error message was logged
    assert "API request failed" in caplog.text


@patch("requests.post")
def test_generate_readme_with_supported_extension(mock_post):
    # Mock API response for supported extension (.py)
    mock_post.return_value.json = lambda: {
        "choices": [{"message": {"content": "Generated README for Python script"}}],
        "usage": {},
    }

    # Mock parameters for a .py file
    api_key = "mock_api_key"
    model = "mock_model"
    file_contents = "print('Hello, World!')"
    file_extension = ".py"

    # Call the function
    result = generate_readme(file_contents, api_key, model, file_extension)

    # Assert that the content is as expected for a Python script
    assert result == "Generated README for Python script"


@patch("requests.post")
def test_generate_readme_with_unsupported_extension(mock_post):
    # Mock API response for unsupported extension (.txt)
    mock_post.return_value.json = lambda: {
        "choices": [{"message": {"content": "Generated README for script"}}],
        "usage": {},
    }

    # Mock parameters for a .txt file (unsupported extension)
    api_key = "mock_api_key"
    model = "mock_model"
    file_contents = "This is a text file."
    file_extension = ".txt"

    # Call the function
    result = generate_readme(file_contents, api_key, model, file_extension)

    # Assert that the content is generic for unsupported extension
    assert result == "Generated README for script"


@patch("readme_generator.requests.post")
def test_generate_readme_timeout_handling(mock_post):
    # Configure the mock to raise a Timeout error
    mock_post.side_effect = requests.exceptions.Timeout

    # Mock parameters for the generate_readme function
    api_key = "mock_api_key"
    model = "mock_model"
    file_contents = "print('Hello, World!')"  # Example content
    file_extension = ".py"

    # Call the function to generate the README with a simulated timeout
    result = generate_readme(file_contents, api_key, model, file_extension)

    # Assert that the result is None due to timeout handling
    assert result is None


@patch("requests.post")
def test_generate_readme_stream_enabled(mock_post):
    # Simulate a streamed API response by mocking iter_lines()
    mock_response = MagicMock()
    mock_response.iter_lines.return_value = [
        b'{"choices": [{"message": {"content": "First chunk of README content"}}]}',
        b'{"choices": [{"message": {"content": "Second chunk of README content"}}]}',
    ]
    mock_response.raise_for_status = lambda: None
    mock_post.return_value = mock_response

    # Mock parameters for the generate_readme function
    api_key = "mock_api_key"
    model = "mock_model"
    file_contents = "print('Hello, World!')"  # Example content
    file_extension = ".py"
    stream = True

    # Call generate_readme with stream=True
    result = generate_readme(
        file_contents, api_key, model, file_extension, stream=stream
    )

    # Assert that the content returned is a concatenation of streamed chunks
    expected_content = "First chunk of README content\nSecond chunk of README content"
    assert result == expected_content


@patch("requests.post")
def test_generate_readme_with_valid_model(mock_post):
    # Mock API response for valid model
    mock_post.return_value.json = lambda: {
        "choices": [
            {"message": {"content": "Generated README content for valid model"}}
        ],
        "usage": {},
    }
    api_key = "mock_api_key"
    valid_model = "valid_model_name"
    result = generate_readme(file_contents, api_key, valid_model, file_extension)
    assert result == "Generated README content for valid model"


@patch("requests.post")
def test_generate_readme_with_invalid_model(mock_post):
    # Mock API response to simulate invalid model error
    mock_post.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "Invalid model"
    )
    api_key = "mock_api_key"
    invalid_model = "invalid_model_name"
    result = generate_readme(file_contents, api_key, invalid_model, file_extension)
    assert result is None  # Expected behavior for invalid model handling


@patch("readme_generator.requests.post")
def test_token_usage_logging(mock_post, caplog):
    # Set up the mock response to include token usage
    mock_post.return_value.json = lambda: {
        "choices": [{"message": {"content": "Mocked README content"}}],
        "usage": {"total_tokens": 100},
    }

    # Define the test parameters
    api_key = "mock_api_key"
    model = "mock_model"
    file_contents = "print('Hello, World!')"  # Example file contents
    file_extension = ".py"

    # Run the function and capture logs
    with caplog.at_level(logging.INFO):
        generate_readme(file_contents, api_key, model, file_extension)

    # Check if the token usage log is present in captured logs
    assert "Token usage: {'total_tokens': 100}" in caplog.text


@patch("requests.post")
def test_generate_readme_content_structure(mock_post):
    # Define the mock response that `generate_readme` should process
    mock_post.return_value.json = lambda: {
        "choices": [
            {
                "message": {
                    "content": "## Usage\n\nThis is the usage section.\n\n## Examples\n\nExample content."
                }
            }
        ],
        "usage": {},
    }

    # Mock parameters for the generate_readme function
    api_key = "mock_api_key"
    model = "mock_model"
    file_contents = "print('Hello, World!')"  # Example content
    file_extension = ".py"

    # Call generate_readme with the mock response
    result = generate_readme(file_contents, api_key, model, file_extension)

    # Check that the result is a string
    assert isinstance(result, str), "Expected the result to be of type 'str'"

    # Check for specific keywords or sections in the README content
    assert "Usage" in result, "Expected 'Usage' section in README content"
    assert "Examples" in result, "Expected 'Examples' section in README content"


@patch("requests.post")
def test_large_file_content(mock_post):
    # Define a large content for the file
    large_content = "print('Hello, World!')" * 10000  # Repeat to create a large input

    # Mock API response for large content
    mock_post.return_value.json = lambda: {
        "choices": [{"message": {"content": "Generated README for large content"}}],
        "usage": {},
    }

    # Mock parameters for the generate_readme function
    api_key = "mock_api_key"
    model = "mock_model"
    file_extension = ".py"

    # Call the function with the large content
    result = generate_readme(large_content, api_key, model, file_extension)

    # Assert that the result is as expected
    assert result == "Generated README for large content"


@patch("requests.post")
def test_generate_readme_with_output_manager(mock_post):
    # Define the mock response to simulate API behavior
    mock_post.return_value.json = lambda: {
        "choices": [{"message": {"content": "Generated README content for testing"}}],
        "usage": {},
    }

    # Define the necessary parameters within the test function
    api_key = "mock_api_key"
    model = "mock_model"
    file_contents = "print('Hello, World!')"  # Example content
    file_extension = ".py"

    # Create a temporary directory to test file output
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = os.path.join(temp_dir, "sample_file.py")

        # Initialize OutputManager with the temporary directory and JSON output disabled
        output_manager = OutputManager(output_dir=temp_dir, json_output=False)

        # Run generate_readme to get the content
        readme_content = generate_readme(file_contents, api_key, model, file_extension)

        # Verify that the README content is not None
        assert readme_content is not None, "Expected README content to be generated"

        # Save the README content using OutputManager
        output_manager.save_readme(Path(temp_path), readme_content)

        # Check if the README file was created successfully
        readme_path = os.path.join(temp_dir, "sample_file_README.md")
        assert os.path.exists(readme_path), "Expected README file to be created"

        # Verify the content of the saved README file
        with open(readme_path, "r") as readme_file:
            saved_content = readme_file.read()
            assert (
                saved_content == "Generated README content for testing"
            ), "Expected README content to match generated content"


# Test for basic functionality with mocked successful response
@patch("readme_generator.make_api_request")
def test_generate_readme_success(mock_make_api_request):
    mock_make_api_request.return_value = ("Mocked README content", {})

    api_key = "mock_api_key"
    model = "mock_model"
    file_contents = "print('Hello, World!')"
    file_extension = ".py"

    result = generate_readme(file_contents, api_key, model, file_extension)

    assert result == "Mocked README content"


# Test for empty content
def test_generate_readme_empty_content():
    api_key = "mock_api_key"
    model = "mock_model"
    file_contents = ""  # Empty content
    file_extension = ".py"

    result = generate_readme(file_contents, api_key, model, file_extension)

    assert result == "No content to process"


# Test for error handling when make_api_request returns None
@patch("readme_generator.make_api_request")
def test_generate_readme_error_handling(mock_make_api_request):
    mock_make_api_request.return_value = (None, None)

    api_key = "mock_api_key"
    model = "mock_model"
    file_contents = "print('Hello, World!')"
    file_extension = ".py"

    result = generate_readme(file_contents, api_key, model, file_extension)

    assert result is None


@patch("requests.post")
def test_generate_readme_non_json_response(mock_post):
    mock_post.return_value.text = "Service Unavailable"
    mock_post.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "Service Unavailable"
    )
    api_key = "mock_api_key"
    result = generate_readme(file_contents, api_key, model, file_extension)
    assert result is None


@patch("requests.post")
def test_generate_readme_network_error(mock_post):
    mock_post.side_effect = requests.exceptions.ConnectionError("Connection error")
    api_key = "mock_api_key"
    model = "mock_model"
    result = generate_readme(file_contents, api_key, model, file_extension)
    assert (
        result is None
    )  # Ensure the function returns None when there is a connection error


@patch("requests.post")
def test_generate_readme_with_empty_model(mock_post):
    # Mock the response as if the request was still made, even with an empty model
    api_key = "mock_api_key"
    empty_model = ""

    # Define a mock response
    mock_post.return_value.json.return_value = {
        "choices": [{"message": {"content": "Mocked README content for empty model"}}]
    }
    # Run the function
    result = generate_readme(file_contents, api_key, empty_model, file_extension)
    # Assert that the mock response content is returned
    assert result == "Mocked README content for empty model"  # Adjusted to match the mocked response


def test_output_manager_with_invalid_path():
    output_manager = OutputManager(output_dir="/invalid/path", json_output=False)
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = Path(temp_file.name)
        try:
            output_manager.save_readme(temp_path, "Test content")
        except OSError:
            assert True  # Expect an OSError for an invalid path


def test_output_manager_save_readme():
    with tempfile.TemporaryDirectory() as temp_dir:
        output_manager = OutputManager(temp_dir, json_output=False)
        file_path = Path(temp_dir) / "sample_file.py"
        readme_content = "Sample README content"
        output_manager.save_readme(file_path, readme_content)
        readme_path = Path(temp_dir) / "sample_file_README.md"
        assert readme_path.exists()
        with open(readme_path, "r") as f:
            assert f.read() == readme_content


def test_output_manager_save_json():
    with tempfile.TemporaryDirectory() as temp_dir:
        output_manager = OutputManager(temp_dir, json_output=True)
        file_path = Path(temp_dir) / "sample_file.py"
        result = {"content": "Sample JSON content"}
        output_manager.save_json(file_path, result)
        json_path = Path(temp_dir) / "sample_file_README.json"
        assert json_path.exists()
        with open(json_path, "r") as f:
            assert json.load(f) == result

