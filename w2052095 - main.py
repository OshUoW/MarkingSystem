# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
#Name - Adikaramage Don Oshani Dineshi Jayawardena
# Student ID IIT: 20220802     UOW ID= w2052095
# Date: 10/12/2023 

#Modules used in this code
from graphics import *

#Intializing variables used in this code
user_prompt=0
prog_result=0
user_defer=0
user_pass=0
user_fail=0
tot_result=0
tot_progress=0
tot_trailer=0
tot_retriever=0
tot_exclude=0
tot_students=0
height_progress=0
height_trailer=0
height_retriever=0
height_exclude=0
win=0
error=0
end=True
msg_state=True
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
    global new_value
    while True:
        if value not in [0,20,40,60,80,100,120]:
            print("Out of range")
            value=check_integer("Re-enter input: ")
        else:
            new_value=value
            return value

#Function to check if the total of inputs are equalled to 120   
def check_tot(user_pass,user_defer,user_fail):
    global tot_students
    if user_pass+user_defer+user_fail!=120:
        tot_students-=1
        raise ValueError("Total incorrect") 
    else:
        return ""

#Function to calculate the count of all progressions
def progression_count(prog_result):
    global tot_progress,tot_trailer,tot_retriever,tot_exclude
    if prog_result=="Progress":
        tot_progress +=1
    elif prog_result=="Progress (module trailer)":
        tot_trailer+=1
    elif prog_result=="Module retriever":
        tot_retriever+=1
    elif prog_result=="Exclude":
        tot_exclude+=1

#Histogram
def draw_histogram():
    global win,tot_progress,tot_trailer,tot_retriever,tot_exclude,tot_students,height_retriever,height_exclude,height_progress,height_trailer

    win = GraphWin("Histogram", 400, 450)
    title = Text(Point(80, 24), 'Histogram Results')
    title.draw(win)

    box = Rectangle(Point(24, 280), Point(96, height_progress)) 
    box.setFill("light green")
    txt_p = Text(Point(58, 295), 'Progress')
    txt_p.draw(win)
    box.draw(win)

    box = Rectangle(Point(106, 280), Point(178, height_trailer)) 
    box.setFill("sky blue")
    txt_t = Text(Point(140, 295), 'Trailer')
    txt_t.draw(win)
    box.draw(win)

    box = Rectangle(Point(188, 280), Point(260, height_retriever)) 
    box.setFill("green")
    txt_r = Text(Point(223, 295), 'Retriever')
    txt_r.draw(win)
    box.draw(win)

    box = Rectangle(Point(270, 280), Point(342, height_exclude)) 
    box.setFill("pink")
    txt_r = Text(Point(305, 295), 'Exclude')
    txt_r.draw(win)
    box.draw(win)

    txt_t = Text(Point(80, 350), f"{tot_students}  outcomes in total ")
    txt_t.draw(win)
    win.getMouse()
    win.close()
    
def contine_or_exit(msg):
    global height_progress,height_trailer,height_retriever,height_exclude,prog_list
    while True:  
        if msg=='q':  
            #Creating the variables to obtain the heights of the rectangles in the histogram
            height_progress=(280-(tot_progress*10))
            height_trailer=(280-(tot_trailer*10))
            height_retriever=(280-(tot_retriever*10))
            height_exclude=(280-(tot_exclude*10))
            draw_histogram() 
            end=False         
            exit()
        elif msg=="y":
            break
        else:
            msg_state==False
            msg=input("Invalid entry.Enter 'y' for yes or 'q' to quit and view results:").lower()

#Code body    
while end==True:
    print("Are you a student or staff?")
    entry=input("Enter 'student' or 'staff' to continue : ").lower()
    if entry=='student':
        #STUDENT SECTION
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

            elif user_pass == 100:
                prog_result="Progress (module trailer)"

            elif user_fail >=80:
                prog_result="Exclude" 

            elif user_pass<100 and user_pass>=0:
                prog_result="Module retriever"

            else:
                prog_result=""
            print(prog_result)
        break

    elif entry=='staff':
        #STAFF SECTION
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
                    continue
                        
                print(prog_result)
            progression_count(prog_result)
            tot_students+=1

            print("Would you like to enter another set of data? ")
            msg=input("Enter 'y' for yes or 'q' to quit and view results:").lower()
            contine_or_exit(msg)
            continue
            
    else:
        print("Invalid Entry. Try again")

# REFERENCES
# fstrings - https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
# .isdigit() - https://www.geeksforgeeks.org/python-string-isdigit-method/
#date-time - https://docs.python.org/3/library/datetime.html




