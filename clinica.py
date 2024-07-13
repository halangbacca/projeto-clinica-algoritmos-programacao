# Importa a biblioteca para verificar qual é o SO do usuário
import os

# Definindo uma lista para armazenar os dados dos pacientes
pacientes = []

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def calcular_risco_cardiovascular(paciente):
    risco = 0
    if paciente['sexo'] == 'f' and paciente['idade'] >= 68:
        risco += 8
    if paciente['exercicio_regular']:
        risco -= 1
    if paciente['dieta_saudavel']:
        risco -= 1
    if paciente['diabetico']:
        risco += 4
    if not paciente['fumante']:
        risco += 0
    if paciente['pressao_arterial'] <= 130/80:
        risco += 0
    if paciente['hdl_colesterol'] >= 45:
        risco += 1
    if paciente['ldl_colesterol'] <= 140:
        risco += 0
    return risco

def cadastrar_paciente():
    nome = input("\nNome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (m/f): ").lower()
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    exercicio_regular = input("Exercício regular? (s/n): ").lower() == 's'
    dieta_saudavel = input("Dieta saudável? (s/n): ").lower() == 's'
    fumante = input("Fumante? (s/n): ").lower() == 's'
    diabetico = input("Diabético? (s/n): ").lower() == 's'
    pressao_arterial = float(input("Pressão arterial (ex: 120/80): ").split('/')[0])
    hdl_colesterol = float(input("HDL colesterol (mg/dL): "))
    ldl_colesterol = float(input("LDL colesterol (mg/dL): "))

    imc = calcular_imc(peso, altura)
    paciente = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo,
        'peso': peso,
        'altura': altura,
        'imc': imc,
        'exercicio_regular': exercicio_regular,
        'dieta_saudavel': dieta_saudavel,
        'fumante': fumante,
        'diabetico': diabetico,
        'pressao_arterial': pressao_arterial,
        'hdl_colesterol': hdl_colesterol,
        'ldl_colesterol': ldl_colesterol
    }
    paciente['risco_cardiovascular'] = calcular_risco_cardiovascular(paciente)
    pacientes.append(paciente)
    print(f"\nPaciente {nome} cadastrado com sucesso!\n")

def listar_pacientes():
    if len(pacientes) == 0:
        print("\nNenhum paciente cadastrado.\n")
    else:
        for paciente in pacientes:
            print(f"\nNome: {paciente['nome']}, Idade: {paciente['idade']}, IMC: {paciente['imc']:.2f}, Risco Cardiovascular: {paciente['risco_cardiovascular']}")

def listar_pacientes_por_imc():
    if len(pacientes) == 0:
        print("\nNenhum paciente cadastrado.\n")
    else:
        for paciente in pacientes:
            pacientes_ordenados = sorted(pacientes, key=lambda x: x['imc'], reverse=True)
        for paciente in pacientes_ordenados:
            print(f"\nNome: {paciente['nome']}, IMC: {paciente['imc']:.2f}")

def listar_pacientes_por_risco():
    if len(pacientes) == 0:
        print("\nNenhum paciente cadastrado.\n")
    else:
        for paciente in pacientes:
            pacientes_ordenados = sorted(pacientes, key=lambda x: x['risco_cardiovascular'], reverse=True)
        for paciente in pacientes_ordenados:
            print(f"\nNome: {paciente['nome']}, Risco Cardiovascular: {paciente['risco_cardiovascular']}")

def aguardar():
    print("\nPressione qualquer tecla para continuar...")
    if input():
        os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela de acordo com o SO do usuário
        print("\n")

def menu():
    while True:
        print("Menu:")
        print("1 - Cadastro de pacientes")
        print("2 - Listagem de pacientes")
        print("3 - Listagem de pacientes por IMC")
        print("4 - Listagem de pacientes por risco cardiovascular")
        print("5 - Sair")
        opcao = int(input("\nEscolha uma opção: "))
        if opcao == 1:
            cadastrar_paciente()
            aguardar()
        elif opcao == 2:
            listar_pacientes()
            aguardar()
        elif opcao == 3:
            listar_pacientes_por_imc()
            aguardar()
        elif opcao == 4:
            listar_pacientes_por_risco()
            aguardar()
        elif opcao == 5:
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")
            aguardar()

menu()