class Generators:
    """
    Static methods for generating combinations and permutations from a collection of objects.
    """

    @staticmethod
    def all_r_combinations(r, elements):
        """
        Generate all r-combinations of a given set of elements.

        :param r: the size of each combination
        :param elements: the set of all elements to choose from
        :return: a list of all r-combination sets
        """

        # the smallest value of a given r-combination is {1,2,...,r-1,r}
        # the largest value of a given r-combination is {n-r+1,n-r+2,...,n-1,n}
        # we will be searching in lexicographic order, so we start from the smallest value and stop at the largest.
        combinations = list()
        start = elements[:r]
        end = elements[len(elements) - r:]

        combination = start
        combinations.append(combination)

        while combination != end:
            result = Generators.next_r_combination(combination, elements)
            combinations.append(result)

        return combinations

    @staticmethod
    def next_r_combination(current_r_combination, elements):
        """
        Generate the next r-combination in lexicographic order.

        :param current_r_combination: the current r-combination
        :param elements: the set of all elements to choose from
        :return: the next r-combination set
        """

        r = len(current_r_combination)
        i = r - 1
        n = len(elements)

        # keep moving down the current r-combinations set until we find an element that does not match the
        # order of the given set of elements
        while current_r_combination[i] == elements[n - r + i]:
            i -= 1

        # assign the next largest value to the position where a non-match was found
        current_r_combination[i] = elements[elements.index(current_r_combination[i]) + 1]

        # replace every element afterwards in order
        for j in range(i + 1, r):
            current_r_combination[j] = elements[elements.index(current_r_combination[j - 1]) + 1]

        return set(current_r_combination)
