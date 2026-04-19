fileconnection = open("./week6/olympics.txt","r")
# fileconnection = open("olympics.txt", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    vals = row.strip().split(',')
    if vals[5] != "NA":
        print(f"{vals[0]}: {vals[4]}; {vals[5]}")