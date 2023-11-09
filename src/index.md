Gravity Sort
======

O **gravity sort** (ou bead sort) é um algoritmo de ordenação que não é
particularmente rápido ou eficiente em termos de memória... mas é bonito!
A ideia desse algoritmo é simular a queda de "contas" em um [ábaco](https://pt.wikipedia.org/wiki/%C3%81baco) devido à gravidade. 

Com essa explicação básica, é um pouco difícil de entender exatamente o que será feito, então vamos a um exemplo. Suponha que temos a seguinte lista:

```
[3, 3, 1, 4, 2]
```

Primeiro, colocamos no ábaco a quantidade de contas equivalente ao número que queremos ordenar, sempre à esquerda. Para a lista acima, colocaríamos as contas assim no ábaco: (por enquanto a gravidade está desligada, ou o ábaco está na horizontal, sei lá)

![Primeiro passo](bead/first.png)

Então, quando ligássemos a gravidade, as contas cairiam e ficariam assim:

![Segundo passo](bead/second.png)

E agora está tudo ordenado! A quantidade de contas no nível mais alto do ábaco representa o `lista[0]`, a quantidade de contas no segundo nível representa `lista[1]`, e assim por diante.

Assim, de acordo com a imagem, a lista ordenada fica:

```
[1, 2, 3, 3, 4]
```

Implementação em C
------------------

Primeiro, encontramos o maior elemento da lista:

```c
int max = 0;
for (int i = 0; i < size; i++) {
    if (list[i] > max) {
        max = list[i];
    }
}
```

Depois, criamos uma lista `beads` de tamanho `max` e inicializamos todos os elementos com 0. A ideia dessa lista é que cada elemento dela representa uma coluna do ábaco, e o valor de cada elemento representa a quantidade de contas naquela coluna.
  
```c
int *beads = calloc(max, sizeof(int));
```

Note que o método `calloc()` faz a mesma coisa que o `malloc()`, mas zera todos o espaço alocado.

??? Checkpoint

Como ficaria a lista `beads`, após ser inicializada, para a seguinte lista de entrada? Não considere o fim da execução do algoritmo, apenas como a lista ficaria após ser inicializada.

```
[3, 3, 1, 4, 2]
```

::: Gabarito

```
[0, 0, 0, 0]
```

:::

???

Em seguida, para cada elemento da lista, incrementamos `beads` até o índice `num - 1`:



```c
for (int i = 0; i < size; i++) {
    for (int j = 0; j < list[i]; j++) {
        beads[j]++;
    }
}
```

Pera lá, esse passo é confuso. Pare e pense sobre o que acontece com `beads` a cada iteração do for exterior. Vamos usar como exemplo a lista `[3, 3, 1, 4, 2]`:

```
depois da 1a iteração: [1, 1, 1, 0]
depois da 2a iteração: [2, 2, 2, 0]
depois da 3a iteração: [3, 2, 2, 0]
depois da 4a iteração: [3, 2, 2, 1]
depois da 5a iteração: [3, 3, 2, 1]
```


```c
// Cria a lista ordenada
int *sorted_list = malloc(size * sizeof(int));

// Para cada elemento da lista, percorre beads e incrementa count até que ele seja maior que i
for (int i = 0; i < size; i++) {
    int count = 0;
    for (int j = 0; j < max; j++) {
        if (beads[j] > i) {
            count++;
        }
    }
    sorted_list[i] = count;
}

return sorted_list;
}
```


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