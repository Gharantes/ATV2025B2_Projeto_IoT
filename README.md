# ATV2025B2_Projeto_IoT
Atividade para Disciplina de IoT (Terça-Feira).

**Membros:** Guilherme Harmatiuk Arantes

## Escopo

## Funcionalidades
- Pelo Arduino:
	- Vai ler informação de Sensor **"X"** (qualquer uma).
		- Temperatura seria o melhor eu acho.
	- Enviar os dados por uma API para o backend, junto com o tempo atual.
- Pelo Computador:
    - Backend vai ter 2 Endpoints.
        - Um para receber as informações do Arduino. Por aqui, vai gravar elas em um banco.
        - Um para consultar essas informações.
	- O frontend vai fazer uma requisição ao backend cada 5/10 segundos, buscando os dados do banco.
    - A intenção é montar um gráfico que mostra a diferença entre valores do sensor ao passar do tempo. 
## Componentes
- Arduino
- ProtoBoard
- [Sensores de Umidade e Temperatura](https://blog.eletrogate.com/sensores-dht11-dht22/) (DH11)
- Depende: (se for necessário)
    - Resistor
    - Botão
## Título
## Objetivo
## Lista de Componentes
## Arquitetura Premilinar


# Questões
- Vai ser permitido consulta no Exame?