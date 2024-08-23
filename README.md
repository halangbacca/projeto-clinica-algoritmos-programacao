# Clínica multidisciplinar

- Aplicação para o cadastro de pacientes
- Cálculo automático de IMC e risco cardiovascular
- Listagem de todos os pacientes
- Listagem de pacientes por IMC
- Listagem de pacientes por risco cardiovascular

<img src="/assets/main.png" alt="tela-inicial">

> Tela Inicial do Sistema.

## **Tecnologias Utilizadas**

```
- Python 3.12.3
- Tkinter
```

## **Cálculo do IMC**

```
- Peso (em quilos) / altura² (em metros)
```

## **Cálculo do risco cardiovascular**

```
- Paciente feminino com idade >= 68 anos: +8 pontos
- Pratica exercício regularmente: -1 ponto
- Possui dieta saudável: -1 ponto
- Não é fumante: 0 pontos
- Diabético: +4 pontos
- Pressão arterial <= 130/80: 0 pontos
- Níveis de colesterol HDL >= 45 mg/dL: +1 ponto
- Níveis de colesterol LDL <= 140 mg/dL: 0 pontos
```

## **Porcentagem de risco cardiovascular ns próximos 10 anos**

### Homens:
```
-3 pontos: 1%
-2 ou -1 ponto: 2%
0 pontos: 3%
1 ou 2 pontos: 4%
3 pontos: 6%
4 pontos: 7%
5 pontos: 9%
6 pontos: 11%
7 pontos: 14%
8 pontos: 18%
9 pontos: 22%
10 pontos: 27%
11 pontos: 33%
12 pontos: 40%
13 pontos ou mais: 47%
```

### Mulheres:
```
< -2 pontos: 1%
-1, 0 ou 1 ponto: 2%
2 ou 3 pontos: 3%
4 pontos: 4%
5 pontos: 5%
6 pontos: 6%
7 pontos: 7%
8 pontos: 8%
9 pontos: 9%
10 pontos: 11%
11 pontos: 13%
12 pontos: 15%
>= 13 pontos: 17%
```

## **Classificação de risco cardiovascular**
```
- < 5%: baixo risco cardiovascular
- Entre 5 e 7,5%: compõem o grupo “borderline”
- Entre 7,5 e 12%: risco intermediário
- >= 13%: alto risco
```

## **Mestrandos**
- Halan Germano Bacca
- João Kasprowicz
- Priscila Rorato
- Thaísa Konrath
