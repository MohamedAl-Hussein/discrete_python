from statement import Statement


class Conditional:
    """
    A class providing methods to evaluate conditional statements.
    """

    @staticmethod
    def if_then(p, q):
        """
        Evaluates the conditional statement of the form: p --> q.

        :param p: The hypothesis for the given statement.
        :param q: The conclusion for the given statement.
        :return: The boolean value of the conditional statement.
        """

        if not p:
            return True
        elif p and q:
            return True

        return False

    @staticmethod
    def if_and_only_if(p, q):
        """
        Evaluates the conditional statement of the form: p <--> q.

        :param p: The hypothesis for the given statement.
        :param q: The conclusion for the given statement.
        :return: The boolean value of the conditional statement.
        """

        if Conditional.if_then(p, q) and Conditional.if_then(q, p):
            return True

        return False

    @staticmethod
    def for_all(p, q, domain, num_vars):
        """
        Iterates over a given domain, checking to see if the universal statement of the forms:
        For all x in the Domain, if P(x) --> Q(x), or
        For all x,y in the Domain, if P(x,y) --> Q(x,y).

        :param p: The hypotheses for the given statement, P.
        :param q: The conclusion for the given statement, Q.
        :param domain: A collection object depicting the domain we want to test the conditional against.
        :param num_vars: The number of variables to consider. Choose between 1 and 2.
        :return: True if the universal conditional is true, False otherwise
        """

        if num_vars == 1:
            for x in domain:
                p.x = x
                q.x = x
                s = Statement(p.expression.replace('x', str(x)))
                t = Statement(q.expression.replace('x', str(x)))
                if not Conditional.if_then(s, t):
                    return False

        elif num_vars == 2:
            for x in domain:
                p.x = x
                q.x = x
                for y in domain:
                    p.y = y
                    q.y = y
                    s = Statement(p.expression.replace('x', str(x)))
                    t = Statement(q.expression.replace('x', str(x)))
                    s = Statement(s.expression.replace('y', str(y)))
                    t = Statement(t.expression.replace('y', str(y)))
                    if not Conditional.if_then(s, t):
                        return False

        return True
