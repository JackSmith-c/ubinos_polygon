class TestClassB:
    """
    테스트 클래스 B
    """

    def __init__(self):
        """
        테스트 클래스 B 초기화
        """
        pass

    def test_method_2(self, age):
        """
        테스트 메서드 1
        - age: 나이
        """
        print(f"I'm {age} years old.!")


def sum(arg1, arg2):
    """
    This is sum function.

    Args:
        arg1 (int): Description of arg1.
        arg2 (int): Description of arg2.

    Returns:
        int: Description of return value

    Examples:
        >>> a=1
        >>> b=2
        >>> sum(a, b)
        3
    """
    return arg1 + arg2
        