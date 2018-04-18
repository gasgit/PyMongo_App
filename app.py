from pymongo import MongoClient


import time

# MongoDB
# Connect to Database called 'Doc_Repo'
# Create collection called 'mydocuments'


def menu():
    while(1):
        
        print("\n1. Insert\n2. Find All\n3. Insert Many\n4. Less\n5. Delete All\n6. Get Input")
        
        choice = raw_input("Select: " )

        if choice == "1":
            insert_doc()
        elif choice == "2":
            find_all()
        elif choice == "3":
            insert_many()
        elif choice == "4":
            less()
        elif choice == "5":
            delete_all()
        elif choice == "6":
            get_num()
        else:
            print("Invalid Selection")
        
        

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
except Exception as ex:
    print str(ex)

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
    except Exception as ex:
        print str(ex)

# Get all entries to mydocuments collection
# Iterate and print

def find_all():
    try:
        entries = db.mydocuments.find()
        for e in entries:
            print(e)
    except Exception as ex:
        print str(ex)

# Get single document from mydocuments coollection

def find_name():
    try:
        result = db.mydocuments.find_one({"name": "glen"})
        print(result)
    except Exception as ex:
        print str(ex)
    

# insert multiple docs using time, and position

def insert_many():
    for i in range(100):
        db.mydocuments.insert({
            "time": time.clock(),
            "position": i
        })

# unused yet

def get_num():
    try:
        result =  int(raw_input("Enter less the 100: "))
        print(result)  
    except ValueError:
        print("Input error, use int value!")

# get all docs with id less than n
def less():
    try:
        lessthan_entries = db.mydocuments.find({"position":{"$lt":15}})
        for lt in lessthan_entries:
            print(lt)
    except Exception as ex:
        print(ex)
    

def greater():
    pass
    
def equal():
    pass
# clear all docs in collection
def delete_all():
    db.mydocuments.remove()


menu()

