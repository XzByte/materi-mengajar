
# looping dengan for 
# print the integer 2 through 10 using a "for" loop
for i in range(2, 11):
    print(i)


#looping dengan while
# print the integer 2 through 10 using a "while" loop
i = 2
while i < 11:
    print(i)
    i = i + 1


# return result dari fungsi
def doubles(num):
    """Return the result of multiplying an input number by 2."""
    return num * 2

#looping conditional dan pemanggilan hasil# lalu panggil function tersebut
my_num = 2
for i in range(0, 3):
    my_num = doubles(my_num)
    print(my_num)
