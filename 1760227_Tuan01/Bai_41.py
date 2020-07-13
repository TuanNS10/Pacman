n=int(input('Nhap vao n: :'))
if(n<=0):
    print('Gia tri n nhap vao khong hop le !!!')
else:
    sum=0
    x = 0
    while(n>0):
        for x in range(0,n+1):
            if(x%2==0):
                sum=sum+x
                n=n-2
    print('Tong cac so chan la: ',sum)