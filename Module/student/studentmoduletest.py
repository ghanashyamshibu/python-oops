#this python file is used to test the student class
#in future we will use this in real senerio like login/regisrtation and other functionality

from student import studentclass


# step 1: student registration test

email = input("Enter your email: ")
password = input("Enter your password: ")       

s1 = studentclass()
s1.setUserNameAndPassword(email, password)