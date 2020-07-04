# Copy-Ah
Introdução
John é monitor na matéria de Introdução à Produção Textual I na Penn State University (PSU). Durante esse período, John descobriu que uma epidemia de COH-PIAH estava se espalhando pela PSU. Essa doença rara e altamente contagiosa faz com que as pessoas contaminadas produzam textos extremamente semelhantes de forma involuntária. Após a entrega da primeira redação, John desconfiou que alguns alunos estavam sofrendo de COH-PIAH. John, se preocupando com a saúde da turma, resolveu buscar um método para identificar os casos de COH-PIAH. Para isso, ele necessita da sua ajuda para desenvolver um programa que o auxilie a identificar os alunos contaminados.

Detecção de autoria
Utilizando diferentes estatísticas do texto, é possível identificar aspectos que funcionam como uma “assinatura” do autor. Diferentes pessoas possuem diferentes estilos de escrita, algumas preferindo sentenças mais curtas, outras preferindo sentenças mais longas.

Essas “assinatura” pode ser utilizada para detecção de plágio, evidência forense, ou nesse caso, para detectar a grave doença COH-PIAH.

Traços linguísticos
Nesse exercício utilizaremos as seguintes estatísticas para detectar a doença:

Tamanho médio de palavra: Média simples do número de caracteres por palavra.
Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
Razão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo número total de palavras.
Tamanho médio de sentença: Média simples do número de caracteres por sentença.
Complexidade de sentença: Média simples do número de frases por sentença.
Tamanho médio de frase: Média simples do número de caracteres por frase.
Funcionamento do programa
Diversos estudos foram compilados e hoje se conhece precisamente a assinatura de um portador de COH-PIAH. Seu programa deverá receber diversos textos e calcular os valores dos diferentes traços linguísticos da seguinte forma:

Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale 4/5 = 0.8 

Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale 3/5 = 0.6 

Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).
Complexidade de sentença é o número total de frases divido pelo número de sentenças.
Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).
Após calcular esses valores para cada texto, você deve comparar com a assinatura fornecida para os infectados por COH-PIAH. O grau de similaridade entre dois textos, aa e bb, é dado pela fórmula:

![Equation](https://i.ibb.co/YPTGTBT/render.png)



Onde:

* Sab é o grau de similaridade entre os textos aa e bb

* ![fia](https://i.ibb.co/ftPj7dL/fia.jpg)é o valor de cada traço linguístico ii no texto aa


* ![fib](https://i.ibb.co/1JZ2Mvb/fib.jpg)é o valor de cada traço linguístico ii no texto bb

