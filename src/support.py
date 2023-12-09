from typing import List, Dict

dataset_type = List[List[object]]
itemset_type = List[object]


def support(itemsets: dataset_type, data_set: itemset_type) -> float:
    """
    Calculate the support of itemsets in a dataset.
    """
    support_count = 0
    for transaction in itemsets:
        if set(data_set).issubset(set(transaction)):
            support_count += 1
    return support_count / len(itemsets)