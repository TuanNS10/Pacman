
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

duplicate = []

Number = int(input("Nhập số lượng phần tử trong danh sách: "))
for i in range(1, Number + 1):
    value = int(input("Nhập gia trị của phần tử %d: " %i))
    duplicate.append(value)
print(Remove(duplicate))