class Proposition:
    """
    Represents a basic propositional object, that has a truth value and can be compared against other propositional
    objects.
    """

    _expression = str()
    _variables = dict()

    def __init__(self, truth_value=True):
        self._truth_value = truth_value

    def __bool__(self):
        return self._truth_value

    def get_truth_value(self):
        """
        Get the truth value of the current object.
        :return: boolean
        """

        return self._truth_value

    def set_truth_value(self, value):
        """
        Set the truth value for the current object.
        :param value: truth value
        """

        self._truth_value = value

    def get_variables(self):
        """
        Get a dictionary representing all variables and their values for this current object.

        Example
        { x : 0, y : 2, ... }

        :return: dictionary
        """

        return self._variables

    def add_variable(self, variable, value):
        """
        Add a variable with an assigned value to this object.
        :param variable: a string representation of a variable name
        :param value: the variable's value
        """

        self._variables[variable] = value

    def show_variable_value(self, variable):
        """
        Show a variable's current value.
        :param variable: the variable name to lookup
        :return: the variable's current value
        """

        return self._variables[variable]

    def change_variable_value(self, variable, value):
        """
        Update the value for a given variable.
        :param variable: the variable's name
        :param value: the new value to assign to the variable
        """

        self._variables[variable] = value

    def set_expression(self, expression, *variables):
        """
        Create an expression with one or more variables and replace the variables with their associated values.

        Example
        "x > y" becomes "0 > 2"

        :param expression: the expression we want to set
        :param variables: one or more variables to assign to the expression
        """

        _expr = expression

        for variable in variables:
            _val = self._variables[variable]
            _expr = _expr.replace(variable, str(_val))

        self._expression = _expr

    def get_expression(self):
        """
        Get a string representation of the current object's expression.
        :return: string
        """

        return self._expression

    def evaluate_expression(self):
        """
        Evaluate the current object's expression.
        :return: boolean
        """

        return eval(self._expression)

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
