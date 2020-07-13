NumList = []
Odd_Sum = 0

Number = int(input("Nhập n phần tử trong danh sách: "))
for i in range(1, Number + 1):
    value = int(input("Nhập gia trị của phần tử %d: " %i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j] % 2 != 0):       
        Odd_Sum = Odd_Sum + NumList[j]


print("Tổng các số lẻ có trong danh sách là =  ", Odd_Sum)