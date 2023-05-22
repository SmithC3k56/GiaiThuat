if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    mean = 0.00
    for key in student_marks:
        if key == query_name:
            sumss = 0
            marks = student_marks[key]
            for j in marks:
                sumss += j
            mean = sumss / len(marks)

    print("{:.2f}".format(mean))


# give a dictionary include keys are student'names and value are list marks of each student => result is mean of student's marks