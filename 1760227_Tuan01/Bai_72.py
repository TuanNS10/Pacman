list=[]
Number = int(input("Nhập số lượng phần tử trong danh sách: "))
for i in range(1, Number + 1):
    value = int(input("Nhập gia trị của phần tử %d: " %i))
    list.append(value)    
sum_ = 0
for item in list:
    if item % 2 == 0:
        sum_ += item
print(sum_) 