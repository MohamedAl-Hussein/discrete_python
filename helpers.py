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


def prepare(proposition):
    """
    Prepares a propositional string for use in a truth table.
    Splits all sub-propositions and variables and orders them based on the order of operations for propositions.

    Example
    Input: "(p & q) | (q & r)"
    Output: ["p", "q", "r", "(p & q)", "(q & r)", "(p & q) | (q & r)"

    :param proposition: a propositional string
    :return: a list of ordered variables and propositions
    """

    return sort(remove_duplicate(separate_negations(flatten(proposition))))


def sort(propositions):
    """
    Returns a sorted list of propositions, with variables sorted alphabetically at the front.

    :param propositions: a list of propositional elements with unsorted variables
    :return: an ordered list of propositions and variables
    """

    sorted_list = list()

    # add any missing variables that weren't captured in the flattening step
    missing_vars = add_missing_vars(propositions)
    sorted_list.extend(missing_vars)

    # add all variables first and then sort them alphabetically
    for prop in propositions:
        if prop.isalpha() and prop not in sorted_list:
            sorted_list.append(prop)

    sorted_list.sort()

    # add remaining propositions to end of list
    for prop in propositions:
        if not prop.isalpha():
            sorted_list.append(prop)

    return sorted_list


def add_missing_vars(propositions):
    """
    Looks through propositions in a list and returns all variables

    :param propositions: a list of propositions
    :return: a list of variables
    """

    missed_vars = list()

    for prop in propositions:
        for char in prop:
            if char.isalpha() and char not in missed_vars:
                missed_vars.append(char)

    return missed_vars


def remove_duplicate(propositions):
    """
    Removes any duplicates from a list of propositions.

    :param propositions: a list of propositions
    :return: a duplicate-free list of propositions
    """

    cleaned_list = list()

    # iterate through propositions list and only add elements that haven't been added to cleaned_list
    for prop in propositions:
        if prop not in cleaned_list:
            cleaned_list.append(prop)

    return cleaned_list


def separate_negations(propositions):
    """
    Creates a non-negated version of a proposition and adds it to the correct position in the propositions list.

    Example
    Input: ["~p"]
    Output: ["p", "~p"]

    :param propositions: a list of propositions
    :return: a list of propositions with ordered negations
    """

    separated_list = list()

    for prop in propositions:
        if prop[0] == '~':
            separated_list.append(prop[1:])

        separated_list.append(prop)

    return separated_list


def flatten(proposition):
    """
    Recursively flattens a propositional string until all sub-propositions have been identified and returns them in
    a collection.

    :param proposition: a propositional string to flatten
    :return: a list of sub-propositions and variables
    """

    # split the proposition
    chunks = split(proposition)

    # base case: splitting returned the same element
    if len(chunks) == 1:
        return chunks

    # iterate through each element in chunks
    flattened_list = list()
    for chunk in chunks:
        # recursively flatten
        inner_chunk = flatten(chunk)

        # add inner_chunk to flattened_list
        flattened_list.extend(inner_chunk)

    flattened_list.append(proposition)

    return flattened_list


def split(proposition):
    """
    Splits a proposition based on a set of symbols and returns the split portions in a list.

    Example
    Input: "p & q"
    Output: ["p", "q"]

    :param proposition: a propositional string to split
    :return: a list of propositional elements
    """

    # we have two cases:
    # case 1: the proposition is wrapped by one or more matching bracket pairs
    proposition = unwrap(proposition)

    # case 2: it is not the case that case 1 is true
    # do nothing

    # search for top level symbols of the type: ~, &, |, -->, <-->
    symbols = ['~', '&', '|', '-', '<']
    depth = 0
    splits = list()
    start = 0
    end = 0

    for indexed_char in enumerate(proposition):
        # skip a partial symbol of --> or <-->
        if indexed_char[1] == '-' and proposition[indexed_char[0] - 1] == '-':
            continue
        elif indexed_char[1] == '-' and proposition[indexed_char[0] - 1] == '<':
            continue
        elif indexed_char[1] == '>':
            continue

        # skip over anything enclosed in brackets
        if indexed_char[1] == '(':
            depth += 1
            continue
        elif indexed_char[1] == ')':
            depth -= 1
            continue

        # determine how to split a proposition based on the symbol
        if indexed_char[1] in symbols and depth == 0:

            # we have a negated proposition
            if indexed_char[1] == '~':
                if proposition[indexed_char[0] + 1].isalpha():
                    end = indexed_char[0] + 2
                elif proposition[indexed_char[0] + 1] == '(':
                    closing_bracket = find_closing_bracket(proposition[indexed_char[0] + 1:])
                    end = closing_bracket + 1
            else:
                end = indexed_char[0]

            # grab the left-most portion of the propositional string
            left_string = proposition[start:end]

            # set the starting point for the next split based on the splitter's length
            if indexed_char[1] == '-':
                start = end + 3
            elif indexed_char[1] == '<':
                start = end + 4
            else:
                start = end + 1

            # add the left-most portion to splits
            splits.append(left_string)

    # add the final half of a proposition after reaching the end of the string
    if start < len(proposition):
        splits.append(proposition[start:])

    # strip off any white spaces
    for i in range(len(splits)):
        splits[i] = splits[i].strip()

    # get rid of any empty strings
    for s in splits:
        if s == '':
            splits.remove(s)

    return splits


def unwrap(proposition):
    """
    Removes all brackets enclosing a propositional string.

    Example
    Input: "(((X+Y)))"
    Output: "X+Y"

    :param proposition:
    :return:
    """
    is_wrapped = True

    while is_wrapped:
        if proposition[0] == '(':
            closing_bracket = find_closing_bracket(proposition)
        else:
            is_wrapped = False
            continue

        if closing_bracket == len(proposition):
            proposition = proposition[1:-1]
        else:
            is_wrapped = False

    return proposition
