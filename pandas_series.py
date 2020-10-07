import pandas as pd

grades = pd.Series([87,100,94])

myarray = pd.Series(98.6, range(3))

'''
print(myarray)

print(grades[0])

print(grades.describe())
'''

grades = pd.Series([87,100,94],index=['Wally','Eva','Sam'])

print(grades)

grades = pd.Series({'Wally':87, 'Eva':100, 'Sam':94})

print(grades)

hardware = pd.Series(['Hammer','Saw','Wrench'])

a = hardware.str.contains('a')

print(a)

b = hardware.str.upper()

print(b)