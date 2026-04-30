from main import add, is_valid_message

def test_add():
    assert add(2, 3) == 5

def test_valid_message():
    assert is_valid_message("hello") == True

def test_invalid_message():
    assert is_valid_message("") == False