from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
#step1
engine=create_engine("sqlite:///company.db")
#step2
Base= declarative_base()
#step3
class Employee(Base):
    __tablename__="employees"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    department=Column(String)

#step4
Base.metadata.create_all(engine)
#step5
Session=sessionmaker(bind=engine)
session=Session()
e1=Employee(name="Nobita",age=14,department="chillllllll")
e2=Employee(name="dekesuki",age=15,department="IAS")
session.add(e1)
session.add(e2)
session.commit()
#step6
Employees=session.query(Employee).all()
for i in Employees:
    print(i.id,i.name,i.age,i.department)

'''-----------code of updation-----------------'''
# Employees=session.query(Employee).filter_by(id=1).first()
# Employees.name="Arushree"
# session.commit()
# Employees=session.query(Employee).all()
# for i in Employees:
#     print(i.id,i.name,i.age,i.department)

'''----------code for deletion---------------'''
emp=session.query(Employee).filter(Employee.id==2).first()
if emp:
    session.delete(emp)
    session.commit()
print("delete-------------------------------------------------------")


Employees=session.query(Employee).all()
for i in Employees:
    print(i.id,i.name,i.age,i.department)


'''code to delete multiple data from table'''
emp=session.query(Employee).filter(Employee.age>18).all()
if emp:
    session.delete(emp)
    session.commit()
print("delete-------------------------------------------------------")


Employees=session.query(Employee).all()
for i in Employees:
    print(i.id,i.name,i.age,i.department)


#name is rahul and age is greater than 21 (and== ,)
emp=session.query(Employee).filter(Employee.name=="rahul",Employee.age>21).all()

#name is rahul or ge is greater than
from sqlalchemy import or_
emp=session.query(Employee).filter (or_(Employee.name=="rahul",Employee.age>21)).all()
"""== -> equal
   != -> not equal
    > -> greater than
    < ->less than 
    >= -> greater than or equal
    <= -> less than or equal"""

#ordered by
from sqlalchemy import desc,asc
emp=session.query(Employee).order_by(desc(Employee.id)).all()
print("----------------------------------------------------------")
emp=session.query(Employee).order_by(desc(Employee.id)).limit(2).all()
print(emp)