def add(a, b):
    return a + b

def is_valid_message(msg):
    return isinstance(msg, str) and len(msg) > 0

if __name__ == "__main__":
    print("4 + 6 =", add(4, 6))
    print("Valid:", is_valid_message("hello"))