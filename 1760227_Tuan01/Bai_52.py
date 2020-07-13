NumList = []

Number = int(input("Nhập số lượng phần tử trong danh sách: "))
for i in range(1, Number + 1):
    value = float(input("Nhập gia trị của phần tử %d: " %i))
    NumList.append(value)

print("Phần tử nhỏ nhất là:", min(NumList)) 