import logicProblem as lp
import owlready2 as owl

REAL_CLASS_LABEL = 0  # lable di classe nella prima posiz(solo comodità)

def get_class(ontology, class_name):
    """Function returns a list of subclasses of the class named class_name"""
    for c in ontology.classes():
        if class_name in c.label:  # se ho trovato la classe target allora cerco tutte le sottoclassi e le restituisco
            res = ontology.search(is_a=c)
            return res


def build_map(ontology):
    """function returns a dctionary <string, list<string>> where the key is the name of the disease,
       and the value is the list symptoms names that causes the disease"""
    _map = {}  # è il dizionario che conterrà come chiave il nome della malattia e come valore la lista di sintomi che la causa
    dis = get_class(ontology, "disease")  # prendo tutte le malattie
    for d in dis:  # per ogni malattia
        sym = d.has_symptom  # prendo tutti i sintomi coinvolti in tale malattia
        sintomi = []
        for j in sym:
            sintomi.append(j.label[REAL_CLASS_LABEL])  # inserisco le label per i sintomi
        if sym: _map[d.label[REAL_CLASS_LABEL]] = sintomi
        # se ci sono sintomi cha causano la malattia:
        # imposto come chiave il nome reale della malattia e come valore la lista dei nomi reali dei sintomi coinvolti nella malattia
    return _map


def create_KB(map_disease_symptom):
    statements = []  # tutte le clausole
    for k in map_disease_symptom.keys():  # itero su tutte le malattie
        defined_clause = lp.Clause(k, map_disease_symptom.get(k)) # costruisce una clausola definita con k(malattia) come testa e sintomi come corpo
        statements.append(defined_clause)
    _KB = lp.KB(statements)  # oggetto con tutte le clausole
    return _KB


def list_symptoms(map_disease_symptoms):
    symptoms = []
    for k in map_disease_symptoms.keys():
        symptom = map_disease_symptoms.get(k)
        for i in symptom:
            symptoms.append(i)
    symptoms = list(set(symptoms))
    symptoms.sort()
    return symptoms