from pymongo import MongoClient
import pprint



# MongoDB
# Create Database called 'Doc_Repo'
# Create collection called 'mydocuments'


try:
    client = MongoClient('localhost:27017')
    print("Connected Sucessfully To Server!")
    print(client)
    db = client.Doc_Repo

except Exception, e:
    print(e)


def insert_doc():
    
    try: 
        name = raw_input("Enter Name: ")
        email = raw_input("Enter Email: ")
        phone = raw_input("Enter Phone Number: ")
        dob = raw_input("Enter Date of Birth: ")

        print("Thank you!")

        db.mydocuments.insert_one({
            "name": name,
            "email": email,
            "phone": phone,
            "dob": dob
        })
        print("Document Inserted")

      
    except Exception, e:
        print(e)



def find_all():
    try:
        entries = db.mydocuments.find()
        for e in entries:
            print(e)
    except Exception, ex:
        print(ex)



def find_name():
    result = db.mydocuments.find_one({"name": "glen"})
    print(result)
    


#insert_doc()

#find_all()

find_name()