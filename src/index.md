Gravity Sort
======

O **gravity sort** (ou bead sort) é um algoritmo de ordenação que não é
particularmente rápido ou eficiente em termos de memória... mas é bonito!
A ideia desse algoritmo é simular a queda de "contas" em um [ábaco](https://pt.wikipedia.org/wiki/%C3%81baco) devido à gravidade. 

Com essa explicação básica, é um pouco difícil de entender exatamente o que será feito, então vamos a um exemplo. Suponha que temos a seguinte lista:

```py
lista = [3, 3, 1, 4, 2]
```

Primeiro, colocamos no ábaco a quantidade de contas equivalente ao número que queremos ordenar, sempre à esquerda. Para a lista acima, colocaríamos as contas assim no ábaco: (por enquanto a gravidade está desligada, ou o ábaco está na horizontal, sei lá)

![Primeiro passo](bead/first.png)

Então, quando ligássemos a gravidade, as contas cairiam e ficariam assim:

![Segundo passo](bead/second.png)

E agora está tudo ordenado! A quantidade de contas no nível mais alto do ábaco representa o `lista[0]`, a quantidade de contas no segundo nível representa `lista[1]`, e assim por diante.

Assim, de acordo com a imagem, a lista ordenada fica:

```py
lista = [1, 2, 3, 3, 4]
```

Implementação
-------------

Primeiro encontramos o maior elemento do 

Código completo em Python
-------------------------

```py
def beadsort(input_list):
    return_list = []

    transposed_list = [0] * max(input_list)

    for num in input_list:
        transposed_list[:num] = [n + 1 for n in transposed_list[:num]]

    for i in range(len(input_list)):
        return_list.append(sum(n > i for n in transposed_list))

    return return_list
```