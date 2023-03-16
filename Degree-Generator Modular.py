
'''Degree generator: A modular and menu-driven program in Python to generate Marksheets and degrees:
*** menu-options:
1. To generate a degree in bulk
2. To include Corrections in a degree
3. To view a degree
4. To exit from execution

It contain the following modules:
1. myDegreeGenerator: A module that accept a text filename containing the 
    Name of the student, Roll Number, Course Name, year of award and percentage of the students,
    like in File 'degreeData.txt' and generates the degree of the students. 
    The format of the degree is in degreeTemplate.txt. 
    The degrees are saved in a text file with the Students' name and roll number.
2. myDegreeCorrector: A module to include correction(s) in the degree file. 
    It accept a text file containing the degree and make corrections as per the user's input.
    Display a menu to ask the user to make corrections in the degree.
    Also user can also ask for further correction in degree. 
3. myDegreeViewer: A module to view a degree. It accepts a filename containing a degree and displays the degree.

Variables that are used in this modular:
    con(continue), choice, degree_name, temp, 
    myDegreeGenerator module-( lines, count, s_name, roll_no, program_name, year, percentage, degree)
    myDegreeCorrector module-( degree_name, file_data, roll_no, prev_name, con(continue), choice, new_name, new_filename,
        new_programme, file_name, data, new_year, new_per)
    myDegreeViewer module-( degree_name,degree)


Author:-
    YADVENDRA YADAV   DU(MCA)

Supervised by:-
    DR. BHARTI RANA (ASST. PROFESSOR, DEPT. OF COMP. SCIENCE, UNIVERSITY OF DELHI)
    
    COMPLETION DATE: March 16,2023
    CODE EDITOR :- Visual Studio Code

'''



import os                                               # import module for operating system tasks
from datetime import date                               # import module for datetime


# Template getter method definition
def tempGetter():
    # DegreeTemplate file opened in read mode
    with open("degreeTemplate.txt","r") as filehandler:
        temp = filehandler.read()
        return temp
    



# Degree generator method/function definition
def myDegreeGenerator():

    # Opening of file in read mode to get data line by line
    with open("degreeData.txt", "r") as file1:
        lines = file1.readlines()[2:]                   # assigning readed data(line-by-line) after 2nd line

        # print(lines) prints line in continous
        # Intiating count to specify line(indexing)
        count = 0

        # Looping through lines to assign specific values to records
        for line in lines:
            count+=1
            
            # Unpacking of values of particular line for every student data
            s_name,roll_no,program_name,year,percentage = line.strip().split(",")
            # slicing roll no to remove whitespace in starrting of roll_no
            roll_no=roll_no[1:]                                                   
            
            # Replacing placeholders in template with particular student record
            degree = tempGetter().replace("<Student Name>",s_name).replace("<Name of Programme>",program_name).replace("<Year>",year).replace("<Percentage>",percentage).replace("<date of creation>",date.today().strftime("%d %m %y"))
            

            # Creating individual txt format file of degree for every student
            with open(f"{s_name}_{roll_no}.txt","w") as degreefilehandler:
                degreefilehandler.write(degree)
                print(f"Degree text file Generated for Student:{s_name}\t&\tRoll no:{roll_no}")
            
        



# Degree corrector method definition to make corretions on particular student data file
def myDegreeCorrector(degree_name):
    
    #Opening given name text file (degree_name) to read file
    with open(f"{degree_name}.txt","r") as filehandler:
        file_data=filehandler.read()
        print("\n")
        print(file_data)                                            
    
    # Fetching roll no. and Name of student from given degree file
    roll_no = degree_name[-5:]
    prev_name = degree_name.split("_")[0]


    # Confirmation on entering to particular file
    print(f"You are viewing degree : {degree_name}")
     
    # Giving menu options for every operation that is to be executable in myDegreeCorrector method
    print("\n\n****** Menu correction options *******")
    print("1. To perform corrections on Name fo student:")      
    print("2. To perform corrections on Programme:")
    print("3. To perform correction on year of passing:")
    print("4. To perform correction on percentage bagged by student:")
    print("5. To exit from correction window")
    
    # continue variable to compare for further more operation or not
    con = "y"
    while (con=="y" or con=="Y"):
        
        # Taking input choice to select of following opeartion to be performed
        choice = int(input("Enter the choice no. which operation you want to perform: "))

        # First condition statement for correction of Name of student
        if choice==1:                                                                           

            new_name = input("Enter the correct name:")                     # Taking correct Name input from user
            file_data =  file_data.replace(prev_name,new_name)              # Replacing correct Name with previous name in degree file
            
            # Updating previous local variable to continuation operation on same file with updated file name
            prev_name = new_name                                                                

            # Renaming file with updated name with concatinating format of file
            degree_name = f"{degree_name}.txt"
            new_filename = f"{new_name}_{roll_no}.txt"
            os.rename(degree_name,new_filename)
            with open(new_filename,"w") as f:
                f.write(file_data)
            
        
        # Second condition statement for correction of Programme name in degree
        if choice==2:
            # Taking New(Correct) programme name from user
            new_programme = input(f"Enter the correct programme name for {prev_name}: ")

            file_name = f"{prev_name}_{roll_no}.txt"

            # Opening files to read data line by line to replace programme name 
            with open(file_name,"r") as f:
                data = f.readlines()
                data[5] = f" {new_programme}\n"                  #assigning Correct programme name with particular index of line(programme name)

            # Overwriting data of file with updated data
            with open(file_name,"w") as f:
                f.writelines(data)


        # Third condition statement for correction of year of passing for student
        if choice==3:
            new_year = input(f"Enter the correct year of passing for {prev_name}:")
            # Opening files to read data line by line to replace year of passing 
            with open(file_name,"r") as f:
                data = f.readlines()
                data[7] = f" {new_year}\n"                       #assigning correct year of passing in list of line for particular indexed line to update data
            # Overwriting data of file with updated data
            with open(file_name,"w") as f:
                f.writelines(data)
                 
        
        # Fourth condition statement for correction of Percentage of student
        if choice==4:
            new_per = float(input(f"Enter the correct percentage for {prev_name}:"))
            
            # Exception raising if input percentage is not possible (should be greater than 0% and less than 100%)
            if (new_per<0 and new_per>100):
                raise Exception("Sorry, Input percentage is Invalid") 
            
            # Opening files to read data line by line to replace percentage
            with open(file_name,"r") as f:
                data = f.readlines()
                data[9] = f" {new_per}% of marks.\n"            #assigning correct percentage in list of line for particular indexed line to update data
            
            # Overwriting data of file with updated data
            with open(file_name,"w") as f:
                f.writelines(data)

        # Fourth condition statement to exit from the myDegreeGenerator method 
        if choice==5:
            break
        
        else:
            pass

        # Taking continuation input to compare with while condition
        con = input("Did you want to perform further corrections(y/n): ")
        



        
# myDegreeViewer method definition to show specific student degree with passing degreeName as argument
def myDegreeViewer(degree_name):
    with open(f"{degree_name}.txt","r") as filehandler:             #opening of degree_name file in read mode to display degree
        degree = filehandler.read()                                 #calling read function
    print("\n ",degree)                                             #printing given filename (degree)




#Driver code to providing menu of operations to be performed on givem Data Operations depending on choices as follows:
#1. Generating of degree for every student mentioned in data-file
#2. To perform correction on individual student degree file and also reflect back on data-file
#3. Taking input file name of individual student to view degree
#4. Terminating the execution

con="y"
while(con=="y" or con=="Y"):
    print("********** OPTIONS **********")
    print("Press:1 - To generate degree in bulk ")
    print("Press:2 - To make correction in a degree ")
    print("Press:3 - To view a degree ")
    print("Press:4 - Exit ")
    
    # To caught (selection input bound) runtime error 
    try:
        choice = int(input("\nEnter the choice of operation which you want to perform: "))

        if choice==1:
            myDegreeGenerator()                                         #calling myDegreeGenerator function
        

        elif choice==2:
            # try block to check wether given input degree_name exists or not
            try:
                degree_name = input("Enter the degree name on which you want to perform corrections: ")   
                myDegreeCorrector(degree_name)
            
            # Handling Exception if file not exists
            except FileNotFoundError:   
                print("ERROR:, There is no such file")  
        

        elif choice==3:
            # try block to check wether given input degree_name exists or not
            try:
                degree_name = input("Enter the degree name, you want to view : \n")
                myDegreeViewer(degree_name)
            
            # Handling Exception if file not exists
            except FileNotFoundError as e:
                print("ERROR:",e)
        
        
        elif choice==4:
            break                       # Conditional Statement to exit from execution of program

        else:                           # Conditional Statement to print wrong choice for (base 10) other numerical choice 
            print("***** Wrong Choice *****")
        

        print("\nDo you want to continue with more operations : y/n ")
        con = input()                   # Taking continue variable to compare with while condition, wether user want to continue or not

    # Exception Handling for invalid input of selection of choice operation (other than number input)
    except ValueError:
        print("ERROR: Invalid input...")
    