import pandas as pd

grades_dict = {'Wally':[87,96,70],'Eva':[100,87,90],'Sam':[94,77,90],'Katie':[100,81,82],'Bob':[83,65,85]}

grades = pd.DataFrame(grades_dict)

grades.index = ['Test 1','Test 2','Test 3']
'''
print(grades)

print(grades.Sam)
'''

print(grades.loc[['Test 1','Test 2'],['Eva','Katie']])
#print(grades.iloc[0:2])
