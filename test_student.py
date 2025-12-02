from student import student_registration_details

def test_student_details():
    expected_output=(
        "Student ID:323\n"
        "Student Name:Bhagya\n"
        "Course:BCA\n"
        "Academic Year:2024-2025"
    )
    assert student_registration_details("323","Bhagya","BCA","2024-2025")==expected_output
