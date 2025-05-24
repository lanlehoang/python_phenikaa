from person_classes import *
from typing import List
from utils.sorters import *


class Class:
    def __init__(self, name: str, homeroom_teacher: Lecturer, students: List[Student]):
        self.name = name
        self.homeroom_teacher = homeroom_teacher
        self.students = self._sort_students(students)

    def _sort_students(students):
        return sorted(students, key=lambda x: [get_vi_name_key(x.name), get_date_key(x.birthday)])
    
    def self_introduce(self):
        print(
            f"Lớp: {self.name}"
            f"\nGVCN: {self.homeroom_teacher.name}"
            f"\nSĩ số:{len(self.students)}"
            f"\nSố học sinh nam: {sum(1 for s in self.students if s.sex.lower == 'nam')}"
            f"\nSố học sinh nữ: {sum(1 for s in self.students if s.sex.lower == 'nữ')}"
        )
    

class School:
    def __init__(self, name: str, classes: List[Class]):
        self.name = name
        self.classes = classes

    def self_introduce(self):
        print(
            f"Trường: {self.name}"
            f"\nSố lớp học: {len(self.classes)}"
        )