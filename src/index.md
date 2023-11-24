Gravity Sort
======

O **gravity sort** (ou bead sort) é um algoritmo de ordenação que não é
particularmente rápido ou eficiente em termos de memória... mas é interessante e bonito de ver!

![Primeiro passo](bead/anim_bead_julien.gif)

Antes de começar a ordenar vetores, vamos fazer um **exercício de simulação**. Imagine que, dentro de uma grade quadrada, você tem cinco pilhas de caixas, com diferentes quantidades de caixas em cada uma.


![Primeiro passo](bead/caixas_empilhadas.png)

??? Checkpoint

Como ficaria essa grade se a girássemos 90 graus no sentido horário e deixássemos a gravidade agir sobre as caixas?


![Primeiro passo](bead/girando.gif)

Se precisar, desenhe a grade em um papel e faça a simulação.

::: Gabarito

Devido à gravidade, as caixas cairiam para baixo, e ficariam assim:


![Primeiro passo](bead/caindo.gif)

:::

???

Parabéns Newton, gravidade existe e funciona como esperamos. Mas como isso ~~afeta o grêmio~~ nos permite ordenar vetores? Vamos observar as imagens anteriores para descobrir.

??? Checkpoint

Se representássemos o número de caixas em cada **coluna** na imagem inicial da grade por um número em um vetor, como ficaria esse vetor?

::: Gabarito

O vetor seria ` [3, 1, 4, 2, 3]`, pois a primeira coluna tem 3 caixas, a segunda tem 1, e assim por diante.

:::

???

??? Checkpoint

E se representássemos o número de caixas em cada **linha** na imagem final da grade por um número em um vetor, como ficaria esse vetor?

::: Gabarito

O vetor seria ` [1, 2, 3, 3, 4]`, pois a primeira linha tem 1 caixa, a segunda tem 2, e assim por diante.

Olha só, são os mesmos valores que o primeiro vetor, porém agora ordenados!

???

E assim funciona o **gravity sort**. Existem [outras formas de exemplificá-lo](https://en.wikipedia.org/wiki/Bead_sort), como com um [ábaco](https://pt.wikipedia.org/wiki/%C3%81baco), mas a ideia é sempre a mesma: colocar os elementos em uma estrutura, girá-la e deixar a gravidade agir.

Para os nossos estudos, vamos usar caixas mesmo...

Implementação em Python
-------

...e um pouquinho de Python também.

A função que faz o `gravity sort`, recebe uma lista que vamos chamar de `input_list`
```py
def beadsort(input_list):
```

Inicializamos nosso código criando uma lista para retorno e iniciando uma lista com zero,s e seu tamanho é definido como o valor máximo presente na lista de entrada

```py
return_list = []

transposed_list = [0] * max(input_list)
```
A segunda parte é fazer a contagem: Nesta parte, o código percorre cada elemento na lista de entrada. Para cada elemento, os primeiros elementos da `transposed_list` são incrementados em 1. 
```py
for num in input_list:
    transposed_list[:num] = [n + 1 for n in transposed_list[:num]]
```
Nesta parte, o código constrói a lista de saída. Para cada posição i na lista de entrada, ele conta quantos elementos na `transposed_list` são maiores que i e adiciona esse número à `return_list`. Isso efetivamente determina a posição de cada elemento na lista ordenada.
Por ultimo devemos construir a lista de saida, a `return_list` 

```py
for i in range(len(input_list)):
    return_list.append(sum(n > i for n in transposed_list))
```
Essas três partes juntas formam o algoritmo Gravity Sort, onde a posição final de cada elemento é determinada com base nas contagens acumuladas.

??? Checkpoint

Quantos elementos teria a lista `beads`, para a seguinte lista de entrada?

```
[3, 3, 1, 4, 2, 7, 5, 6]
```

::: Gabarito

A lista teria 7 elementos, pois o maior valor da lista de entrada é 7.

```
[0, 0, 0, 0, 0, 0, 0]
```

:::

???

<!--
Implementação em C
------------------

Nessa implementação, vamos considerar uma função `beadsort` que recebe um ponteiro para uma lista de inteiros ` *list` e o tamanho dessa lista ` size`, e retorna um ponteiro para uma lista ordenada.

```c
int *beadsort(int *list, int size)
```

Para começar a implementação, encontramos o maior elemento da lista:

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

Note que o método `calloc()` faz a mesma coisa que o `malloc()`, mas zera todo o espaço alocado.

??? Checkpoint

Quantos elementos teria a lista `beads`, para a seguinte lista de entrada?

```
[3, 3, 1, 4, 2, 7, 5, 6]
```

::: Gabarito

A lista teria 7 elementos, pois o maior valor da lista de entrada é 7.

```
[0, 0, 0, 0, 0, 0, 0]
```

:::

???

Em seguida, para cada elemento da lista, incrementamos `beads` até o índice ` num - 1`:



```c
for (int i = 0; i < size; i++) {
    for (int j = 0; j < list[i]; j++) {
        beads[j]++;
    }
}
```

Pera lá, esse passo é confuso...

??? Checkpoint
...pare e simule o que acontece com `beads` a cada iteração do for exterior. Para isso, considere a lista ` [3, 3, 1, 4, 2]`.

Se necessário, utilize esse [template](/template.txt) no notepad.

::: Gabarito
```
início: [0, 0, 0, 0]
depois da 1a iteração: [1, 1, 1, 0]
depois da 2a iteração: [2, 2, 2, 0]
depois da 3a iteração: [3, 2, 2, 0]
depois da 4a iteração: [4, 3, 3, 1]
depois da 5a iteração: [5, 4, 3, 1]
```
:::

???

Em seguida, criamos uma nova lista para armazenar a lista ordenada que retornaremos no final. Dessa vez, o tamanho é `size`, pois queremos uma lista com o mesmo tamanho da lista de entrada.


```c
int *sorted_list = malloc(size * sizeof(int));
```

Aqui, não precisamos usar o `calloc()`, pois vamos preencher todos os elementos da lista com outros valores, pouco importanto o lixo de memória que estiver lá.

Depois, para cada elemento da lista, percorremos `beads` e incrementamos `count` até que ele seja maior que `i`, e então colocamos `count` no índice `i` da lista ordenada.

```c
for (int i = 0; i < size; i++) {
    int count = 0;
    for (int j = 0; j < max; j++) {
        if (beads[j] > i) {
            count++;
        }
    }
    sorted_list[i] = count;
}
```

??? Checkpoint

Como ficaria a lista `sorted_list` após cada iteração do for exterior? Considere uma lista beads ` [5, 4, 3, 1]`.

Novamente, use esse [template](/template2.txt) no notepad, se necessário.

::: Gabarito

```
início: [0, 0, 0, 0, 0]
depois da 1a iteração: [1, 0, 0, 0, 0]
depois da 2a iteração: [1, 2, 0, 0, 0]
depois da 3a iteração: [1, 2, 3, 0, 0]
depois da 4a iteração: [1, 2, 3, 3, 0]
depois da 5a iteração: [1, 2, 3, 3, 5]
```

Olha só, é a lista ordenada!

:::

???

E, por fim, retornamos essa nova lista.
```c
return sorted_list;
```

-->

---

Desafios
--------

??? Desafio

Qual a complexidade de tempo do **gravity sort**?

::: Gabarito

TODO GABARITO

:::

???

---

Código completo em C
--------------------

```c
int *beadsort(int *list, int size) {
    int max = 0;
    for (int i = 0; i < size; i++) {
        if (list[i] > max) {
            max = list[i];
        }
    }

    int *beads = calloc(max, sizeof(int));

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < list[i]; j++) {
            beads[j]++;
        }
    }

    int *sorted_list = malloc(size * sizeof(int));

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

Para fins de consulta numa linguagem em que vocês tem mais familiaridade, deixo aqui também uma implementação em Python:

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