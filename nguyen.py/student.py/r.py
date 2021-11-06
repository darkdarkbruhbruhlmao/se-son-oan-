from pymongo import MongoClient

client = MongoClient('192.168.1.6:27017')
read_database1 = client.get_database('readpdatabase1')
read_student = read_database1.get_collection('readstudent')

read_document = read_student.find_one({'name' : 'NAME1'})

read_document = read_student.find({'name' : 'NAME2'})

print(list(read_document))



















































# name = input("what is ypur name? ")
# lop = input("what is your class? ")
# school_year1 = input("enter your first year at school: ")
# school_year2 = input("Enter your last year at school: ")
# school_year = school_year1, 'to', school_year2


# dict.collection = ({
#     'name' : name,
#     'class' : lop,
#     'school year' : school_year 
# })



# def create_dict(dict):
#      print("hello", dict)
# create_dict(dict)