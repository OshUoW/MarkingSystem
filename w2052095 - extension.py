# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
#Name - Adikaramage Don Oshani Dineshi Jayawardena
# Student ID IIT: 20220802     UOW= w2052095
# Date: 6/12/2023 

#Modules used in this code
from datetime import *

#Intializing variables used in this code
credit_score=0
prog_result=0
user_defer=0
user_pass=0
user_fail=0
credits_allowed=0
save=0
msg_state=0
file_name=0
txt_file=0
read_file=0
new_value=0


#Intiliazing lists used in this project
prog_list=[]

#Function to check if all of the inputs entered are integer
def check_integer(user_prompt):
    while True:
        user_input=input(user_prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid Entry. Please enter an integer")

#Function to check if the inputs are within the range
def range_check(value):
    while True:
        global new_value
        if value not in [0,20,40,60,80,100,120]:
            print("Out of range")
            value=check_integer("Re-enter input: ")
        else:
            new_value=value
            return value

#Function to check if the total of inputs are equalled to 120   
def check_tot(user_pass,user_defer,user_fail):
    if user_pass+user_defer+user_fail!=120:
        raise ValueError("Total incorrect")
    else:
        return ""
    
def contine_or_exit(msg):
    while True:  
        if msg=='q':
            #Code snippet for the List Extension ( Part 2 )
            for elements in prog_list:
                print(f"{elements[0]} - {elements[1]}, {elements[2]}, {elements[3]}\n")   
           
            #Code snippet to write the marks to the file
            save=datetime.now()
            file_name=f"{save.year}_{save.month}_{save.day}_{save.hour}_{save.minute}.txt"
            file=open(file_name,'w')
            file.write("Mark Summary\n")
            for elements in prog_list:
                file.write(f"{elements[0]} - {elements[1]}, {elements[2]}, {elements[3]}\n")
            file.close()

            #Accessing the stored values using read mode
            read_file=open(file_name,'r')
            for line in read_file:
                print(line,end='')
            read_file.close()
            exit()

        elif msg=="y":
            break
        else:
            msg_state==False
            msg=input("Invalid entry.Enter 'y' for yes or 'q' to quit and view results:").lower()

#Code body    
while True:
    try:
        user_pass=check_integer("Enter number of credits at pass: ")
        range_check(user_pass)
        user_pass=new_value
        user_defer=check_integer("Enter number of credits at defer: ")
        range_check(user_defer)
        user_defer=new_value
        user_fail=check_integer("Enter number of credits at fail: ")
        range_check(user_fail)
        user_fail=new_value
        check_tot(user_pass,user_defer,user_fail)

    except ValueError as error:
        print(error)

    else:  
        if user_pass == 120 :
            prog_result="Progress" 
            prog_list.append([prog_result,user_pass,user_defer,user_fail])
                    

        elif user_pass == 100:
            prog_result="Progress (module trailer)"
            prog_list.append([prog_result,user_pass,user_defer,user_fail])

        elif user_fail >=80:
            prog_result="Exclude"
            prog_list.append([prog_result,user_pass,user_defer,user_fail])

        elif user_pass<100 and user_pass>=0:
            prog_result="Module retriever"
            prog_list.append([prog_result,user_pass,user_defer,user_fail])

        else:
            prog_result=""
        print(prog_result)
          

        print("Would you like to enter another set of data? ")
        msg=input("Enter 'y' for yes or 'q' to quit and view results:").lower()
        contine_or_exit(msg)
        continue
            


# REFERENCES
# fstrings - https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
# .isdigit() - https://www.geeksforgeeks.org/python-string-isdigit-method/



        


