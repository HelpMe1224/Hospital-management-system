from Doctor import Doctor
from Patient import Patient
 
class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """
 
        self.__username = "username"
        self.__password = "password"
        self.__address =  address
 
    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')
 
    def login(self) :
        """
        A method that deals with the logins
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin
 
        username = input('Enter the username: ')
        password = input('Enter the password: ')
 
        # check if the username and password match the registered ones
        #ToDo1
        return (username == self.__username and password == self.__password)
              
 
    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True
 
        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        first_name = input("Enter the first name:")
        surname = input ("Enter the surname:")
        speciality= input ("Enter the specialist:")
        return first_name, surname, speciality
        
 
    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """
 
        print("-----Doctor Management-----")
 
        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')
 
        op = input('Input: ')
        
 
        # register
        if op == '1':
            print("-----Register-----")
 
            # get the doctor details
            print('Enter the doctor\'s details:')
            first_name, surname, speciality = self.get_doctor_details()
            pass
 
            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    break
            else:
                    doctor = Doctor(first_name,surname, speciality)
                    doctors.append(doctor)
                    print("Doctor registered.")
                    
                    pass # save time and end the loop
 
            
            pass# add the doctor ...
                                                         # ... to the list of doctors
            print('Doctor registered.')
 
        # View
        elif op == '2':
            print("-----List of Doctors-----")
            print("ID     Fullname     Speciality ")
            self.view(doctors)
 
        # Update
        elif op == '3':
            while  True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("Doctor not found")
 
                    
                        # doctor_index is the ID mines one (-1)
                        
 
                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')
 
            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: ')) # make the user input lowercase
 
            if op ==1 :
                updated_first_name = input("Enter the new updated first name ")
                doctors[index].set_first_name(updated_first_name)
                print("First name updated successfully.")
 
            elif op == 2:
                updated_surname = input("Enter the new updated surname: ")
                doctors[index].set_surname(updated_surname)
                print("Surname updated successfully.")
 
            elif op == 3:
                updated_speciality = input("Enter the new updated speciality: ")
                doctors[index].set_speciality(updated_speciality)
                print("Speciality updated successfully.")
                
            else:
                print("Enter the valid option ")
            pass
 
        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)
 
            doctor_index = input('Enter the ID of the doctor to be deleted: ')
            try:
                doctor_index = int(doctor_index)-1
                
            except:
                print('The id entered is incorrect')
 
            else: 
                if self.find_index(doctor_index,doctors) != False:
                    delete_doctor=doctors.pop(doctor_index)
                    print(f'Doctor "{delete_doctor.full_name()}" is delete.')
            
          # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')
 
    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        for index, item in enumerate(patients):
         print(f'{index+1:3}|{item}')
        pass 
 
    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")
 
        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)
 
        patient_index = input('Please enter the patient ID: ')
 
        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1
 
            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures
 
        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures
 
        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms
 
        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')
 
        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1
 
            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                doctors[doctor_index].add_patient(patients[patient_index]) 
                patients[patient_index].link(doctors[doctor_index].full_name())
                pass
                
                print('The patient is now assign to the doctor.')
 
            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')
 
        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')
 
    def discharge(self, patients, discharged_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
             discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")
         
        self.view(patients)
        patient_index = input('Please enter the patient ID: ')
        ask=input("Do you want to discharge this patient(Y/N: )")
 
        try:
           patient_index = int(patient_index) - 1
           if self.find_index(patient_index, patients) !=False:
               if ask == 'Y' or ask == "y":
                discharged_patients.append(patients[patient_index])
                patients.pop(patient_index)
                print("Patient discharged successfully.")
           else:
              print('The entered ID was not found.')
        except IndexError:
          print('Invalid input. Please enter a valid ID.')
 
        
        #ToDo12
        pass
 
    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
 
        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo13
        self.view(discharged_patients)
 
    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """
 
        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))
 
        if op == 1:
            #ToDo14
            new_username= input("Enter the new username:")
            self.username = new_username
            print("New Username Updated Sucessfully.")
            pass
 
        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password
 
        elif op == 3:
            #ToDo15
            new_address= input("Enter the new address")
            self.address = new_address
            print("New address updated sucessfully.")
            pass
 
        else:
            #ToDo16
            print("Invalid option. Please Try Again")
            pass