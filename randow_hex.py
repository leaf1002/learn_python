def get_random_hex():
    """
    获取0-65535之间随机一个16进制字符串

    :return:
    """
    ran_num = random.randint(1, 50000)
    ran_hex_num = hex(ran_num)
    ran_hex_str = ran_hex_num[2:]
    if len(ran_hex_str) < 4:
        index = (4 - len(ran_hex_str)) * "0"
        ran_hex_str = index + ran_hex_str
    return ran_hex_str.upper()


def get_channel_random_hex():
    """
    获取1-31之间随机一个16进制字符串

    :return:
    """
    ran_num = random.randint(1, 31)
    ran_hex_num = hex(ran_num)
    ran_hex_str = ran_hex_num[2:]
    if len(ran_hex_str) < 2:
        index = (2 - len(ran_hex_str)) * "0"
        ran_hex_str = index + ran_hex_str
    return ran_hex_str.upper()
