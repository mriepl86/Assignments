### Assignment recapApp ###

# s123456_s00922587, YourLastname1_Riepl       ##TODO
# Implement a console-based Student Grades Manager.
# The program reads data from a CSV file, allows some data processing and summary operations, and writes results back to another file.

# ================================
# Task 1: File Reading
# ================================
"""
Reads the CSV file and returns a list of tuples (student_id, name, grade).
Handles file-not-found gracefully: Log the error to the console and return an empty list.
"""

def read_grades(filename):
    try: 
        with open(filename, "r") as datei:
            inhalt = datei.read()

        zeilen = inhalt.splitlines()

        liste  = []

        for i in zeilen:
            teile = i.split(";")

            student_id, name, grade = teile

            student_id = int(student_id)
            grade = int(grade)

            tupel = (student_id, name, grade)

            liste.append(tupel)

        return(liste)

    except FileNotFoundError:
        print("Datei nicht gefunden")
        return []
    return []

# ================================
# Task 2: Filtering and Transformations
# the parameter 'students' is a list
# ================================

def filter_passing(students):
    """
    Filters and returns students with grade >= 60.
    """
    return [i for i in students if i[2] >= 60]  

def to_name_grade_dict(students):
    """
    Converts list of tuples to a dictionary {name: grade}.
    """
    return {i[1]: i[2] for i in students}

def curve_grades(students, curve_by):
    """
    Returns a new list of tuples with grades increased by curve_by (max 100).
    """
    x=[]

    for i in students:
        student_id, name, grade = i
        
        if grade + curve_by <= 100:
            tupel = (student_id, name, grade + curve_by)
            x.append(tupel)
            
        else:
            tupel = (student_id, name, 100) #fixer Wert 100 im Tupel falls grade >95
            x.append(tupel)
            
    return x

# ================================
# Task 3: Summary Statistics
# ================================

def print_statistics(students):
    """
    Prints number of students, average grade, min, and max. Use the formatting in the example:
    Example:
    Number of students: 5
    Average grade: 82.6
    Lowest grade: 59 (David)
    Highest grade: 100 (Eve)

    """
    number = len(students)
    average = sum([i[2] for i in students]) / number
    low = min(students, key = lambda i: i[2])
    high = max(students, key = lambda i: i[2])

    print (f"Number of students: {number}\nAverage grade: {average}\nLowest grade: {low[2]} ({low[1]})\nHighest grade: {high[2]} ({high[1]})")
    


# ================================
# Task 4: File Writing
# ================================

def write_grades(filename, students):
    """
    Writes the list of student tuples back to a CSV file.
    Sort by name before writing.
    """

    students=sorted(students, key= lambda p: p[1])

    with open (filename, "w") as datei:
        for student_id, name, grade in students:
            datei.write(f"{student_id};{name};{grade}\n")
    
# ================================
# Task 5: Putting It All Together
# ================================

def main():
    # TODO: Implement program flow:
    # 1. Read file
    # 2. Print stats
    # 3. Filter failing
    # 4. Curve grades +5
    # 5. Print stats again
    # 6. Write curved grades
    
    students = read_grades("grades.csv")

    print_statistics(students)

    students_passed = filter_passing(students)          #ist das die richtige Funktion? Filter passing - Filter failing???

    students_passed_curved = curve_grades(students_passed, 5)

    print_statistics(students_passed_curved)

    write_grades("finalgrades.csv", students_passed_curved)

if __name__ == "__main__":
    main()
  

