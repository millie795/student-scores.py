import csv

# Student names and scores
students = [
    ["John", 75],
    ["Mary", 90],
    ["Peter", 65],
    ["Grace", 85],
    ["David", 80]
]

# Write student records into a CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Score"])
    writer.writerows(students)

print("Student records saved successfully!")

# Read the CSV file
student_records = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        student_records.append({
            "name": row["Name"],
            "score": float(row["Score"])
        })

# Calculate class average
total_score = sum(student["score"] for student in student_records)
average = total_score / len(student_records)

# Identify the top performer
top_student = max(student_records, key=lambda student: student["score"])

# Display results
print("\n===== CLASS RESULTS =====")

print("\nStudent Scores:")
for student in student_records:
    print(f"{student['name']}: {student['score']}")

print(f"\nClass Average: {average:.2f}")
print(f"Top Performer: {top_student['name']}")
print(f"Highest Score: {top_student['score']}")