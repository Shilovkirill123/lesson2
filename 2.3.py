school= [
    {'school_class' : '1A', 'assessments' : [4,4,3,5,3,3,4]},
    {'school_class' : '2A', 'assessments' : [3,5,5,2,4,5,3]},
    {'school_class' : '3A', 'assessments' : [2,4,3,5,4,5,4]},
    {'school_class' : '3B', 'assessments' : [3,4,3,2,3,3,4]},
    {'school_class' : '5A', 'assessments' : [5,3,5,4,3,4,5]},
    {'school_class' : '6A', 'assessments' : [3,5,5,4,3,4,4]}
]


a=sum(school[0]['assessments'])/len(school[0]['assessments'])
print(f'Средняя оценка 1A: {a}')
b=sum(school[1]['assessments'])/len(school[1]['assessments'])
print(f'Средняя оценка 2A: {b}')
c=sum(school[2]['assessments'])/len(school[2]['assessments'])
print(f'Средняя оценка 3A: {c}')
d=sum(school[3]['assessments'])/len(school[3]['assessments'])
print(f'Средняя оценка 3B: {d}')
e=sum(school[4]['assessments'])/len(school[4]['assessments'])
print(f'Средняя оценка 5A: {e}')
f=sum(school[5]['assessments'])/len(school[5]['assessments'])
print(f'Средняя оценка 6A: {f}')

print(f'Средний бал по школе: {(a+b+c+d+e+f)/6}')