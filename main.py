def profit(salary):
    tax = 0.13
    bonus = salary * 0.7 / 3
    bonus = bonus - bonus * tax
    total = salary - salary * tax
    return round(total, 0), round(bonus, 0), round((total + bonus), 0)


ba_salary = 165700
pm_salary = 1957000

print("Total salary for Business Analyst:", profit(ba_salary))
print("Total salary for Product Manager:", profit(pm_salary))
