#### Calculadora Gráfica Programada via Python com o Uso do Pacote Tkinter, feito por Bruno Luis dos Santos Costa e Pedro Poliselli Corrêa.
###
##
#

#
## O comando abaixo serve para importar pacotes importantes para serem utilizados no programa. tkinter é o nome de um pacote utilizado para gerar programas com interface gráfica em janela.

from tkinter import *

### Abaixo estamos montando a janela da calculadora.
##
# Aqui é criado o objeto principal que será utilizado. Informalmente, ele é o objeto da nossa janela onde estará presente a calculadora. Tal objeto será denominado janelatkinter. utilizando do comando .title, adicionamos um nome ao nosso programa que estará visível na janela da calculadora (Calculadora Tkinter). Utilizando do comando .geometry determinamos a resolução padrão da nossa janela, e com o comando .resizable determinamos que a janela possa ser aumentada e diminuída horizontalmente e verticalmente.

janelatkinter = Tk()
janelatkinter.title('Calculadora Tkinter')
janelatkinter.geometry('320x480')
janelatkinter.resizable(1,1)

#
## 
### Abaixo estamos definindo uma variável que será uma string. Uma string, informalmente falando, é um texto, diferindo essencialmente de uma entrada numérica. É muito utilizada para armazenar dados e para gerar interfaces intuitivas, como é o nosso caso. a variável será denominada stringnumericaP, apenas estamos definindo ela como uma string que virá a ser preenchida.

stringnumericaP = ''

### Abaixo definimos diversas funções
## Nesta parte são definidas diversas funções com diversos objetivos, o def é o comando utililzado para definir a função. 
# como a stringnumericaP é utilizada como variável global (aparece em mais de uma função), devemos utilizar global antes de fazer referência a ela.

# A função juntastrings será utilizada para adicionar valores a variável global, e, mais formalmente, juntar duas strings em apenas uma, gerando ao final uma string que contenha as operações e números que o usuário deseja fazer. a variável numeroouop é relativa a entrada que será dada pelo usuário, de um número ou operação.
def juntastrings(numeroouop):
    global stringnumericaP
    stringnumericaP = stringnumericaP + str(numeroouop)
    tela['text'] = stringnumericaP

# A função limpar redefine a variável global stringnumericaP como uma string vazia, possibilitando que novas operações sejam feitas.
def limpar():
    global stringnumericaP
    stringnumericaP = ''
    tela['text'] = stringnumericaP

# A função fazerconta redefine a variável global, como a limpar, mas antes determina o valor final da conta, que está em valorfinal.
def fazerconta():
    global stringnumericaP
    valorfinal = str(eval(stringnumericaP))
    tela['text'] = valorfinal
    stringnumericaP = ''

# Observe que todas as funções acima contêm tela['text']; tal é utilizado justamente para mostrar o que foi feito por comando, como limpar a conta ou adicionar números e operações, na tela efetiva da calculadora. É um label que será definido mais adiante.

#
##
### Abaixo são definidos os frames e um label. frames são objetos que informalmente são espaços onde estarão presentes elementos gráficos, como botões ou avisos. o .pack determina o que o frame irá fazer na janela; com expand=True vai tomar o espaço que estiver disponível para ele na janela e com fill=BOTH irá preencher o espaço horizontalmente e verticalmente. Cada frame, no nosso caso, se tornará uma linha de botões (ou a tela) da calculadora.

frame_0 = Frame(janelatkinter) 
frame_0.pack(expand=True, fill=BOTH)

frame_1 = Frame(janelatkinter) 
frame_1.pack(expand=True, fill=BOTH)

frame_2 = Frame(janelatkinter)
frame_2.pack(expand=True, fill=BOTH)

frame_3 = Frame(janelatkinter)
frame_3.pack(expand=True, fill=BOTH)

frame_4 = Frame(janelatkinter)
frame_4.pack(expand=True, fill=BOTH)

frame_5 = Frame(janelatkinter)
frame_5.pack(expand=True, fill=BOTH)

# Aqui estamos formando um label, objeto que fica presente no frame e é muito utilizado para apresentar textos ao usuário. No nosso caso o label é referente a tela da calculadora. o fundo aparecerá com a cor #595954 (fg) e o texto terá cor branca (bg). a tela ficará no frame_0, textvariable indica que o label é de texto, font indica a fonte do texto, anchor determina que o texto apareça a direita com a opção SE.

tela = Label(
    frame_0,
    textvariable='',
    font=('Arial', 20),
    anchor = SE,
    bg = '#595954',
    fg = 'white' 
    )

tela.pack(expand=True, fill=BOTH)

### Aqui são criados os botões da calculadora.
##
#

# Aqui é definido o botão de inserir o número 1. como na maioria dos casos, o número ou operação será inserido na variável global através da função juntastrings. tem opções semelhantes ao label, com a diferença que temos aqui bd, que determina a grossura da borda dos botões, text, que indica o texto que estará no botão, relief, que determina o tipo de borda do botão, e command, que indica qual comando o botão irá efetuar. Como nossa função é do tipo lambda utilizamos lambda: antes de "chamar" a função juntastrings anteriormente definida.

botao_1 = Button(
    frame_1,
    text='1',
    font=('Arial', 22),
    bd = 5,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: juntastrings(1)
    )

botao_1.pack(expand=True, fill=BOTH, side=LEFT)

# Aqui é definido o botão de inserir o 2.

botao_2 = Button(
    frame_1,
    text='2',
    font=('Arial', 22),
    bd = 5,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: juntastrings(2)
    )

botao_2.pack(expand=True, fill=BOTH, side=LEFT)

# Aqui é definido o botão de inserir o 3.

botao_3 = Button(
    frame_1,
    text='3',
    font=('Arial', 22),
    bd = 5,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: juntastrings(3)
    )

botao_3.pack(expand=True, fill=BOTH, side=LEFT)

# Aqui é definido o botão de inserir o +.

botao_soma = Button(
    frame_1,
    text='+',
    font=('Arial', 22),
    bd=5,
    relief=GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: juntastrings('+')
    )

botao_soma.pack(expand=True, fill=BOTH, side=LEFT)

# Aqui é definido o botão de inserir o 4.

botao_4 = Button(
    frame_2,
    text='4',
    font=('Arial', 22),
    bd = 5,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: juntastrings(4)
    )

botao_4.pack(expand=True, fill=BOTH, side=LEFT)

# Aqui é definido o botão de inserir o 5.

botao_5 = Button(
    frame_2,
    text='5',
    font=('Arial', 22),
    bd = 5,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: juntastrings(5)
    )

botao_5.pack(expand=True, fill=BOTH, side=LEFT)

# Aqui é definido o botão de inserir o 6.

botao_6 = Button(
    frame_2,
    text='6',
    font=('Arial', 22),
    bd = 5,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: juntastrings(6)
    )

botao_6.pack(expand=True, fill=BOTH, side=LEFT)

# Aqui é definido o botão de inserir o -.

botao_sub = Button(
    frame_2,
    text='-',
    font=('Arial', 22),
    bd = 5,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: juntastrings('-')
    )

botao_sub.pack(expand=True, fill=BOTH, side=LEFT)

# Aqui é definido o botão de inserir o 7.

botao_7 = Button(
    frame_3,
    text='7',
    font=('Arial', 22),
    bd = 5,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: juntastrings(7)
    )

botao_7.pack(expand=True, fill=BOTH, side=LEFT)

# Aqui é definido o botão de inserir o 8.

botao_8 = Button(
    frame_3,
    text='8',
    font=('Arial', 22),
    bd = 5,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: juntastrings(8)
    )

botao_8.pack(expand=True, fill=BOTH, side=LEFT)

# Aqui é definido o botão de inserir o 9.

botao_9 = Button(
    frame_3,
    text='9',
    font=('Arial', 22),
    bd = 5,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: juntastrings(9)
    )

botao_9.pack(expand=True, fill=BOTH, side=LEFT)

# Aqui é definido o botão de inserir o *.

botao_mul = Button(
    frame_3,
    text='*',
    font=('Arial', 22),
    bd = 5,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: juntastrings('*')
    )

botao_mul.pack(expand=True, fill=BOTH, side=LEFT)

# Aqui é definido o botão de apagar inserir o ..

botao_ponto = Button(
    frame_4,
    text='.',
    font=('Arial', 22),
    bd = 5,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: juntastrings('.')
)

botao_ponto.pack(expand=True, fill=BOTH, side=LEFT)

# Aqui é definido o botão de inserir o 0.

botao_0 = Button(
    frame_4,
    text='0',
    font=('Arial', 22),
    bd = 5,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: juntastrings(0)
    )

botao_0.pack(expand=True, fill=BOTH, side=LEFT)

# Aqui é definido o botão ^ de inserir **.

botao_elev = Button(
    frame_4,
    text='^',
    font=('Arial', 22),
    bd = 5,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: juntastrings('**')
    )

botao_elev.pack(expand=True, fill=BOTH, side=LEFT)

# Aqui é definido o botão de inserir /.

botao_div = Button(
    frame_4,
    text='/',
    font=('Arial', 22),
    bd = 5,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: juntastrings('/')
    )
    
botao_div.pack(expand=True, fill=BOTH, side=LEFT)

# Aqui é definido o botão para limpar a tela e invocar o comando limpar.

botao_limpar = Button(
    frame_5,
    text='C',
    font=('Arial', 22),
    bd = 5,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = limpar
    )

botao_limpar.pack(expand=True, fill=BOTH, side=LEFT)

# Aqui é definido o botão para fazer as contas; invocar a função fazerconta.

botao_igual = Button(
    frame_5,
    text='=',
    font=('Arial', 22),
    bd = 5,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = fazerconta
    )

botao_igual.pack(expand=True, fill=BOTH, side=LEFT)

# Quando rodamos todos os comandos acima em um terminal do python a janela com a calculadora aparecerá e será completamente funcional; mas o terminal ainda estará aberto e com uma linha para comandos ativa para ser digitada. O comando abaixo, o mainloop(), faz com que nenhuma outra linha para comando seja aberta até que a janela do programa criado (no nosso caso, a calculadora) seja fechada. Além disso, é um comando necessário para que a calculadora abra quando os comandos são invocados via um arquivo .py, que é o nosso caso, dado que o python encerra suas atividades a partir do momento em que roda todos os comandos do arquivo ao invés de deixar aberta uma nova linha de comando.

janelatkinter.mainloop()
