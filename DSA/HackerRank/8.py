# my_list = ["Sam", "Jess","Taylor"]
# new_list = []
# for name in my_list:
#     name = name + " Smith" #The space added so it looks sam smith
#     new_list.append(name)

# new_list = [name + " Smith" for name in my_list]
# print(new_list)

#Rough 2
# num_list = [1,2,3,45,6,7,8,9,10]

# new_list = [i * 3 for i in num_list]
# print(new_list)

#Rough 3

x = 1
y = 1
z = 2
n = 3
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                print(i, j, k,)