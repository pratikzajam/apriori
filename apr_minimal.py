from efficient_apriori import apriori

transcations = [('eggs', 'bacon', 'soup'),
                ('eggs', 'bacon', 'apple'),
                ('soup', 'bacon', 'banana')]
 
_, rules_list = apriori(transcations, min_support=0.5,
        min_confidence=1)

for rule in rules_list:
    print(rule)

