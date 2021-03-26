import sys


def decimal_to_base(dec_num, base):
    if dec_num == 0:
        return [0]
    new_base_num = list()
    while dec_num > 0:
        dec_num, remainder = divmod(dec_num, base)
        new_base_num.append(remainder)
    return new_base_num[::-1]


def decimal_to_bin(dec_num):
    bin_list = [str(num) for num in decimal_to_base(dec_num, 2)]
    bin_num = "0b" + "".join(bin_list)
    return bin_num


HEX_CHAR_LIST = [*[str(num) for num in range(0, 10)], "a", "b", "c", "d", "e", "f"]


def decimal_to_hex(dec_num):
    hex_list = [HEX_CHAR_LIST[num] for num in decimal_to_base(dec_num, 16)]
    hex_num = "0x" + "".join(hex_list)
    return hex_num
