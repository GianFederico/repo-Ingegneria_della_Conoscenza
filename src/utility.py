from logicProblem import KB
from logicBottomUp import fixed_point
import os

class ProbItem:
    def __init__(self, name, prob):
        self.name = name
        self.prob = prob

    def __str__(self):
        return self.name + " -> " + str(self.prob)

    def __repr__(self):
        return str(self)

    def __lt__(self, item):
        return self.prob < item.prob


def get_disease(kb=KB()):
    """ Returns all diseases true in the KB fixed point, starting from the symptoms true """
    fp = fixed_point(kb)  # punto fisso della kb
    atoms = {c.head for c in kb.clauses if c.isAtom()}  # nessuno degli atomi è una malattia
    return list(fp.difference(atoms))


def get_prob_model(kb=KB()):
    """Returns a list of ProbItems obj which stands for a probabilistic model with the probability of the patient
       to have that specific disease. If there are no disease returns empty."""
    disease = get_disease(kb)  # prendo le malattie vere dalla base di conoscenza

    if len(disease) == 0:
        return []  # non ci sono malattie vere

    model = []  # variabile modello con il ranking delle probabilità di ogni malattia
    for d in disease:
        model.append(ProbItem(d, get_prob(d, kb))) # appendo un oggetto di tipo ProbItem al modello

    sumProb = sum(item.prob for item in model)  # somma delle probabilità (per somma totale = 1)
    for item in model:
        item.prob = item.prob / sumProb  # sostituzione probabilità ricalcolata
    model.sort(reverse=True)
    return model


def get_prob(disease, kb=KB()):
    """Returns the probability of a disease to be true on a pre-condition:
       the disease must have an associate clausole with a non-null body"""
    allSym = len({c.head for c in kb.clauses if c.isAtom()})  # prendo il numero dei sintomi che sono veri
    for c in kb.clauses:  # cerco la malattia
        if c.head == disease:
            return len(c.body) / allSym  # restituisco il numero di sintomi che ha su tutti quelli veri


def how(KB, item):
    for c in KB.clauses:
        if c.head == item:
            return c
    return None


def real_filename(filename=""):
    return os.path.realpath(filename)
