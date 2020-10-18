def find_closing_bracket(search_area):
    """
    Returns the index position of the closing bracket within a string of 1 or more nested brackets.

    :param search_area: the string we are searching inside
    :return: integer representing the index of the closing bracket
    """

    # start count from 1 and count up for each new opening bracket and down otherwise.
    # stop once we reach 0.
    # start count and i at one since we already have an opening bracket at the 0th index.

    count = 1
    i = 1

    while count != 0:
        if i >= len(search_area):
            count = 0
            continue

        char = search_area[i]
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        i += 1

    return i


def get_nested_brackets(equation):
    """
    Returns a list representing each set of elements within nested brackets.
    Note: Only works with a single set of nested brackets at the time being.

    Example:
    Input: "((X))"
    Output: ["X", "(X)", "((X))"]

    :param equation: a string representation of an equation with nested brackets
    :return: a collection of objects within each depth of the nested brackets
    """

    # base case when no nested brackets are left inside equation
    if equation.count('(') == equation.count(')') == 0:
        return [equation]
    else:
        starting_index = equation.find('(')
        closing_index = find_closing_bracket(equation)
        search_area = equation[starting_index+1:closing_index-1]

    return get_nested_brackets(search_area) + [equation]
