import re
from datetime import datetime


class Person:
    def __init__(self, person_id: str, name: str, sex: str, birthday: str):
        self.person_id = person_id
        self.name = name
        if sex.lower() not in ["nam", "nữ"]:
            raise ValueError("Giới tính không hợp lệ")
        self.sex = sex.capitalize()
        if not re.match(r"\d{2}/\d{2}/\d{4}", birthday):
            raise ValueError("Ngày sinh không theo format dd/mm/yyyy")
        try:
            datetime.strptime(birthday, "%d/%m/%Y")
        except ValueError:
            raise ValueError(f"Ngày sinh {birthday} không tồn tại")
        self.birthday = birthday

    def self_introduce(self):
        print(f"Tôi là {self.name}, giới tính {self.sex}, sinh ngày {self.birthday}")


class Lecturer(Person):
    def __init__(self, person_id: str, name: str, sex: str, birthday: str, subject: str):
        super().__init__(person_id, name, sex, birthday)
        self.subject = subject

    def self_introduce(self):
        print(
            f"Tôi là {self.name}, giới tính {self.sex}, sinh ngày {self.birthday}, "
            f"dạy môn {self.subject}"
        )


class Student(Person):
    def __init__(
            self, person_id: str, name: str, sex: str, birthday: str,
            scr_math: float, scr_algo: float, scr_prog: float
    ):
        super().__init__(person_id, name, sex, birthday)
        self.scr_math = round(scr_math, 1)
        self.scr_algo = round(scr_algo, 1)
        self.scr_prog = round(scr_prog, 1)
        self.scr_avg = self._get_average()

    def _get_average(self):
        return round((self.scr_math + self.scr_algo + self.scr_prog)/3, 1)
    
    def self_introduce(self):
        print(
            f"Tôi là {self.name}, giới tính {self.sex}, sinh ngày {self.birthday}, "
            f"điểm môn Toán {self.scr_math}, "
            f"điểm môn Cấu trúc dữ liệu và giải thuật {self.scr_algo}, "
            f"điểm môn Lập trình {self.scr_prog}, "
            f"điểm trung bình {self.scr_avg}"
        )
    