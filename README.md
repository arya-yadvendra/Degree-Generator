# Degree-Generator

Author:-
    YADVENDRA YADAV   DU(MCA)

Supervised by:-
    DR. BHARTI RANA (ASST. PROFESSOR, DEPT. OF COMP. SCIENCE, UNIVERSITY OF DELHI)
    
    COMPLETION DATE: March 16,2023

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
