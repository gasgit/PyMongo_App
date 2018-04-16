from pymongo import MongoClient

# MongoDB
# Connect to Database called 'Doc_Repo'
# Create collection called 'mydocuments'

try:
    client = MongoClient('localhost:27017')
    print("Connected Sucessfully To Server!")
    print(client)
    db = client.Doc_Repo

    mycollection = "mydocuments"

    allcollections = db.collection_names()
    if not mycollection in allcollections:
        db.create_collection(mycollection)
        print(mycollection + " Collection Created :)")
    else:
        print(mycollection + " Already exists!")
except Exception, ex:
    print(ex)

# Get input from user
# Insert into mydocuments collection

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
    except Exception, ex:
        print(ex)

# Get all entries to mydocuments collection
# Iterate and print

def find_all():
    try:
        entries = db.mydocuments.find()
        for e in entries:
            print(e)
    except Exception, ex:
        print(ex)

# Get single document from mydocuments coollection
def find_name():
    result = db.mydocuments.find_one({"name": "glen"})
    print(result)
    


insert_doc()

#find_all()

#find_name()