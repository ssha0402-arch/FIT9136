mark_num = int(input("Input the number of marks: "))
n_num = int(0)
sum_num = float(0)
while mark_num > n_num :
    sum_num += float(input("Input mark "+str(n_num+1)+": "))
    n_num += 1
arv_num = sum_num / n_num
print("The average mark is", arv_num)