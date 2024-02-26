from cs60_validator import CS60Validator
from datetime import datetime

def check_graduation(student_data):
    date_of_admission = student_data['date_of_admission']
    years = datetime.date(date_of_admission).year

    result = None

    # (FUTURE) Add more if-else for different major and years
    if student_data["student_major"] == "Computer Science" and years >= 2017 and years < 2022:
        result = CS60Validator().validate(student_data)

    # Currently except only CS Major (TODO: throw error)

    student_data.update({
        "is_graduate": result,
    })

    return student_data