csv_data = [
"Name,Student ID,Suburb",
"Luke,202154321,2000 NSW Sydney",
"Anakin,202212345,3800 VIC Clayton",
"Boba,202223456,3800 VIC Clayton",
"Leia,202098764,3000 VIC Melbourne"
]

#we ask the user for a year
query_year = int(input("Input year to search: "))
#print (csv_data[2])

for row in csv_data[1:] :
    element = row.split(",")
    Name = element[0]
    Student_ID = element[1]
    Suburb = element[2]
    if query_year == int(Student_ID[:4:1]):
        Address = Suburb.split(" ")
        print(Name , Address[1] )
    