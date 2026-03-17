number_of_marks = int(input("Input the number of marks: "))
total = 0.0

for index in range(1, number_of_marks + 1):
    mark = float(input(f"Input mark {index}: "))
    total += mark

average = total / number_of_marks
print(f"The average mark is {average:.1f}")
