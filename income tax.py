

gross_income= float(input('Enter the gross income: '))
num_dep= int(input('Enter the number of dependents: '))

def calc(bd, hhd):
    total_deduction= bd - (10000 + (3000 * hhd))
    final_tax= total_deduction * .20
    print('The income tax is', final_tax) 
    
calc(gross_income, num_dep)
