import os 
import math 

directorio_Actual= os.getcwd()
print (f"Current working directory: {directorio_Actual}")

num= int(input("Enter an integer: "))

log_value = math.log2(num)
print (f"Log base 2 of {num} is: {log_value}")

floor_value = math.floor(log_value)
ceiling_value = math.ceil(log_value)

print (f"Floor: {floor_value}")
print (f"Ceiling: {ceiling_value}")