#this python file is used to test the student class
#in future we will use this in real senerio like login/regisrtation and other functionality

from student import studentclass


# step 1: student registration test

email = input("Enter your email: ")
password = input("Enter your password: ")       

s1 = studentclass()
s1.setUserNameAndPassword(email, password)


# step 2: student primary information test


Full_name = input("Enter your full name: ")
date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
age = input("Enter your age: ")
mobile_number = input("Enter your mobile number: ")
preferred_language = input("Enter your preferred language: ")
school_college_name = input("Enter your school/college name: ")
class_grade = input("Enter your class/grade: ")
academic_year = input("Enter your academic year: ")


s1.setPrimaryInformation(
    full_name=Full_name,
    date_of_birth=date_of_birth,
    age=age,
    mobile_number=mobile_number,
    preferred_language=preferred_language,
    school_college_name=school_college_name,
    class_grade=class_grade,
    academic_year=academic_year
)