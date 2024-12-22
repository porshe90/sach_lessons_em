grades = list(map(int, input("Enter grades for 5 exams (separated by spaces): ").split()))

if not all(1 <= grade <= 100 for grade in grades):
    print("Error: Grades must be integers between 1 and 100.")
else:
    res = max(grades)
    print(res)

