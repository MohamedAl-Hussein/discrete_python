
def P(n, k, i=1):
    """
    Calculates the k-permutations of n using the equation:

    P(n,k) = Product(from i=1 to k): (n - i + 1) = n(n-1)(n-2)...(n-k+1)

    :param n: the number of elements in the set
    :param k: the size of each subset
    :param i: the position in the sequence
    :return: nPk
    """

    # we have reached the end of the sequence at i=k
    if i == k:
        return n - i + 1

    return (n - i + 1) * P(n, k, i + 1)


def C(n, k, i=1):
    """
    Calculates the k-combinations of n using the equation:

    C(n,k) = Product(from i=1 to k): (n - i + 1) / (k - i + 1) = [n/k][(n-1)/(k-1)][(n-2)/(k-2)]...[(n-k+1)/(k-k+1)]

    :param n: the number of elements in the set
    :param k: the size of each subset
    :param i: the position in the sequence
    :return: nCk
    """

    # we have reached the end of the sequence at i=k
    if i == k:
        return (n - i + 1) / (k - i + 1)

    return ((n - i + 1) / (k - i + 1)) * C(n, k, i + 1)
