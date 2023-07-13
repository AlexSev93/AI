st = 'egufhg d#%E$^&I'
st_byte = b'hello'
print(st_byte)

for char in st_byte:
    print(char)

str_utf_8 = 'русские символы'
utf = str_utf_8.encode('utf-8')
to_str = utf.decode('utf-8')
print(utf, to_str)
