import numpy as np
marks = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])
student_avg = np.mean(marks, axis=1)
print("Student Average -", student_avg)
subject_avg = np.mean(marks, axis=0)
print("Subject Average -", subject_avg)
total_scores = np.sum(marks, axis=1)
best_student_index = np.argmax(total_scores)
print("Top Student Index (highest total score) -", best_student_index)
marks[:, 2] += 5
print("New Updated Score -", marks)