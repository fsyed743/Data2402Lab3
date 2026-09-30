
class PatientExam:
    def __init__(self, exam_id: int, date: str, patient_name: str, weight: float, height: float):
        self.exam_id = exam_id
        self.date = date
        self.patient_name = patient_name
        self.weight = weight
        self.height = height
       
    def calculate_bmi(self) -> float:
        return self.weight/(self.height ** 2)

    def get_month(self) -> int:
        month = self.date.split('/')[0] 
        return int(month)

    def __repr__(self):
        return f"PatientExam({self.exam_id}, {self.date}, {self.patient_name})"
        
