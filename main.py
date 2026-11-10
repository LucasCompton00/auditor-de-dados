
cadastros = []

# ========== CADASTROS ==========
while True:
    name = input("Digite o Nome: ").strip()
    idade = input("Digite a Idade: ").strip()

    vName = False
    vIdade = False

    # ========== VALIDAÇÃO ==========
    if not name:
        print("Nome é um dado inválido")
    else:
        vName = True

    if idade.isdecimal():
        idade = int(idade)

        if 0 <= idade <= 120:
            vIdade = True
        else:
            print("Idade fora do intervalo permitido")
    else:
        print("Idade inválida. Digite um número inteiro")

    # ========== ARMAZENAMENTO ==========
    if vName and vIdade:
        print("Cadastro válido!")
        cadastros.append({"nome": name, "idade": idade})

    # ========== PERGUNTA S/N ==========
    while True:
        answer = input(
            "Deseja cadastrar outra pessoa? (S/N): "
        ).strip().lower()

        match answer:
            case "s":
                break

            case "n":
                break

            case _:
                print("Opção inválida! Digite S ou N.")

    # ========== ENCERRAMENTO ==========
    if answer == "n":
        break


# ========== RELATÓRIO FINAL ==========
print("\n" + "=" * 50)
print("RELATÓRIO DE CADASTROS")
print("=" * 50)

for cadastro in cadastros:
    print(f"Nome: {cadastro['nome']} | Idade: {cadastro['idade']}")

print(f"\nTotal de cadastros válidos: {len(cadastros)}")
print("=" * 50)
print("Até logo!")
