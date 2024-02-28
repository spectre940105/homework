a=float(input('請輸入:'))
b=float(input('請輸入:'))
c=float(input('請輸入:'))
q=b**2-4*a*c
float(q)
if q<0:
    print("無解")
elif q==0:
    print('(',-b/(2*a),')')
else:
    print('(',(-b+(b**2-4*a*c)^0.5)/(2*a),')')
    print('(',(-b-(b**2-4*a*c)^0.5)/(2*a),')')