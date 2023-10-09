def revers_grade(grade_array):
    new_grade_array = []

    for i in grade_array:
        temp = []
        for j in i:
            temp.append(j)
        temp.reverse()
        new_grade_array.append(int(''.join(temp)))

    return ','.join([str(n) for n in new_grade_array])

grade_array = input().split(',')
print(revers_grade(grade_array))