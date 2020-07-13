test_dict = {"ST" : 20, "TH" : 20, "KN" : 20, "Neymar JR" : 27}  
print ("Từ điển trước khi xóa : " + str(test_dict)) 
new_dict = {key:val for key, val in test_dict.items() if key != 'KN'} 
print ("Từ điển sau khi xóa là : " + str(new_dict)) 