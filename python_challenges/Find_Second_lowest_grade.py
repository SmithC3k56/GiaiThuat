def print_second_lowest_grade(students):

  grades = []
  for student in students:
    grades.append(student[1])
  grades.sort()
  count = 0
  l = len(grades)
  new_grades =[]
  for i in grades:
      if i < 0:
          new_grades.append(i)

  if l == len(new_grades):
      grades = new_grades
      for i in range(0, l):
          if i + 1 > l - count: break

          if l - count > 1 | i + 1 < l - count and grades[i] == grades[i + 1]:
              count += 1
              grades.remove(grades[i])
  else:
    for i in range(0,l ):
      if i+1 >  l - count: break
      if grades[i] < 1:
          count += 1
          grades.remove(grades[i])
      if  l-count > 1 | i+1 < l - count and grades[i] == grades[i+1] :
          count +=1
          grades.remove(grades[i])



  # Find the second lowest grade.
  if len(grades) == 1:
      second_lowest_grade = grades[0]
  else:
      second_lowest_grade = min(grades[1:])
  # Find all students with the second lowest grade.
  students_with_second_lowest_grade = []
  for student in students:
    if student[1] == second_lowest_grade:
      students_with_second_lowest_grade.append(student[0])

  # Sort the students alphabetically.
  students_with_second_lowest_grade.sort()

  # Print the names of the students.
  for student in students_with_second_lowest_grade:
    print(student)


# Create a list of lists to store the names and grades of the students.
students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

# Print the names of any student(s) having the second lowest grade.
print_second_lowest_grade(students)


# n là số học sinh=> nhập lần lượt tên => điểm của học sinh đó và tìm ra học sinh có số điểm thấp thứ 2