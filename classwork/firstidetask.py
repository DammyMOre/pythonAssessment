#for numbers in range (1,16):
 #   list = [numbers]
#    print(list, end=' ')
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#print(numbers)
#print(numbers+numbers)
number = numbers+numbers
print(number)

#def get_thirdelemnt(number):
total = 0
for index in range(number[1],len(number),3):
    print(number[index])
    total+=number[index]
    print(total)
   # for num in range(number[0], (len(number)/2) ):
       # print(number[num])
    print(number[0])
   # print(len(number)/2)
    print(number[len(number)-1])
