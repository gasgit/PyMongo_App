from pymongo import MongoClient



client = MongoClient('localhost:27017')
db = client.Test_Document


def insert_doc():
    
    try: 
        name = raw_input("Enter name: ")
        email = raw_input("Enter Email: ")
        phone = raw_input("Enter Phone Number: ")
        dob = raw_input("Enter Date of Birth: ")

        print("Thank you!")
    except Exception, e:
        print(e)


insert_doc()