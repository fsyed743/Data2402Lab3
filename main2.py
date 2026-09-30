from classes import PatientExam

# your code here
def load_exams(filename: str) -> list[PatientExam]:
    exams = []
    with open(filename, 'r') as file:
        contents = file.read().strip()
        rows = contents.split('\n')
        header = rows.pop(0)

        for row in rows:
                    values = row.strip().split(',')
                    exam_id = int(values[0])
                    date = values[1]
                    patient_name = values[2].strip()
                    weight = float(values[3])
                    height = float(values[4])
        
                    exam = PatientExam(exam_id, date, patient_name, weight, height)
                    exams.append(exam)
        
        return exams

def average_bmi(exams: list[PatientExam]) -> float:
    total = 0
    for exam in exams:
        total += exam.calculate_bmi()
    return total / len(exams)


def busiest_month(exams: list[PatientExam]) -> int:
    month_counts = dict()
    for exam in exams:
        month = exam.get_month()
        month_counts[month] = month_counts.get(month, 0) + 1

    busiest = max(month_counts, key=month_counts.get)
    return busiest


exams = load_exams("patient_data.csv")

avg_bmi = average_bmi(exams)
print(f"Average BMI: {avg_bmi:.2f}")

month = busiest_month(exams)
print(f"Busiest month: {month}")
