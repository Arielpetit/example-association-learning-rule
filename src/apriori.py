def generate_combinations(itemset, length):
    combinations = []
    n = len(itemset)
    if length > n:
        return combinations

    def helper(current_combination, start_index):
        if len(current_combination) == length:
            combinations.append(current_combination.copy())
            return

        for i in range(start_index, n):
            current_combination.append(itemset[i])
            helper(current_combination, i + 1)
            current_combination.pop()

    helper([], 0)
    return combinations


def apriori(transactions, min_support=0.7, min_confidence=0.5):
    itemset_length = 1
    itemsets = set()
    frequent_itemsets = {}
    strong_association_rules = {}

    for transaction in transactions:
        itemsets.update(transaction)

    while True:
        new_frequent_itemsets = {}
        combinations = generate_combinations(list(itemsets), itemset_length)

        for combination in combinations:
            support_value = support(transactions, combination)

            if support_value >= min_support:
                new_frequent_itemsets[tuple(combination)] = support_value

        if not new_frequent_itemsets:
            break

        frequent_itemsets.update(new_frequent_itemsets)
        itemset_length += 1

    for itemset in frequent_itemsets.keys():
        itemset_length = len(itemset)

        if itemset_length < 2:
            continue

        for i in range(1, itemset_length):
            combinations = generate_combinations(list(itemset), i)

            for combination in combinations:
                remaining = list(set(itemset) - set(combination))
                confidence_value = confidence(transactions, (combination, remaining))

                if confidence_value >= min_confidence:
                    strong_association_rules[(combination, remaining)] = confidence_value

    return frequent_itemsets, strong_association_rules