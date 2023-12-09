from typing import List, Tuple

dataset_type = List[List[object]]
rule_type = Tuple[List[object], List[object]]


def confidence(data_set: dataset_type, rule: rule_type) -> float:
    """
    Calculate the confidence of a rule in a dataset.
    """
    antecedent, consequent = rule
    antecedent_support = support(data_set, antecedent)
    rule_support = support(data_set, antecedent + consequent)
    if antecedent_support == 0:
        return 0
    return rule_support / antecedent_support