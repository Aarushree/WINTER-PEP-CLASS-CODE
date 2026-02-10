#import create_engine to connect the database
from sqlalchemy import create_engine
engine=create_engine("sqlite:////school.db")
#sql lite database
#file name is school.db
#will be created if not exist
print("database connected")



