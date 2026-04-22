# string = "The fox jumped over the lazy dog"
# print(len(string.split(' ')))
# words = ['The', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
# print(words.index('the'))

# # Intent: The code should replace all 'a' characters with 'e'
# # and display the resulting message
# my_string = 'hare paws wall tuba draw'
# for i in range(len(my_string)):
#     if my_string[i] == 'a':
#         my_string[i] = 'e'

# print(my_string)





# import random

# # Your code goes here

# ori_message = input("Input a message:").split()
# out_message = []

# for word in ori_message:
#     if len(word) <= 3:
#         out_message.append(word)
#     else:
#         middle_chars = list(word[1:-1])
#         random.shuffle(middle_chars)
#         out_message.append(word[0] + "".join(middle_chars) + word[-1])

# print(" ".join(out_message))






# names = ["Tom", "Amy", "Bob"]
# ages = [18, 20, 19]

# print(list(zip(names, ages)))
x = [0,1,2,1/3,5/2,3]
for t in x:
    f = ((t-1)**3)*(20*t**3-104*t**2+143*t-19)+20
    print(t,f)
