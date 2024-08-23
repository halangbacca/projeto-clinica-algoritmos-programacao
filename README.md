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

## **Pontuação de risco cardiovascular**

### Homens:
```
- -3 pontos: 1% de risco cardiovascular nos próximos 10 anos
- -2 ou -1 ponto: 2% de risco cardiovascular nos próximos 10 anos
- 0 pontos: 3% de risco cardiovascular nos próximos 10 anos
- 1 ou 2 pontos: 4% de risco cardiovascular nos próximos 10 anos
- 3 pontos: 6% de risco cardiovascular nos próximos 10 anos
- 4 pontos: 7% de risco cardiovascular nos próximos 10 anos
- 5 pontos: 9% de risco cardiovascular nos próximos 10 anos
- 6 pontos: 11% de risco cardiovascular nos próximos 10 anos
- 7 pontos: 14% de risco cardiovascular nos próximos 10 anos
- 8 pontos: 18% de risco cardiovascular nos próximos 10 anos
- 9 pontos: 22% de risco cardiovascular nos próximos 10 anos
- 10 pontos: 27% de risco cardiovascular nos próximos 10 anos
- 11 pontos: 33% de risco cardiovascular nos próximos 10 anos
- 12 pontos: 40% de risco cardiovascular nos próximos 10 anos
- 13 pontos ou mais: 47% de risco cardiovascular nos próximos 10 anos
```

### Mulheres:
```
- < -2 pontos: 1% de risco cardiovascular nos próximos 10 anos
- -1, 0 ou 1 ponto: 2% de risco cardiovascular nos próximos 10 anos
- 2 ou 3 pontos: 3% de risco cardiovascular nos próximos 10 anos
- 4 pontos: 4% de risco cardiovascular nos próximos 10 anos
- 5 pontos: 5% de risco cardiovascular nos próximos 10 anos
- 6 pontos: 6% de risco cardiovascular nos próximos 10 anos
- 7 pontos: 7% de risco cardiovascular nos próximos 10 anos
- 8 pontos: 8% de risco cardiovascular nos próximos 10 anos
- 9 pontos: 9% de risco cardiovascular nos próximos 10 anos
- 10 pontos: 11% de risco cardiovascular nos próximos 10 anos
- 11 pontos: 13% de risco cardiovascular nos próximos 10 anos
- 12 pontos: 15% de risco cardiovascular nos próximos 10 anos
- 13 pontos ou mais: 17% de risco cardiovascular nos próximos 10 anos
```

## **Classificação de risco cardiovascular**
```
- Inferior a 5% prediz baixo risco cardiovascular
- Entre 5 e 7,5% compõem o grupo “borderline”
- Entre 7,5 e 12% risco intermediário
- E uma taxa igual ou superior a 13% de evento nos próximos 10 anos, alto risco
```

## **Mestrandos**
- Halan Germano Bacca
- João Kasprowicz
- Priscila Rorato
- Thaísa Konrath
