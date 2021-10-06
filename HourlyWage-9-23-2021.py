hourlypay=float(input('Hourly Pay: '))
WorkHours=int(input('Total Weekly hours: '))

Week1=.817*(hourlypay*WorkHours)
Week2=2*Week1
Week3=3*Week1
Week4=4*Week1

Statement=("Hours: {} \n Hourly Wage: {}$ \n 1 week: {}$ \n semi-monthly: {}$ \n 3 weeks: {}$ \n 1 month: {}$")

print(Statement.format(hourlypay,WorkHours,Week1,Week2,Week3,Week4))
