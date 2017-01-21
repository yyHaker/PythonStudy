# -*- coding: utf-8 -*-
height = 1.76
weight = 67.5
bmi = weight/(height*height)
print(bmi)
if ( bmi < 18.5 ):
    print("too light")
elif (bmi>=18.5 and bmi<25):
    print("normal")
elif(bmi>=25 and bmi<28):
    print("too weighty")
elif (bmi>=28 and bmi<32):
    print("bmi>32")
else:
    print("serious weighty")