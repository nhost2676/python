mealCost = raw_input()
tipPercent = raw_input()
taxPercent = raw_input()
tip = 12 * float(tipPercent) / 100
tax = 12 * float(taxPercent) / 100
totalCost = mealCost + tip + tax
print "The total meal cost is",int(round(totalCost)),"dollars."