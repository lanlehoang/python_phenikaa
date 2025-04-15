import numpy as np
import uuid

# Student related constants
ID_LENGTH = 8
PROVINCES = ["Hà Nội", "Thái Bình", "Nam Định", "Hải Phòng", "Hải Dương"]
# Score ranges
MIN_SCORE = 4
MAX_SCORE = 10
# Surnames and first names
SURNAMES = [
    "Nguyễn", "Trần", "Lê", "Phạm", "Phan", "Bùi",
    "Huỳnh", "Võ", "Đặng", "Vũ", "Ngô", "Trương"
]
FEMALE_NAMES = [
    "Khánh Linh", "Bảo Ngọc", "Thùy Trang", "Thu Hương", "Hồng Nhung", "Tường Vy",
    "Ngọc Anh", "Thanh Hà", "Minh Châu", "Mai Phương", "Anh Thư", "Phương Nhi",
    "Tú Uyên", "Lan Chi", "Ngọc Ánh", "Ngọc Mai", "Hạ Vy", "Quỳnh Như",
    "Thu Giang", "Kim Ngân", "Thùy Dung", "Diệp Anh", "Hải Yến", "Hà My",
    "Bảo Linh", "Hà Phương", "Minh Trang", "Thùy Linh", "Minh Ngọc", "Thúy Nga"
]
MALE_NAMES = [
    "Minh Khoa", "Anh Duy", "Quốc Huy", "Đức Minh", "Hoàng Phúc", "Tuấn Kiệt",
    "Thành Đạt", "Nhật Minh", "Trung Hiếu", "Quốc Đạt", "Đức Anh", "Thành Công",
    "Khánh Duy", "Hải Đăng", "Ngọc Hưng", "Nam Khánh", "Đăng Khoa", "Quang Huy",
    "Tuấn Anh", "Đình Quân", "Chí Công", "Thái Sơn", "Gia Hưng", "Hoàng Lân",
    "Mạnh Dũng", "Hải Dương", "Hùng Mạnh", "Hoàng Việt", "Hoàng Phú", "Tiến Nam"
]
LENGTH_DISTRIBUTION = {
    2: 0.1,
    3: 0.7,
    4: 0.2
}


class StudentGenerator:
    @staticmethod
    def generate_student_id():
        return "PKA-" + str(uuid.uuid4())[:ID_LENGTH].upper()

    @staticmethod
    def generate_name_and_gender():
        # Generate 2, 3, and 4 letter names
        name_length = np.random.choice(
            list(LENGTH_DISTRIBUTION.keys()),
            p=list(LENGTH_DISTRIBUTION.values())
        )
        # Generate the surname first (common for all cases)
        surname = np.random.choice(SURNAMES)
        name = surname + " "
        # Generate name based on gender
        g = np.random.rand()   # 0 for Male, 1 for Female
        if name_length == 2:    # 2 letter names
            if g < 0.5:
                gender = 'M'
                first_name = np.random.choice(MALE_NAMES).split()[-1]
            else:
                gender = 'F'
                first_name = np.random.choice(FEMALE_NAMES).split()[-1]
        elif name_length == 3:  # 3 letter names
            if g < 0.5:
                gender = 'M'
                first_name = np.random.choice(MALE_NAMES)
            else:
                gender = 'F'
                first_name = np.random.choice(FEMALE_NAMES)
        else:   # 4 letter names
            if g < 0.5:
                gender = 'M'
                # A different approach for 4 letter male names
                surname2 = np.random.choice(SURNAMES)
                # Ensure the second surname is different from the first
                while surname2 == surname:
                    surname2 = np.random.choice(SURNAMES)
                first_name = surname2 + " " + np.random.choice(MALE_NAMES)
            else:
                # For 4 letter female names, adding "Thị" is the simplest approach
                gender = 'F'
                first_name = "Thị " + np.random.choice(FEMALE_NAMES)
        # Concatenate the name
        name += first_name
        return name, gender

    @staticmethod
    def generate_home():
        return np.random.choice(PROVINCES)

    @staticmethod
    def generate_score():
        return np.random.uniform(MIN_SCORE, MAX_SCORE)
