def add(a, b):
    return a + b

def is_valid_message(msg):
    return isinstance(msg, str) and len(msg) > 0

if __name__ == "__main__":
    print("2 + 9 =", add(2, 9))
    print("Valid:", is_valid_message("hello"))