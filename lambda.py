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

string1: str = 'asdfgh'
print(list(string1))
print('sass' in 'dcfdffd')

#
string = "Skillbox курс 2018"
no_blanks = "".join([s for s in string if not s.isdigit()])
no_blanks.strip()
print(no_blanks)