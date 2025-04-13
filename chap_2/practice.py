from utils.generators import StudentGenerator
from utils.vi_dict_sorter import get_vi_name_key
from typing import List, Optional, Callable
import pandas as pd


class Student:
    def __init__(self, student_id, name, gender, home, math, algo, prog):
        self.student_id = student_id
        self.name = name
        self.gender = gender
        self.home = home
        self.math = round(math, 1)
        self.algo = round(algo, 1)
        self.prog = round(prog, 1)
        self.avg = round(sum([self.math, self.algo, self.prog])/3, 1)

    def get_standardized_name(self):
        return " ".join([n.capitalize() for n in self.name.split()])

    def get_upper_name(self):
        return self.name.upper()
    
    def get_lower_name(self):
        return self.name.lower()
    
    def print_student_info(self, formatted_name):
        print(
            f"{self.student_id:<14} {formatted_name:<30} {self.gender:<6} "
            f"{self.home:<15} {self.math:<5} {self.algo:<5} "
            f"{self.prog:<5} {self.avg:<5}"
        )
    

class StudentManager:
    def __init__(self, students: Optional[List[Student]]=None):
        self.students = students if students else []

    @classmethod
    def generate_students(cls, n_students):
        # Generate names and genders, avoiding duplicated names
        NAME_RETRIES = 3    # Number of retries to generate a unique name
        names = []
        genders = []
        for _ in range(n_students):
            exceeded_retries = True
            for __ in range(NAME_RETRIES):
                name, gender = StudentGenerator.generate_name_and_gender()
                if name not in names:
                    names.append(name)
                    genders.append(gender)
                    exceeded_retries = False
                    break
            if exceeded_retries:    # Add the name even if it was duplicated
                names.append(name)
                genders.append(gender)
        # Generate the remaining attributes
        student_ids = [StudentGenerator.generate_student_id() for _ in range(n_students)]
        homes = [StudentGenerator.generate_home() for _ in range(n_students)]
        math_scores = [StudentGenerator.generate_score() for _ in range(n_students)]
        algo_scores = [StudentGenerator.generate_score() for _ in range(n_students)]
        prog_scores = [StudentGenerator.generate_score() for _ in range(n_students)]
        # Create Student objects
        return cls([
            Student(
                student_id=student_ids[i],
                name=names[i],
                gender=genders[i],
                home=homes[i],
                math=math_scores[i],
                algo=algo_scores[i],
                prog=prog_scores[i]
            ) for i in range(n_students)
        ])

    @classmethod
    def from_file(cls, filename):
        # Read from xlsx file only
        if not filename.endswith(".xlsx"):
            raise ValueError("Filename must end with .xlsx")
        df = pd.read_excel(filename)
        students = []
        for _, row in df.iterrows():
            students.append(
                Student(
                    row['ID'],
                    row['Name'],
                    row['Gender'],
                    row['Home'],
                    row['Math'],
                    row['Algo'],
                    row['Prog'],
                    row['Avg']
                )
            )
        # Clean up the memory
        del df
        return cls(students)

    def to_file(self, filename):
        # Write to xlsx file (csv messes up Vietnamese names)
        if not filename.endswith(".xlsx"):
            raise ValueError("Filename must end with .xlsx")
        student_data = [
            {
                "ID": student.student_id,
                "Name": student.get_standardized_name(),
                "Gender": student.gender,
                "Home": student.home,
                "Math": student.math,
                "Algo": student.algo,
                "Prog": student.prog,
                "Avg": student.avg
            } for student in self.students
        ]
        df = pd.DataFrame(student_data)
        df.to_excel(filename, index=False)
        print(f"Data saved to {filename}")
        # Clean up the memory
        del df, student_data
        
    def add_student(self, student: Student):
        self.students.append(student)

    def print_list(self, name_getter: Callable[[Student], str]):
        print(
            f"{'ID':<14} {'Name':<30} {'Gender':<6} {'Home':<15} "
            f"{'Math':<5} {'Algo':<5} {'Prog':<5} {'Avg':<5}"
        )
        print("-"*90)
        for student in self.students:
            student.print_student_info(name_getter(student))
        print("-"*90)

    def sort_by_name(self):
        self.students.sort(key=lambda s: get_vi_name_key(s.name))

    def sort_by_home(self):
        self.students.sort(key=lambda s: s.home)

    def sort_by_score(self, subject):
        if subject not in ("math", "algo", "prog", "avg"):
            raise ValueError("Invalid subject")
        self.students.sort(key=lambda s: getattr(s, subject), reverse=True) 


if __name__ == "__main__":
    n_students = int(input().strip())
    students = StudentManager.generate_students(n_students)
    print("1. Print list of students with upper case names")
    students.print_list(Student.get_upper_name)
    print("\n\n")
    print("2. Print list of students with lower case names")
    students.print_list(Student.get_lower_name)
    print("\n\n")
    print("3. Print list of students with standardized names")
    students.print_list(Student.get_standardized_name)
    print("\n\n")
    print("4. Print list of students with sorted names")
    students.sort_by_name()
    students.print_list(Student.get_standardized_name)
    print("\n\n")
    print("5. Print list of students with sorted home towns")
    students.sort_by_home()
    students.print_list(Student.get_standardized_name)
    print("\n\n")
    print("6. Print list of students with sorted math scores")
    students.sort_by_score("math")
    students.print_list(Student.get_standardized_name)
    print("\n\n")
    print("7. Print list of students with sorted algorithm scores")
    students.sort_by_score("algo")
    students.print_list(Student.get_standardized_name)
    print("\n\n")
    print("8. Print list of students with sorted programming scores")
    students.sort_by_score("prog")
    students.print_list(Student.get_standardized_name)
    print("\n\n")
    print("9. Print list of students with sorted average scores")
    students.sort_by_score("avg")
    students.print_list(Student.get_standardized_name)
    print("\n\n")
    