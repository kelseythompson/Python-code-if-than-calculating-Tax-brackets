# make the dictionary if/than
Tax_bracket={500:.10, 1500:.15, 2499:.20, 2500:.3}
income=int(input('enter income'))
print(income)

# the income is in the 500 tax bracket (10%). key #0
if income < list(Tax_bracket.keys())[0]:
    tax=income*Tax_bracket[500]
elif income < list(Tax_bracket.keys())[1]:
    tax=income*Tax_bracket[1500]
elif income <= list(Tax_bracket.keys())[2]:
    tax=income*Tax_bracket[2499]
else:
    tax=income*Tax_bracket[2500]
print(tax)