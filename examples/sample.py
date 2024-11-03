# file1.py


def greet(name):
    """
    This function prints a greeting message to the user.
    :param name: Name of the user
    """
    return f"Hello, {name}! Welcome to the project."


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
