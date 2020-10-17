class Statement:
    """
    An object representing a propositional statement.
    """

    def __init__(self, expression):
        self.x = 0
        self.y = 0
        self.z = 0
        self.expression = expression

    def __bool__(self):
        return eval(self.expression)
