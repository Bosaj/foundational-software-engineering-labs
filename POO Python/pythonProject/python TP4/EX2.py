class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def get_average_grade(self):
        if not self.students:
            return 0
        return sum(student.get_grade() for student in self.students) / len(
            self.students
        )


# Création des objets Student
student1 = Student("Alice", 20, 18)
student2 = Student("Bob", 21, 16)
student3 = Student("Charlie", 19, 15)

# Création de l'objet Course
course = Course("Maths", 2)

# Ajout des étudiants au cours
print("Ajout de student1 au cours :", course.add_student(student1))  # True
print("Ajout de student2 au cours :", course.add_student(student2))  # True
print(
    "Ajout de student3 au cours :", course.add_student(student3)
)  # False (Capacité maximale atteinte)

# Affichage de la moyenne des notes des étudiants inscrits au cours
print("Moyenne des notes des étudiants inscrits au cours :", course.get_average_grade())
