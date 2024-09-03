nome = "Kayron Mendes"
end = "Av Castelo Branco"
idade = 17

# print(nome, end, idade)
# 1ª forma de concatenação
print("Olá", nome,"seu endereço é ", end,"sua idade é ", idade)

#2ª forma de concatenação
print("Seja bem vindo {} sua residência está na {} e você possui {} anos".format(nome,end,idade))

#3ª forma de concatenação - f string
print(f"Olá, seja bem vindo {nome} o seu endereço é {end} e sua idade é {idade}")
