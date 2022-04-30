#   Author      :Khoiruunisa
#   NIM         : 120450029
#   Affilition  : Sains Data - RA
#   Mata Kuliah : Pemrograman berbasis fungsi
#   Deskripsi Program : Enkripsi password


def encrypt(pwd):
  splitpass = list(pwd)
  asciipass = list()
  for char in splitpass:
    asciichar = ord(char)
    asciipass.append(asciichar)

  new_password = ""
  for num in asciipass:
    firstval = num//26 + 80
    secondval = num%26 + 80
    if firstval > secondval:
      thirdval = '-'
    else:
      thirdval = '+'
    new_password = new_password + chr(firstval) + chr(secondval) + thirdval
  return new_password

def original_password(pwd):
  splitpass = [pwd[i:i+3] for i in range(0, len(pwd), 3)]
  asciipass = list()
  for word in splitpass:
    firstval = ord(word[0]) - 80
    secval = ord(word[1]) - 80
    val = 26 * firstval + secval
    asciipass.append(val)
  password = ''
  for i in asciipass:
    char = chr(i)
    password = password + char
  return password

print('Enkripsi Password: ')
password1 = 'anakanakcerdas2020'
print ('Original Password: '+ password1)
print ("Encrypted Password: "+ encrypt(password1))

print("\nOriginal Password:")
password2 = "Sc-TV-Sc-TS+T[-Sc-TQ+TV-T[-Sf-Sc-T\-Sc-Qh-Qf-Qh-Qf-TS+Sg-Se-Sg-"
print ("Encrypted Password : " + password2)
print ("Original Password : " + original_password(password2))


