import tkinter as tk
from tkinter import ttk, messagebox

# Definindo a lista de pacientes
pacientes = []

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def calcular_risco_cardiovascular(paciente):
    risco = 0
    if paciente['sexo'] == 'f':
        if paciente['idade'] >= 68:
            risco += 8
    if paciente['exercicio_regular']:
        risco -= 1
    if paciente['dieta_saudavel']:
        risco -= 1
    if paciente['diabetico']:
        risco += 4
    if paciente['hdl_colesterol'] >= 45:
        risco += 1

    return risco

def risco_cardiovascular_por_pontos(pontos, sexo):
    if sexo == 'm':
        if pontos == -3:
            return "1%"
        elif pontos in [-2, -1]:
            return "2%"
        elif pontos == 0:
            return "3%"
        elif pontos in [1, 2]:
            return "4%"
        elif pontos == 3:
            return "6%"
        elif pontos == 4:
            return "7%"
        elif pontos == 5:
            return "9%"
        elif pontos == 6:
            return "11%"
        elif pontos == 7:
            return "14%"
        elif pontos == 8:
            return "18%"
        elif pontos == 9:
            return "22%"
        elif pontos == 10:
            return "27%"
        elif pontos == 11:
            return "33%"
        elif pontos == 12:
            return "40%"
        else:
            return "47%"
    else:
        if pontos < -2:
            return "1%"
        elif pontos in [-1, 0, 1]:
            return "2%"
        elif pontos in [2, 3]:
            return "3%"
        elif pontos == 4:
            return "4%"
        elif pontos == 5:
            return "5%"
        elif pontos == 6:
            return "6%"
        elif pontos == 7:
            return "7%"
        elif pontos == 8:
            return "8%"
        elif pontos == 9:
            return "9%"
        elif pontos == 10:
            return "11%"
        elif pontos == 11:
            return "13%"
        elif pontos == 12:
            return "15%"
        else:
            return "17%"

def classificar_risco_cardiovascular(percentual):
    if percentual < 5:
        return "Baixo"
    elif 5 <= percentual < 7.5:
        return "Borderline"
    elif 7.5 <= percentual < 13:
        return "Intermediário"
    else:
        return "Alto"

def cadastrar_paciente():
    try:
        nome = nome_entry.get()
        if not nome:
            raise ValueError("Nome não pode ser vazio")

        idade = idade_entry.get()
        if idade == '' or int(idade) <= 0:
            raise ValueError("Idade deve ser um número positivo")
        else:
            idade = int(idade)

        sexo = sexo_var.get().lower()
        if sexo not in ["m", "f"]:
            raise ValueError("Sexo deve ser 'm' ou 'f'")

        peso = peso_entry.get()
        if peso == '' or float(peso) <= 0:
            raise ValueError("Peso deve ser um número positivo")
        else:
            peso = float(peso)

        altura = altura_entry.get()
        if altura == '' or float(altura) <= 0:
            raise ValueError("Altura deve ser um número positivo")
        else:
            altura = float(altura)

        exercicio_regular = exercicio_var.get()
        dieta_saudavel = dieta_var.get()
        fumante = fumante_var.get()
        diabetico = diabetico_var.get()

        pressao_arterial = pressao_entry.get()
        if not pressao_arterial:
            raise ValueError("Pressão arterial não pode ser vazia")

        hdl_colesterol = hdl_entry.get()
        if hdl_colesterol == '' or float(hdl_colesterol) < 0:
            raise ValueError("HDL colesterol deve ser um número não negativo")
        else:
            hdl_colesterol = float(hdl_colesterol)

        ldl_colesterol = ldl_entry.get()
        if ldl_colesterol == '' or float(ldl_colesterol) < 0:
            raise ValueError("LDL colesterol deve ser um número não negativo")
        else:
            ldl_colesterol = float(ldl_colesterol)

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

        pontos_risco = calcular_risco_cardiovascular(paciente)
        percentual_risco = float(risco_cardiovascular_por_pontos(pontos_risco, sexo).replace("%", ""))

        classificacao_risco = classificar_risco_cardiovascular(percentual_risco)

        paciente['risco_cardiovascular'] = f"{percentual_risco}% ({classificacao_risco})"
        pacientes.append(paciente)

        messagebox.showinfo("Sucesso", f"Paciente {nome} cadastrado com sucesso! IMC: {imc:.2f}, Risco Cardiovascular: {paciente['risco_cardiovascular']}")
        limpar_campos()

    except ValueError as ve:
        messagebox.showerror("Erro de Validação", str(ve))

def listar_pacientes():
    listar_todos_pacientes(pacientes)

def listar_pacientes_por_imc():
    pacientes_ordenados = sorted(pacientes, key=lambda x: x['imc'], reverse=True)
    listar_todos_pacientes(pacientes_ordenados)

def listar_pacientes_por_risco():
    # Ordena os pacientes por risco cardiovascular, convertendo a string percentual em float
    pacientes_ordenados = sorted(pacientes, key=lambda x: float(x['risco_cardiovascular'].split('%')[0]), reverse=True)
    listar_todos_pacientes(pacientes_ordenados)

def listar_todos_pacientes(pacientes_list):
    list_window = tk.Toplevel(root)
    list_window.title("Listagem de Pacientes")
    tree = ttk.Treeview(list_window, columns=("nome", "idade", "imc", "risco"), show="headings")
    tree.heading("nome", text="Nome")
    tree.heading("idade", text="Idade")
    tree.heading("imc", text="IMC")
    tree.heading("risco", text="Risco Cardiovascular")
    tree.pack(fill=tk.BOTH, expand=True)

    for paciente in pacientes_list:
        tree.insert("", "end", values=(paciente['nome'], paciente['idade'], f"{paciente['imc']:.2f}", paciente['risco_cardiovascular']))

def limpar_campos():
    nome_entry.delete(0, tk.END)
    idade_entry.delete(0, tk.END)
    sexo_var.set("")
    peso_entry.delete(0, tk.END)
    altura_entry.delete(0, tk.END)
    exercicio_var.set(False)
    dieta_var.set(False)
    fumante_var.set(False)
    diabetico_var.set(False)
    pressao_entry.delete(0, tk.END)
    hdl_entry.delete(0, tk.END)
    ldl_entry.delete(0, tk.END)

# Configurando a janela principal
root = tk.Tk()
root.title("Sistema de Cadastro de Pacientes")

# Criando frames para organizar a interface
frame1 = ttk.Frame(root, padding="10")
frame1.grid(row=0, column=0, sticky=(tk.W, tk.E))

frame2 = ttk.Frame(root, padding="10")
frame2.grid(row=1, column=0, sticky=(tk.W, tk.E))

# Frame 1: Formulário de cadastro
ttk.Label(frame1, text="Nome:").grid(row=0, column=0, sticky=tk.W)
nome_entry = ttk.Entry(frame1)
nome_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame1, text="Idade:").grid(row=1, column=0, sticky=tk.W)
idade_entry = ttk.Entry(frame1)
idade_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame1, text="Sexo (m/f):").grid(row=2, column=0, sticky=tk.W)
sexo_var = tk.StringVar()
sexo_entry = ttk.Combobox(frame1, textvariable=sexo_var, values=["m", "f"])
sexo_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame1, text="Peso (kg):").grid(row=3, column=0, sticky=tk.W)
peso_entry = ttk.Entry(frame1)
peso_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame1, text="Altura (m):").grid(row=4, column=0, sticky=tk.W)
altura_entry = ttk.Entry(frame1)
altura_entry.grid(row=4, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame1, text="Exercício regular:").grid(row=5, column=0, sticky=tk.W)
exercicio_var = tk.BooleanVar()
exercicio_check = ttk.Checkbutton(frame1, variable=exercicio_var)
exercicio_check.grid(row=5, column=1, sticky=tk.W)

ttk.Label(frame1, text="Dieta saudável:").grid(row=6, column=0, sticky=tk.W)
dieta_var = tk.BooleanVar()
dieta_check = ttk.Checkbutton(frame1, variable=dieta_var)
dieta_check.grid(row=6, column=1, sticky=tk.W)

ttk.Label(frame1, text="Fumante:").grid(row=7, column=0, sticky=tk.W)
fumante_var = tk.BooleanVar()
fumante_check = ttk.Checkbutton(frame1, variable=fumante_var)
fumante_check.grid(row=7, column=1, sticky=tk.W)

ttk.Label(frame1, text="Diabético:").grid(row=8, column=0, sticky=tk.W)
diabetico_var = tk.BooleanVar()
diabetico_check = ttk.Checkbutton(frame1, variable=diabetico_var)
diabetico_check.grid(row=8, column=1, sticky=tk.W)

ttk.Label(frame1, text="Pressão arterial (ex: 120/80):").grid(row=9, column=0, sticky=tk.W)
pressao_entry = ttk.Entry(frame1)
pressao_entry.grid(row=9, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame1, text="HDL colesterol (mg/dL):").grid(row=10, column=0, sticky=tk.W)
hdl_entry = ttk.Entry(frame1)
hdl_entry.grid(row=10, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame1, text="LDL colesterol (mg/dL):").grid(row=11, column=0, sticky=tk.W)
ldl_entry = ttk.Entry(frame1)
ldl_entry.grid(row=11, column=1, sticky=(tk.W, tk.E))

ttk.Button(frame1, text="Cadastrar Paciente", command=cadastrar_paciente).grid(row=12, column=0, columnspan=2, pady=10)

# Frame 2: Botões de listagem
ttk.Button(frame2, text="Listar Todos os Pacientes", command=listar_pacientes).grid(row=0, column=0, padx=10, pady=5)
ttk.Button(frame2, text="Listar Pacientes por IMC", command=listar_pacientes_por_imc).grid(row=0, column=1, padx=10, pady=5)
ttk.Button(frame2, text="Listar Pacientes por Risco Cardiovascular", command=listar_pacientes_por_risco).grid(row=0, column=2, padx=10, pady=5)

root.mainloop()