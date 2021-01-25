# logicBottomUp.py - Bottom-up Proof Procedure for Definite Clauses
# AIFCA Python3 code Version 0.8.0 Documentation at http://aipython.org

# Artificial Intelligence: Foundations of Computational Agents
# http://artint.info
# Copyright David L Poole and Alan K Mackworth 2017.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

from logicProblem import yes

def fixed_point(kb):
    """Returns the fixed point of knowledge base kb."""
    fp = ask_askables(kb)
    added = True
    while added:
        added = False  # added is true when an atom was added to fp this iteration
        for c in kb.clauses:
            if c.head not in fp and all(b in fp for b in c.body):
                fp.add(c.head)
                added = True
    return fp


def ask_askables(kb):
    return {at for at in kb.askables if yes(input("Is " + at + " true? "))}


#from logicProblem import KB,Clause
#example_KB = KB([Clause("fever",["high temperature","common cold"]),Clause("high temperature"),Clause("common cold")])
#print(fixed_point(example_KB))