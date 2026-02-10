# # from sqlalchemy import create_engine
# # engine=create_engine("sqlite:////school.db")
# # #import  declarative_base
# # from sqlalchemy.orm import declarative_base
# # from sqlalchemy import Column, Integer, String
# # #it will usse to insert our data inside the table
# # from sqlalchemy.orm import sessionmaker
# # #create base class
# # Base= declarative_base()
# # #base will be parent pf all models
# # class Student(Base):
# #     __tablename__="students"
# #     id=Column(Integer,primary_key=True)
# #     name=Column(String)
# #     age=Column(Integer)
# #     course=Column(String)

# # Session=sessionmaker(bind=engine)
# # session=Session()
# # s1=Student(id=1,name="rahul",age=20,course="python")
#import  declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
#step 1
engine=create_engine("sqlite:///school.db")
#create base class
#step 2
Base=declarative_base()
# #base will be parent of all models
# #step 3
# class Student(Base):
#     __tablename__="students"
#     id=Column(Integer,primary_key=True)
#     name=Column(String)
#     age=Column(Integer)
#     course=Column(String)
# #create all tables defined using base
# #step 4
# Base.metadata.create_all(engine)

# #step 5
# Session=sessionmaker(bind=engine)
# session=Session()
# s1=Student(name="rahul",age=21,course="python")
# s2=Student(name="karan",age=22,course="java")
# session.add(s1)
# session.add(s2)
# session.commit()
# students = session.query(Student).all()
# for i in students:
#     print(i.id,i.name,i.age,i.course)

# import os
# print(os.getcwd())
# print("above is path of database")

# stu=session.query(Student).filter(Student.age>20).all()
# for i in stu:
#     session.delete(i)
# session.commit()















from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Department(Base):
    __tablename__="depatments"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    students=relationship("Student",back_populates="department")

class Student(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    department_id=Column(Integer,ForeignKey("department.id"))
    department=relationship("Department",back_populates="students")

print("program end=============================")