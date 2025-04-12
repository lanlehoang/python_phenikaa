import numpy as np
import uuid


class Student:
    def __init__(self, name, gender, home, math, algo, prog):
        self.id = str(uuid.uuid4())[:18]
        self.name = name
        self.gender = gender
        self.home = home
        self.math = round(math, 1)
        self.algo = round(algo, 1)
        self.prog = round(prog, 1)
        self.avg = round(sum([self.math, self.algo, self.prog])/3, 1)

    def get_upper_name(self):
        return self.name.upper()
    
    def get_lower_name(self):
        return self.name.lower()
    
    def get_standardized_name(self):
        name = self.name.split()
        name = [n.capitalize() for n in name]
        return " ".join(name)
    
    def get_western_name(self):
        full_name = self.name.split()
        return full_name[-1] + " " + " ".join(full_name[:-1])
    
    def print_student_info(self, name_type):
        print(
            f"{self.id:<19} {name_type:<30} {self.gender:<6} "
            f"{self.home:<15} {self.math:<5} {self.algo:<5} "
            f"{self.prog:<5} {self.avg:<5}"
        )
    

class StudentManager:
    def __init__(self, n_students):
        self.students = []
        self.n_students = n_students

        def generate_names_and_gender():
            # Define constants
            SURNAMES = ["Nguyễn", "Trần", "Lê", "Phạm", "Phan", "Bùi", "Huỳnh", "Hoàng"]
            FEMALE_NAMES = [
                "Khánh Linh", "Bảo Ngọc", "Thùy Trang", "Thu Hương", "Hồng Nhung", "Tường Vy",
                "Ngọc Anh", "Thanh Hà", "Minh Châu", "Mai Phương", "Anh Thư", "Phương Nhi",
                "Tú Uyên", "Lan Chi", "Hoài An", "Trúc Linh", "Hạ Vy", "Quỳnh Như",
                "Thu Giang", "Kim Ngân", "Bích Phượng", "Diệp Anh", "Hải Yến", "Hà My"
            ]
            MALE_NAMES = [
                "Minh Khoa", "Anh Duy", "Quốc Huy", "Gia Bảo", "Hoàng Phúc", "Tuấn Kiệt",
                "Thành Đạt", "Nhật Minh", "Trung Hiếu", "Hoàng Nam", "Đức Anh", "Bảo Long",
                "Khánh Duy", "Hải Đăng", "Ngọc Hưng", "Nam Khánh", "Đăng Khoa", "Tấn Phát",
                "Tuấn Anh", "Đình Quân", "Chí Công", "Thái Sơn", "Gia Hưng", "Hoàng Lân"
            ]
            LENGTH_DISTRIBUTION = [0.15, 0.6, 0.25] # Probability of #2 #3 #4
            LENGTH_NUMS = [int(dist*self.n_students) for dist in LENGTH_DISTRIBUTION[:-1]]
            LENGTH_NUMS.append(self.n_students - sum(LENGTH_NUMS))
            # Generate names
            names = []
            genders = []
            # 2 letter names
            for _ in range(LENGTH_NUMS[0]):
                name = np.random.choice(SURNAMES) + " "
                g = np.random.rand()   # 0 for Male, 1 for Female
                if g < 0.5:
                    gender = 'M'
                    first_name = np.random.choice(MALE_NAMES).split()[-1]
                else:
                    gender = 'F'
                    first_name = np.random.choice(FEMALE_NAMES).split()[-1]
                name += first_name
                names.append(name)
                genders.append(gender)
            # 3 letter names
            for _ in range(LENGTH_NUMS[1]):
                name = np.random.choice(SURNAMES) + " "
                g = np.random.rand()   # 0 for Male, 1 for Female
                if g < 0.5:
                    gender = 'M'
                    first_name = np.random.choice(MALE_NAMES)
                else:
                    gender = 'F'
                    first_name = np.random.choice(FEMALE_NAMES)
                name += first_name
                names.append(name)
                genders.append(gender)
            # 4 letter names
            for _ in range(LENGTH_NUMS[1]):
                name = np.random.choice(SURNAMES) + " "
                g = np.random.rand()   # 0 for Male, 1 for Female
                if g < 0.5:
                    gender = 'M'
                    first_name = "Văn " + np.random.choice(MALE_NAMES)
                else:
                    gender = 'F'
                    first_name = "Thị " + np.random.choice(FEMALE_NAMES)
                name += first_name
                names.append(name)
                genders.append(gender)
            return names, genders
        
        def generate_home():
            PROVINCES = ["Hà Nội", "Thái Bình", "Nam Định", "Hải Phòng", "Hải Dương"]
            return [np.random.choice(PROVINCES) for _ in range(self.n_students)]
        
        def generate_scores():
            return np.random.uniform(4, 10, self.n_students)
        
        names, genders = generate_names_and_gender()
        home = generate_home()
        math_scores = generate_scores()
        algo_scores = generate_scores()
        prog_scores = generate_scores()

        for i in range(self.n_students):
            self.students.append(
                Student(names[i], genders[i], home[i],
                        math_scores[i], algo_scores[i], prog_scores[i])
            )

    def print_header(self):
        print(
            f"{'ID':<19} {'Name':<30} {'Gender':<6} {'Home':<15} "
            f"{'Math':<5} {'Algo':<5} {'Prog':<5} {'Avg':<5}"
        )
        print("-" * 95)

    def print_list_upper(self):
        self.print_header()
        for student in self.students:
            student.print_student_info(student.get_upper_name())

    def print_list_lower(self):
        self.print_header()
        for student in self.students:
            student.print_student_info(student.get_lower_name())

    def print_list_standardized(self):
        self.print_header()
        for student in self.students:
            student.print_student_info(student.get_standardized_name())

    def print_sorted_names(self):
        self.print_header()
        for student in sorted(self.students, key=lambda s: s.get_western_name()):
            student.print_student_info(student.get_standardized_name())

    def print_sorted_home(self):
        self.print_header()
        for student in sorted(self.students, key=lambda s: s.home):
            student.print_student_info(student.get_standardized_name())

    def print_sorted_score(self, subject):
        if subject not in ("math", "algo", "prog", "avg"):
            raise ValueError("Invalid subject")
        self.print_header()
        for student in sorted(self.students, key=lambda s: getattr(s, subject), reverse=True):
            student.print_student_info(student.get_standardized_name())         


if __name__ == "__main__":
    n_students = int(input().strip())
    students = StudentManager(n_students)
    print("1. Print list of students with upper case names")
    students.print_list_upper()
    print("\n\n")
    print("2. Print list of students with lower case names")
    students.print_list_lower()
    print("\n\n")
    print("3. Print list of students with standardized names")
    students.print_list_standardized()
    print("\n\n")
    print("4. Print list of students with sorted names")
    students.print_sorted_names()
    print("\n\n")
    print("5. Print list of students with sorted home towns")
    students.print_sorted_home()
    print("\n\n")
    print("6. Print list of students with sorted math scores")
    students.print_sorted_score("math")
    print("\n\n")
    print("7. Print list of students with sorted algorithm scores")
    students.print_sorted_score("algo")
    print("\n\n")
    print("8. Print list of students with sorted programming scores")
    students.print_sorted_score("prog")
    print("\n\n")
    print("9. Print list of students with sorted average scores")
    students.print_sorted_score("avg")
    print("\n\n")
    