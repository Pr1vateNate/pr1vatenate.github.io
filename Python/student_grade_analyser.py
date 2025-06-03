
print("Enter your full name:")
studentName = input()
print("Enter your grade in Math:")
mathGrade_str = input()
mathGrade = int(mathGrade_str)
print("Enter your grade in Science:")
scienceGrade_str = input()
scienceGrade = int(scienceGrade_str)
print("Enter your grade in English:")
englishGrade_str = input()
englishGrade = int(englishGrade_str)
print("Enter your grade in History:")
historyGrade_str = input()
historyGrade = int(historyGrade_str)
print("Enter your grade in Art:")
artGrade_str = input()
artGrade = int(artGrade_str)
grades = [mathGrade, scienceGrade, englishGrade, historyGrade, artGrade]
subjects = ("Math", "Science", "English", "History", "Art")
gradeList = {
    subjects[0]: grades[0],
    subjects[1]: grades[1],
    subjects[2]: grades[2],
    subjects[3]: grades[3],
    subjects[4]: grades[4]
} 
averageGrade = sum(grades) / len(grades)    #Calculate average
highestGrade = max(grades)                  #Calculate highest grade
lowestGrade = min(grades)                   #Calculate lowest grade
highestIndex = grades.index(highestGrade)
lowestIndex = grades.index(lowestGrade)
highestSubject = subjects[highestIndex]
lowestSubject = subjects[lowestIndex]
print(f"Hello {studentName}!")
print(f"Your grades: {subjects[0]} ({grades[0]}), {subjects[1]} ({grades[1]}), {subjects[2]} ({grades[2]}), {subjects[3]} ({grades[3]}), {subjects[4]} ({grades[4]})")
print(f"Highest grade: {highestGrade} ({highestSubject})")
print(f"Lowest grade: {lowestGrade} ({lowestSubject})")
print(f"Average: {averageGrade}")
if averageGrade >= 85:
    print("Result: Great job!")
if averageGrade >= 60 and averageGrade < 85:
    print("Result: You passed!")
if averageGrade < 60:
    print("Result: You failed. Try harder next time!")
