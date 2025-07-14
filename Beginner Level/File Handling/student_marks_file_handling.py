import csv

FILE_PATH = 'Beginner Level\\File Handling\\student_marks.csv'

def safe_int(value):
    return int(value.strip()) if value.strip().isdigit() else 0

def read_csv(filepath):
    with open(filepath, mode='r') as file:
        return list(csv.DictReader(file))

def calculate_totals(data):
    for row in data:
        row['Total_Marks'] = (
            safe_int(row['Physics']) +
            safe_int(row['Chemistry']) +
            safe_int(row['Maths']) +
            safe_int(row['English']) +
            safe_int(row['Biology']) +
            safe_int(row['Economics']) +
            safe_int(row['History']) +
            safe_int(row['Civics'])
        )
    return data

def calculate_averages(data):
    for row in data:
        row['Average'] = round(row['Total_Marks'] / 8, 2)
    return data

def write_csv(filepath, data):
    with open(filepath, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def process_student_marks(filepath):
    data = read_csv(filepath)
    data = calculate_totals(data)
    data = calculate_averages(data)
    write_csv(filepath, data)
    print("Student data processed and saved successfully.")

process_student_marks(FILE_PATH)