# Clínica multidisciplinar

- Cadastro de pacientes
- Cálculo automático de IMC e risco cardiovascular
- Listagem de todos os pacientes
- Listagem de pacientes por IMC
- Listagem de pacientes por risco cardiovascular

<img src="/assets/main2.png" alt="tela-inicial">

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

## **Classificação do IMC**

...
<18,5 - baixo peso 
18,5 até 24,9 - eutrofia (peso adequado) 
≥25 até 29,9 - sobrepeso 
>30,0 até 34,9 - obesidade grau I
35,00 até 39,99 - obesidade grau II 
≥40.00 - obesidade grau III
...

## **Cálculo do risco cardiovascular**

```
- Paciente feminino com idade >= 68 anos: +8 pontos
- Pratica exercício regularmente: -1 ponto
- Possui dieta saudável: -1 ponto
- Não é fumante: 0 pontos
- Fumante: +2 pontos
- Diabético: +4 pontos
- Pressão arterial <= 130/80: 0 pontos
- Níveis de colesterol HDL >= 45 mg/dL: -1 ponto
- Níveis de colesterol LDL <= 140 mg/dL: 0 pontos
- Calculo de IMC >=25: +2 pontos
 
```

## **Percentual de risco cardiovascular nos próximos 10 anos**

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
>= 13 pontos: 47%
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
< 5%: baixo risco cardiovascular
Entre 5 e 7,5%: compõem o grupo “borderline”
Entre 7,5 e 12%: risco cardiovascular intermediário
>= 13%: alto risco cardiovascular
```

## **Mestrandos**
- Halan Germano Bacca
- João Kasprowicz
- Priscila Rorato
- Thaísa Konrath
