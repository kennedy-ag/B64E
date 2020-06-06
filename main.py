import funcoes

print("O que você deseja fazer?")
print("1 = Converter texto em base64")
print("2 = Converter base64 em texto\n")
entrada = input("Digite sua opção: ")

if(int(entrada)==1):
  text = input("Digite seu texto:\n\n")
  base64 = funcoes.text_to_base(text)
  print("\nResultado: ", base64)
elif(int(entrada)==2):
  base64 = input("Digite seu código base64:\n\n")
  text = funcoes.base_to_text(base64)
  print("\nResultado: ", text)
else:
  print("Opção inválida!")

#Testes, testes e mais testes!
