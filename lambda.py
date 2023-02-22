import math
# filter
my_list = [1, 5, 7, 8, 9, 10]
new_list = list(filter(lambda x:(x%2==0),my_list))
print(new_list)

# map
new_list = list(map(lambda x:(x*2),my_list))
print(new_list)

print(dir(math))
print(math.__loader__)