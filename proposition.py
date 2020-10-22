class Proposition:
    """
    Represents a basic propositional object, that has a truth value and can be compared against other propositional
    objects.
    """

    def __init__(self, truth_value=True):
        self._truth_value = truth_value

    def __bool__(self):
        return self._truth_value

    def get_truth_value(self):
        return self._truth_value

    def set_truth_value(self, value):
        self._truth_value = value

    def then(self, other):
        """
        Evaluates the conditional statement of the form: p --> q.

        :param other: The conclusion for the given statement.
        :return: The boolean value of the conditional statement.
        """

        if not self:
            return True
        elif self and other:
            return True

        return False

    def iff(self, other):
        """
        Evaluates the conditional statement of the form: p <--> q.

        :param other: The conclusion for the given statement.
        :return: The boolean value of the conditional statement.
        """

        if self.then(other) and other.then(self):
            return True

        return False

    def xor(self, other):
        """
        Evaluates a conditional statement of the form (p or q) & ~(p and q), equivalently, a conditional or.

        :param other: The second variable, in this case, q.
        :return: The boolean value for the conditional statement.
        """

        return (self or other) and not (self and other)
