from typing import Optional

STR_DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def int_to_str(_int: int) -> str:
    """Convert int to str not using python bifs."""
    if _int == 0:
        return "0"

    if is_negative := _int < 0:
        _int *= -1

    q, _str = 1, ""
    while q <= _int:
        digit = (_int % (10*q)) // q
        _str = f"{STR_DIGITS[digit]}{_str}"
        q *= 10
    return f"-{_str}" if is_negative else _str


def str_to_int(_str: str) -> Optional[int]:
    """Convert str to int not using python bifs."""
    if _str in ["", "-"]:
        return None

    is_negative = _str[0] == "-"

    _int = 0
    for index, char in enumerate(reversed(_str[1 if is_negative else 0:])):
        if char not in STR_DIGITS:
            return None
        _int += STR_DIGITS.index(char) * 10**index
    return -1 * _int if is_negative else _int