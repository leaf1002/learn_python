def get_min_repeat_data(data_list):
    """
    获取列表中最少重复的元素 
    :param data_list: 至少一个值
    :return:
    """
    from collections import Counter
    s = Counter(data_list)
    s_len = len(s)
    s = s.most_common(s_len)
    a, b = s[s_len - 1]
    min_repeat_i = a
    return min_repeat_i
