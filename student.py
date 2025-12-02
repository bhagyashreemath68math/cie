def student_registration_details(student_id, name, course, academic_year):
    result = (
        f"Student ID      : {student_id}\n"
        f"Student Name    : {name}\n"
        f"Course          : {course}\n"
        f"Academic Year   : {academic_year}\n"
    )
    return result


if __name__ == "__main__":
    student_id = "323"
    name = "Bhagya"
    course = "BCA"
    academic_year = "2024-2025"

    print(student_registration_details(student_id, name, course, academic_year))
