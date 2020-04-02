def str_to_bin(string):
  binario = ''
  binary_list = []
  index = 0
  for i in string:
    binario += bin(ord(i))[2::]
    binary_list.append(binario)
    binario = ''
  for i in binary_list:
    if(len(i)<8):
      binary_list[index] = "{0}{1}".format("0"*(8-len(i)), i)
    index = index + 1
  return binary_list

def concat_bits(lista):
  concat = []
  if(len(lista)<3):
    value = ''.join(lista)
    concat.append(value)
  else:
    iterable = len(lista)//3
    for i in range(0, iterable):
      value = ''.join(lista[0:3])
      concat.append(value)
      del(lista[0:3])
    if(lista!=[]):
      value = ''.join(lista)
      concat.append(value)
  return concat

def divide_concat(lista):
  divided = []
  for i in lista:
    if(len(i)==24):
      aux = []
      aux.append(i[0:6])
      aux.append(i[6:12])
      aux.append(i[12:18])
      aux.append(i[18:24])
      divided.append(aux)
    elif(len(i)==16):
      aux = []
      aux.append(i[0:6])
      aux.append(i[6:12])
      aux.append(i[12:16]+"00")
      aux.append("empty")
      divided.append(aux)
    else:
      aux = []
      aux.append(i[0:6])
      aux.append(i[6:8]+"0000")
      aux.append("empty")
      aux.append("empty")
      divided.append(aux)
  return divided

def find_values(lista):
  values = []
  for i in lista:
    for k in i:
      if(k!="empty"):
        value = int(k, 2)
        values.append(value)
      else:
        values.append("=")
  return values

def convert_values(lista):
  base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  values = []
  for i in lista:
    if(i!='='):
      value = base64[i]
      values.append(value)
    else:
      values.append(i)
  values = ''.join(values)
  return values

def text_to_base(string):
  binary_list = str_to_bin(string)
  concat = concat_bits(binary_list)
  divided = divide_concat(concat)
  values = find_values(divided)
  base64 = convert_values(values)
  return base64

def base_to_decimal(string):
  base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  decimals = []
  for c in string:
    if(c!='='):
      index = base64.index(c)
      decimals.append(index)
    else:
      decimals.append('e')
  return decimals

def decimal_to_bin(lista):
  binarios = []
  for i in lista:
    if(i!='e'):
      binario = str(bin(i))
      binario = binario[2:]
      binario = "{0}{1}".format((6-len(binario))*'0', binario)
      binarios.append(binario)
  return binarios

def concat_reverse_bitlist(lista):
  full_binary = ''.join(lista)
  return full_binary

def slice_reverse_bitlist(string):
  binarios = []
  r = len(string)//8
  for i in range(0, r):
    binario = string[0:8]
    binarios.append(binario)
    string = string[8:]
  binarios = ' '.join(binarios)
  return binarios

def bin_to_str(binario):
  binario = str(binario)
  caractere = ''
  string = ''
  tamanho = len(binario)
  k = 1
  for j in binario:
    if j != ' ':
      caractere += j
      if k == tamanho:
        string += chr(int(caractere, 2))
    else:
      string += chr(int(caractere, 2))
      caractere = ''
    k += 1
  return string

def base_to_text(base):
  a = base_to_decimal(base)
  b = decimal_to_bin(a)
  c = concat_reverse_bitlist(b)
  d = slice_reverse_bitlist(c)
  e = bin_to_str(d)
  return e