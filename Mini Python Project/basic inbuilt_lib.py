'''===================================module project1============================================================
- in this we will use
* maths
* random
* counter
1. Generate random number
2. check which number
3. round numbers using maths
4. count how many timees number appear
5.saves the result in a file
'''
import math  #---------------------------->importing maths
import random #--------------------------->importing random
import os #-------------------------------->
import re
from collections import Counter
numbers = [random.randint(1,10) for _ in range(1,10)]
print(numbers)

#even or odd
even_numbers=[]
odd_numbers=[]
for num in numbers:
    num_str=str(num)
    if re.search(r"^[02468]$",num_str):
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
#calculating average
average=sum(numbers)/len(numbers)
#round off the average
rounded_avg=math.ceil(average)
#count number
count_numbers=Counter(numbers)
#save result using os
if not os.path.exists("easy_reports"):
    os.mkdir("easy_reports")

#file paths
file_path=os.path.join("easy_reports","number_report.txt")

#write data to a file
file=open(file_path,"w")
file.write(f"Generated Numbers:{numbers}")
file.write(f"even_Number:{even_numbers}")
file.write(f"odd_number:{odd_numbers}")
file.write(f"average:{rounded_avg}")
file.write(f"number count:\n")
for num,count in count_numbers.items():
    file.write(f"{num}:{count}\n")

file.close()
print(numbers)
print(odd_numbers)
print(even_numbers)
print(rounded_avg)
print(count_numbers)
print(file_path)