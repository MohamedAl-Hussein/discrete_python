def determine_parity(n):
    """
    The parity is the quality of an integer being even or odd.
    An integer n is even if there exists an integer k such that n = 2k.
    An integer n is odd if there exists an integer k such that n = 2k + 1.

    This function will determine the parity of a given number and prints it.
    """
    
    parity = None

    # We take the absolute value of the number so that the range is increasing
    # for negative numbers.
    # If we look at the definitions for even and odd integers, we see that
    # the maximum value k can achieve is half of n for even integers, and half
    # of n-1 for odd integers. So we want the range to go from 0 up to
    # floor(|n|/2)+1 to cover all integers that are divisible by n.
    
    search_to = abs(n // 2) + 1
    
    for k in range(search_to):
        if abs(n) == 2 * k:
            parity = "even"
        elif abs(n) == 2 * k + 1:
            parity = "odd"

    print("The parity of", n, "is", parity)
