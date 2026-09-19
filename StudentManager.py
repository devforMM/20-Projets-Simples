class School:
    def __init__(self) -> None:
        self.students=[]
    def add_student(self,name):
        new_student=Student(name)
        self.students.append(new_student)
    def best_student(self):
        student_grades=[(s,s.average_grade())for s in self.students]
        best_student=max(student_grades,key=lambda x:x[1])[0]
        print(f"The best student is :{best_student.name} with average grade of  {best_student.average_grade()}")
    def worst_student(self):
        students_grades=[(s,s.average_grade())for s in self.students]
        worst_Student=min(students_grades,key=lambda x:x[1])[0]
        print(f"The worst student is : {worst_Student.name} with an average grade of : {worst_Student.average_grade()} ")

    def passed_students(self):
        students_grades=[(s,s.average_grade()) for s in self.students]
        for s,g in students_grades:
            if g >=10:
                print(f"Student {s.name} passed ")


    def ranking(self):
        print("the ranking of the students is ")
        students_grades=[(s,s.average_grade()) for s in self.students]
        for s,g in sorted(students_grades,key=lambda x:x[1]):
            print(f"Student {s.name}")


class Student:
    def __init__(self,n) -> None:
        self.grades=[]
        self.name=n
    def  best_grad(self):
        return max(self.grades)
    def worst_grade(self):
        return min(self.grades)
    def average_grade(self):
        return sum(self.grades)/len(self.grades)



school=School()


def system():
    print("Welcome to the school system")
    while True:
        print("""Add student
                Best student
                Worst student
                Passed students
                Ranking""")
        operation=input("Choose one of the operations above: ")
        if operation==1:
            student_name=input("Enter the Student name: ")
            school.add_student(student_name)
        elif operation==2:
            school.best_student()
        elif operation==3:
            school.worst_student()
        elif operation==4:
            school.ranking()
        else:
            break
    
        
   
