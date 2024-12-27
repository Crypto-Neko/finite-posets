class FinitePoset:
    # elements (list) - list of the elements of the finite poset
    # relation (dict) - dict in which {a : b, c, ...} implies a < b, a < c, a < ..., ...
    def __init__(self, elements, relation):
        for pair in relation:
            if len(pair) != 2 or pair[0] not in elements or pair[1] not in elements:
                except ValueError("Relation must contain pairs of elements in the poset.")
        self.elements = elements
        self.size = len(elements)
        self.relation = relation

    # Computes the value of mu(x, y), where mu is the Mobius function of P
    def mobius(self, x, y):
        if y > x:
            except ValueError("Mobius function is only defined for x <= y.")
        if x == y:
            return 1
        else:
            return 1 + self.mobius(x+1, y)

