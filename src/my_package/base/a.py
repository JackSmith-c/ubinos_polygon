class TestClassA:
    """
    테스트 클래스 A
    """

    def __init__(self):
        """
        테스트 클래스 A 초기화
        """
        pass

    def test_method_1(self, name):
        """
        테스트 메서드 1
        - name: 이름
        """
        print(f"Hello, {name}!")


def example_function(param1, param2):
    """This is a function example with Google style docstrings.

    The main description of the function is written here and provides
    a brief overview of what the function does.

    Args:
        param1 (int): The first parameter used for ...
        param2 (str): The second parameter used for ...

    Returns:
        bool: True if successful, False otherwise.

    Raises:
        TypeError: If `param1` is not an integer.
        ValueError: If `param2` is an empty string.

    Notes:
        This is an additional note or a set of notes that provide extra
        information about the function, but are not part of the main description.

    Examples:
        >>> example_function(5, "hello")
        True
        >>> example_function(10, "")
        ValueError: param2 should not be an empty string.
    """
    if not isinstance(param1, int):
        raise TypeError("param1 should be of type int")
    if not param2:
        raise ValueError("param2 should not be an empty string")

    # Function's logic here
    return True