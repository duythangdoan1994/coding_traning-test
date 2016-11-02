
def combinations(iterable, r):
    """
    Điều kiện : Chọn ra tổ hợp (k, 107) mã mầu xuất hiện nhiều nhất

    :param iterable:
    :param r:
    :return:
    """
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    print(tuple(pool[i] for i in indices))
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        print(tuple(pool[i] for i in indices))


if __name__ == '__main__':
    combinations(('B', 'BG', 'AB'), 2)
