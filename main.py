# import csv
# with open('student.csv', 'r') as file:
#     reader = csv.reader()
#     next(reader)  # skip header
#     for row in reader:
#         id, name, otch, class_, extra = row
#         login = _login(f"{name} {otch}")
#         password = _password()
#         students.
#     data = file.read()
# print(data)
#
#
# def _name():
#     pass
#
#
#
#
#
# import csv
# import random
#
# def _username(name):
#     name_parts = name.split()
#     surname = name_parts[0]
#     initials = ''.join([name[0] for name in name_parts[1:]])
#     return f"{surname} {initials}"
# def _password():
#     password = ''.join(random.choices('QWERTYUIOPLKJHFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm0123456789', k=8))
#     return password
#
# def _username_password(csv_file):
#     with open('student.csv', 'r') as file:
#         reader = csv.reader(file)
#         students = [row for row in reader]
#
#     for student in students:
#         name = student[1].strip()
#         username = _username(name)
#         password = _password()
#         student.extend([username, password])
#
#     with open('students_password.csv', 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows(students)



import csv
def search_student(project_id):
    with open('student.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['project_id']) == project_id:
                return f"Проект № {row['project_id']} делал: {row['name']} {row['surname']} {row['patronymic']} он(а) получил(а) оценку {row['grade']}"
    return "Ничего не найдено"

while True:
    project_id = int(input("Введите id проекта (или СТОП для завершения): "))
    if project_id == "стоп":
        break
    result = search_student(project_id)
    print(result)


