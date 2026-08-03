patients = []

doctors = []

diseases = set()

status = ("Admitted", "Discharged")

def menu():

    print("======= Hospital Management System =======")

    print("1. Add Patient")
    print("2. Show Patients")
    print("3. Search Patient")
    print("4. update Patient")
    print("5. Delete Patient")
    print("6. Add Doctor")
    print("7. Show Doctors")
    print("8. Assign Doctor")
    print("9. Show Report")
    print("10. Exit")
    print("==========================")

def add_patients():
    patient_id = input("enter patients id:")
    name = input("enter patients name:")
    age = (int(input("enter patients age:")))
    city= input("enter patients city:")
    disease = input("enter patients disease:")

    patient = {
            "id": patient_id,
        "name": name,
        "age": age,
        "city": city,
        "disease": disease,
        "status": "Admitted"
    }

    patients.append(patient)

    print("Patient Added Successfully")
    print("==========================")


def   show_patient():

       if len(patients)== 0:
           print("no patient found:")

       else :
          print("======= All patients ========")


          for patient in patients:
                
                print("ID:", patient["id"])
                print("Name:", patient["name"])
                print("Age:", patient["age"])
                print("City:", patient["city"])
                print("Disease:", patient["disease"])
                print("Status:", patient["status"])
                if "doctor" in patient:
                    print("Doctor:", patient["doctor"])
                else:
                    print("doctor not found")
                print("----------------------")

def search_patient():
     patient_id=input("enter patient id:")

     found = False
     for patient in patients:
        if patient["id"]== patient_id:
            print("id:",patient["id"]) 
            print("name:",patient["name"]) 
            print("age:",patient["age"]) 
            print("city:",patient["city"]) 
            print("disease:",patient["disease"]) 
            print("status:",patient["status"]) 

            found = True
            break

     if found== False:
           print("patient not found:")
           print("==========================")

def update_patient():
     patient_id= input("enter patient id:")
     found = False


     for patient in patients:
            if  patient["id"]==patient_id:
                print("patient found")

                new_name = input("enter patient new name:")
                new_age = int(input("enter patient new age"))
                new_city = input("enter patient new city")
                new_disease = input("enter patient new disease:")

                patient["name"] = new_name
                patient["age"] = new_age
                patient["city"] = new_city
                patient["disease"] = new_disease
                print("patient update successfully:")
                found = True
                break
     if found == False:
        print("patient not found")
        print("==========================")


def delete_patient():
      patient_id =input("enter patirnt id:")
      found = False

      for patient in patients:
            if patient["id"]== patient_id:
              patients.remove(patient) 
              print("patient deleted successfully:") 
              found =True
              break  
      if  found == False:
        print("Patient Not Found")
        print("==========================")


def add_doctor():
      
        doctor_id = input("enter doctor id:")
        name = input("enter doctor name:")
        specialization = input("enter doctor specialization:")
        city= input("enter doctor city:")
      
     
        doctor = {
                 "doctor_id": doctor_id,
             "name": name,
             "specialization":specialization,
             "city": city,
             
         }
     
        doctors.append(doctor)
     
        print("doctor Added Successfully")
        print("==========================")


def show_doctor():
      if len(doctors)==0:

        print("no doctor found:")

      else:
            print("===all doctors====")

            for doctor in doctors:
                  print("doctor_id:",doctor["doctor_id"])
                  print("name:",doctor["name"])
                  print("city:",doctor["city"])
                  print("specialization:",doctor["specialization"])
                  print("==========================")




def assign_doctor():
      
    patient_id =input("enter patient id:")
    doctor_id =input("enter doctor id:")

    patient_found = False
    doctor_found =False


    for patient in patients:
        if patient["id"]==patient_id:

            patient_found=True

            for doctor in doctors:
                if doctor["doctor_id"] == doctor_id:

                   doctor_found=True
                   patient["doctor"] = doctor["name"]

                   print("doctor add successfully:")
                   break
                if doctor_found:
                    break
    if patient_found== False:
             print("patient not found")
    elif doctor_found== False:
                     print("doctor not found")
                     print("==========================")

def show_report():
    patient_id=input("enter patient id:")

    found =False

    for patient in patients:
        if  patient["id"] == patient_id:

            print("====patient report======")
            print("id:",patient["id"]) 
            print("name:",patient["name"]) 
            print("age:",patient["age"]) 
            print("city:",patient["city"]) 
            print("disease:",patient["disease"]) 
            print("status:",patient["status"]) 

            if "doctor" in patient:
                print("doctor:",patient["doctor"])

            else:
                print("doctor not assign")

            found = True
            break

    if found == False:
        print("patient not found")
        print("==========================")


while True:

    menu()

    choice = input("enter your choice:")

    if choice == "1":
        add_patients()

    elif choice == "2":
        show_patient()

    elif choice == "3":
        search_patient()

    elif choice == "4":
            update_patient()

    elif choice == "5":
            delete_patient()

    elif choice == "6":           
            add_doctor()

    elif choice == "7":
            show_doctor()

    elif choice == "8":
            assign_doctor()

    elif choice == "9":
            show_report()

    elif choice == "10":
             
             print("Thank For Using Hospital Management System:")
             break
    else:
             print("invalid choice")
