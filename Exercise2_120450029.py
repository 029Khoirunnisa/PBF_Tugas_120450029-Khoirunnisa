#   Author      : Khoiruunisa
#   NIM         : 120450029
#   Affilition  : Sains Data - RA
#   Mata Kuliah : Pemrograman berbasis fungsi

text_1 = open('text1.txt').read()
text_2= open('text2.txt').read()

print((lambda x,y: int(x)+int(y))(text_1,text_2))