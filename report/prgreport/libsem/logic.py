class Term(tuple):
    """Models terms for a conjunctive dependency logic.

    Terms for the dependency logic can be converted using
    A deterministic procedure from the ``Token''s in a
    Stanford Universal Dependency graph
    """

    def __init__(self, dep):
        """Creates a new term named 'form' with the given variables.

        :param dep: (Token) a dependency relation
        """
        if dep is not None:
            form = dep.form.lower()
            tuple.__init__(self, (form, dep.pos))
            self.form = form
            self.pos = dep.pos

    def __new__(cls, *args, **kwargs):
        return tuple.__new__(cls, (args[0].form.lower(), args[0].pos))

    def __str__(self):
        return '%s[%s]' % (self.form, self.pos)

    @classmethod
    def from_iterable(cls, iterable):
        return Term(_MockDep(iterable))


class _MockDep(object):
    def __init__(self, iterable):
        self.form = iterable[0]
        self.pos = iterable[1]



class Var(object):
    """An unspecified object in a query.

    A predicate is used to test elements in a ``FreqGraph''
    to see if they fit a given formula.
    """
    def __init__(self, name, pred=lambda G, x: True):
        """Creates a new variable.

        :param name (str): a variable name
        :param pred (function): a predicate over graph nodes
            default: (G, x) => True.
        """
        self.name = name
        self.pred = pred