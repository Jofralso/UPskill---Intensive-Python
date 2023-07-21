def calculate_average_grade(student_grades):
    average_grades = {}

    for student, grades in student_grades.items():
        total_grades = sum(grades)
        average = total_grades /len(grades)
        average_grades[student] = average
    return average_grades

student_grades = {
    "Alice": [80, 90, 75],
    "Bob": [85, 95, 70],
    "Charlie": [90, 80, 85]
}

print(calculate_average_grade(student_grades))

#####################



text = "The quick brown lazy fox jumps over the lazy dog jumps quick"
print(text.split())

def count_word_frequency(text):
    words =  text.split()
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] +=1
        else:
            word_frequency[word] =1
    return word_frequency

print(count_word_frequency(text))
# Output: {'The': 1, 'quick': 1, 'brown': 1, 
# 'fox': 1, 'jumps': 1, 'over': 1, 'the': 1, 'lazy': 1, 'dog': 1}