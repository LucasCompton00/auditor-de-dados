name = input("Digite o Nome: ").strip()
idade = input("Digite a Idade: ")
vName = False
vIdade = False
if not name :
    print(f"{name} é Um Dado Invalido")
else:
    vName = True
    
if idade.isdecimal(): 
    idade = int(idade)
    if 0 <= idade <= 120:
        vIdade = True
    else:
        print("Idade Fora Do Intervalo Permitido")
else:
    print(f"{idade} é Um invalido,Precisa Ser Um Numero Inteiro")

if vName and vIdade :
    print("Cadastro Válido")
