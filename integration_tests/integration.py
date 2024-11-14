import requests

def test_add_and_multiply():
    # Test the addition service
    add_response = requests.post("http://add_service:5000/add", json={"a": 2, "b": 3})
    add_result = add_response.json()["result"]
    assert add_result == 5, f"Expected 5, got {add_result}"

    # Test the multiplication service with the result of addition
    multiply_response = requests.post("http://multiply_service:5001/multiply", json={"a": add_result, "b": 4})
    multiply_result = multiply_response.json()["result"]
    assert multiply_result == 20, f"Expected 20, got {multiply_result}"

