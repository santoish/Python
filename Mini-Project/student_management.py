student_details = []

def add_student(id, name):

    def add_details(id, name):
        student = {
            'ID': id,
            'Name': name
        }
        student_details.append(student)
        print(f'{name} details Added')

    id_exist = False

    if not student_details:
        add_details(id, name)
    else:
        for student in student_details:
            if student['ID'] == id:
                id_exist = True
                break
        
        if id_exist:
            print(f'{name} Details Exist')
        else:
            add_details(id,name)
    
    # print(student_details)

def view_students():
    if not student_details:
        print('No Records')

    else:
        print(f'\nSTUDENTS DETAILS\n')
        for student in student_details:      #make table format
            print(f'Student ID : {student["ID"]}')
            print(f'Student Name : {student["Name"]}')

def update_student(id):
    if not student_details:
        print('No Records')
    else:

        id_exist = False

        for student in student_details:
            if student["ID"] == id:
                print(f'Current Details')
                print(student)
                id_exist = True
                field = input('What do you want to Change (ID / Name) ? ').lower()
                if field == 'name':
                    new_name = input('Enter New Name : ')
                    student['Name'] = new_name
                elif field == 'id':
                    new_id = input('Enter New ID : ')
                    student['ID'] = new_id
                print(f'{student} Details Updated')

        if not id_exist:
            print('Student with given ID not Found')


def delete_student(id):
    id_exist = False

    for student in student_details:
        if student["ID"] == id:
            confirm_msg = input('Do You Want to Delete this Student Details (y to delete): ').lower()
            
            if confirm_msg == 'y':
                student_details.remove(student)
            
            id_exist = True

    if not id_exist:
        print('Student with given ID not Found')


def exit_menu():
    print('Thank You..')


def menu():
    print('\nSTUDENT MANAGEMENT SYSTEM\n')
    print('1.Add New Student')
    print('2.Update Student')
    print('3.View Student')
    print('4.Delete Student')
    print('5.Exit Menu')

while (True):
    menu()
    choice = input('Enter Choice (q to  Quit): ')
    if int(choice) == 1:
        student_id = int(input('Enter Student ID : '))
        student_name = input('Enter Student Name : ')
        add_student(student_id,student_name)
    
    elif int(choice) == 2:
        student_id = int(input('Enter Student ID to Update : '))
        update_student(student_id)

    elif int(choice) == 3:
        view_students()

    elif int(choice) == 4:
        student_id = int(input('Enter Student ID to Delete : '))
        delete_student(student_id)

    elif int(choice) == 5:
        exit_menu()
        break

    elif choice == 'q':
        exit_menu()
        break

    else:
        print('Invalid Options')
