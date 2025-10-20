# 42-NguyenThiNgocTram.py
# Ứng dụng Quản lý Sinh viên

# Danh sách để lưu thông tin các sinh viên.
# Mỗi sinh viên là một dictionary.
student_list = []

def add_student(name, year_of_birth, address):
    """
    YÊU CẦU 1: Hoàn thiện hàm này.
    - Tạo một dictionary để lưu thông tin sinh viên.
    - Thêm dictionary đó vào danh sách `student_list`.
    - In ra thông báo "Da them sinh vien <ten> thanh cong."
    """
    student = {
        "name": name,
        "year_of_birth": year_of_birth,
        "address": address
    }
    student_list.append(student)
    print(f"Da them sinh vien {name} thanh cong.")


def print_student_list():
    """
    YÊU CẦU 2: Hoàn thiện hàm này.
    - In ra tiêu đề "--- DANH SACH SINH VIEN ---".
    - Nếu danh sách trống, in ra "Danh sach trong.".
    - Nếu không, duyệt qua `student_list` và in thông tin mỗi sinh viên.
    """
    print("--- DANH SACH SINH VIEN ---")
    if not student_list:
        print("Danh sach trong.")
    else:
        for student in student_list:
            print(f" - Ten: {student['name']}, Nam sinh: {student['year_of_birth']}, Dia chi: {student['address']}")


def search_student(search_name):
    """
    YÊU CẦU 3: Hoàn thiện hàm này.
    - In ra tiêu đề "--- KET QUA TIM KIEM ---".
    - Tìm kiếm tên (không phân biệt hoa thường).
    - In ra thông tin nếu có, ngược lại in "Khong tim thay sinh vien nao.".
    """
    print("--- KET QUA TIM KIEM ---")
    found = []
    for student in student_list:
        if search_name.lower() in student["name"].lower():
            found.append(student)

    if not found:
        print("Khong tim thay sinh vien nao.")
    else:
        for student in found:
            print(f" - Ten: {student['name']}, Nam sinh: {student['year_of_birth']}, Dia chi: {student['address']}")


# --- Phần thực thi chính để kiểm tra ---
if __name__ == "__main__":
    print("--- CHUONG TRINH QUAN LY SINH VIEN ---")

    # Yêu cầu 1: Thêm sinh viên
    print("\n1. Them sinh vien:")
    add_student("Nguyen Van An", 2003, "Da Nang")
    add_student("Tran Thi Binh", 2002, "Quang Nam")
    add_student("Le Van Hung", 2003, "Hue")

    # Yêu cầu 2: In danh sách
    print("\n2. In danh sach sinh vien:")
    print_student_list()

    # Yêu cầu 3: Tìm kiếm
    print("\n3. Tim kiem sinh vien theo ten 'an':")
    search_student("an")

    print("\nTim kiem sinh vien theo ten 'Dung':")
    search_student("Dung")