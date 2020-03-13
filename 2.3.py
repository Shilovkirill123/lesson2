school= [
    {'school_class' : '1A', 'assessments' : [4,4,3,5,3,3,4]},
    {'school_class' : '2A', 'assessments' : [3,5,5,2,4,5,3]},
    {'school_class' : '3A', 'assessments' : [2,4,3,5,4,5,4]},
    {'school_class' : '3B', 'assessments' : [3,4,3,2,3,3,4]},
    {'school_class' : '5A', 'assessments' : [5,3,5,4,3,4,5]},
    {'school_class' : '6A', 'assessments' : [3,5,5,4,3,4,4]}
]

sum_school=0
Number_of_classes=0
for classes in school:
    
    grade_average = sum(classes['assessments'])/len(classes['assessments'])
    print(f'Средняя оценка в {classes["school_class"]}: {grade_average}')
    Number_of_classes += 1
    sum_school += grade_average

print(f'Средняя оценка по школе: {Number_of_classes/sum_school} ')   