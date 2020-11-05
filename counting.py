
def P(n, k, i=1):
    """
    Calculates the k-permutations of n using the equation:

    P(n,k) = Product(from i=1 to k): (n - i + 1) = n(n-1)(n-2)...(n-k+1)

    :param n: the number of elements in the set
    :param k: the size of each subset
    :param i: the position in the sequence
    :return: nPk
    """

    # P(n,0) = 1
    if k == 0:
        return 1

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

    # C(n,0) = 1
    if k == 0:
        return 1

    # we have reached the end of the sequence at i=k
    if i == k:
        return (n - i + 1) / (k - i + 1)

    return ((n - i + 1) / (k - i + 1)) * C(n, k, i + 1)


def binomial(x, y, n, k=0):
    """
    Calculates the binomial (x + y)^n using the binomial theorem:

    (x + y)^n = Sum(from k=0 to n): C(n,k)*(x^(n-k))*(y^k) = C(n,0)*(x^n) + C(n,1)*(x^(n-1))*y + ... + C(n,n)*(y^n)

    :param x: the first value in the binomial
    :param y: the second value in the binomial
    :param n: a nonnegative integer representing the power of the binomial
    :param k: the position in the sequence
    :return: the result of the binomial
    """

    # we have reached the end of the sequence at k=n
    if k == n:
        return C(n, k) * (x ** (n - k)) * (y ** k)

    return binomial(x, y, n, k + 1) + (C(n, k) * (x ** (n - k)) * (y ** k))


def pascals_triangle(depth):
    """
    Draws Pascal's Triangle at a given depth.

    :param depth: an integer value representing the depth of the triangle
    :return: None
    """

    # set the counter to the depth as we will be starting from the base of the triangle
    i = depth

    # create a new empty triangle
    triangle = ''

    # set the bottom row width to 0; we will use this value to center subsequent rows
    bottom_row_width = 0

    # iterate through each row until we reach the top of the triangle
    while i >= 0:
        # create a new empty row
        row = ''

        # calculate the binomial values for the current depth and append to the row
        for j in range(0, i + 1):
            value = f" {int(C(i, j))} "
            row += value

        # update the bottom row width with the width of the bottom row
        if i == depth:
            bottom_row_width = len(row)

        # calculate the row's padding based on it's length compared to the bottom row's length
        padding = (int((bottom_row_width - len(row)) // 2)) * ' '

        # append the row at the top of the triangle
        triangle = '\n' + padding + row + padding + triangle

        i -= 1

    print(triangle)
