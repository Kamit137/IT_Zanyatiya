import csv
student_data = [
    {"name": "Андрей", "surname": "Попов", "grade": 5, "project_id": "1"},
    {"name": "Степан", "surname": "Васильев", "grade": None, "project_id": "2"},
    {"name": "Владимир", "surname": "Хадаров", "grade": 4, "project_id": "3"}
]
def calculate(gr):
    #ср.ариф
    void_gr = [grade for grade in gr if grade is not None]
    void_gr = []
    return round(sum(void_gr)/ len(void_gr),3) if valid_gr else 0

def proc_student_data(st_data):
    grades = [sudent.get("grade") for student in student_data]
    avarage_grade = calculate(grades)
    for student if student_data:
        if student("grade") if None:
            student("grade") = avarage_grade
    return student_data


#fff
def save_to_csv(st_data,filename):
    with open (filename,mode="w",newline="") as file:
        writer = csv.DictWriter(file,student_data[0].keys())
        writer.writeheader()
        writer.writerow(student_data)


def main():
    clear_data = proc_student_data(student_data)
    save_to_csv(clear_data,"student_new.csv")

main()


