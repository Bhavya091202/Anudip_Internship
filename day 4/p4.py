list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # forward indexing
# for i in list:
#     print(i, end=" ")
# print(" ")
# for i in range(len(list)):
#     print(list[i], end=" ")
# print(" ")
# # backward indexing

# for i in range(len(list) - 1, -1, -1):
#     print(list[i], end=" ")
# print(" ")
# # reverse indexing

# len1 = len(list)
# for i in range(len1):
#     print(list[len1 - i - 1], end=" ") 
# print(" ")

# len1 = len(list)
# for i in range(1, len1 + 1):
#     print(list[-i], end=" ") 
# print(" ")


# len1 = len(list)
# for i in range(- 1, -len1 - 1, -1):
#     print(list[i], end=" ")
    
    
for i in range(-len(list), 0):
    print(list[i], end=" ")