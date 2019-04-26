from string import digits, ascii_uppercase, ascii_lowercase, ascii_letters

print digits, type(digits)  # 0123456789
print ascii_uppercase   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print ascii_lowercase   # abcdefghijklmnopqrstuvwxyz
print ascii_letters   # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

Alphabet = digits + ascii_lowercase + ascii_uppercase


def ten2any(n, b=62):
    """
    10进制转换为任意进制  -- 递归方法
    :param n:  10进制数值
    :param b:  转换为几进制
    :return:
    """
    assert b <= 62

    n, index = divmod(n, b)  # n = n // b, index = n % b
    if n > 0:
        return ten2any(n, b) + Alphabet[index]
    else:
        return Alphabet[index]

print ten2any(127, b=8)


def ten2any_2(n, b=62):
    """
    10进制转换为任意进制  -- 迭代方法
    :param n:  10进制数值
    :param b:  转换为几进制
    :return:
    """
    ret = ""
    while n > 0:
        n, index = divmod(n, b)
        ret = Alphabet[index] + ret

    return ret

print ten2any_2(127, b=8)


def any2ten(s, base=62):
    """
    任意进制转换为10进制
    :param s:  进制的数值
    :param base:  数值是几进制
    :return:
    """
    n = 0
    for i, c in enumerate(reversed(s)):
        index = Alphabet.index(c)
        n += index * pow(base, i)
    return n

print any2ten("177", base=8)
