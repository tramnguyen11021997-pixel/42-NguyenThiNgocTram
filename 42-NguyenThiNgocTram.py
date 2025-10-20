# 42-NguyenThiNgocTram.py
# Ứng dụng Quản lý Sinh viên

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


if __name__ == "__main__":
    print("--- CHUONG TRINH QUAN LY SINH VIEN ---")
    print("\n1. Them sinh vien:")
    add_student("Nguyen Van An", 2003, "Da Nang")
    add_student("Tran Thi Binh", 2002, "Quang Nam")
    add_student("Le Van Hung", 2003, "Hue")



def print_student_list():
    print("--- DANH SACH SINH VIEN ---")
    if not student_list:
        print("Danh sach trong.")
    else:
        for student in student_list:
            print(f" - Ten: {student['name']}, Nam sinh: {student['year_of_birth']}, Dia chi: {student['address']}")


def search_student(search_name):
    print("\n--- KẾT QUẢ TÌM KIẾM ---")
    found = []

    for student in student_list:
        if search_name.lower() in student['name'].lower():
            found.append(student)

    if not found:
        print("Không tìm thấy sinh viên nào.")
    else:
        for student in found:
            print(f"→ Tên: {student['name']}, Năm sinh: {student['year_of_birth']}, Địa chỉ: {student['address']}")


if __name__ == "__main__":
    print("\n--- CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN ---")

    # Yêu cầu 1: Thêm sinh viên
    add_student("Nguyen Van An", 2003, "Da Nang")
    add_student("Tran Thi Binh", 2002, "Quang Nam")
    add_student("Le Van Hung", 2003, "Hue")

    # Yêu cầu 2: In danh sách sinh viên
    print("\nDanh sách sinh viên:")
    print_student_list()

    # Yêu cầu 3: Tìm kiếm sinh viên
    print("\nKết quả tìm kiếm theo tên 'an':")
    search_student("an")
