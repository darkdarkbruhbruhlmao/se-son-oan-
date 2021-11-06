from pymongo import MongoClient

client = MongoClient('192.168.1.6:27017')
read_database1 = client.get_database('readpdatabase1')
read_student = read_database1.get_collection('readstudent')

def update_student(student_payload, query):
    read_student.update_one(query, student_payload)