# 2 i)
# student details
student_name = 'Gloria Arinda'
student_number = 'SEP23/BCS/088U/F'
programming = 90
data_science = 87
computer_application = 77
#average mark and print the ans in 3dps
total=programming+data_science+computer_application
print(total)
number_of_subjects = 3
average_mark = total/number_of_subjects
print(average_mark)


# 2 ii)
#MPG=miles driven/gallonsof gas used
# MPG stands for miles per gallons used
milesdriven=float(input("Enter milesdriven: "))
gallon_used=float(input("Enter the gallon_used: "))
MPG =milesdriven /gallon_used
print(f"{MPG}")


# 2 iii)
#print all numbers from 1 to 100 and shldnt be divisible by 2

for num in range(1, 100):  
    if num % 2 != 0:      
        print(num)
