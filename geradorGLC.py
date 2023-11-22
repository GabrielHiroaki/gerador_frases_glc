# Alunos:
# Gabriel Hiroaki Da Silva Kanezaki, 179292
# Luiz Felipe Teodoro Monteiro, 177210

# Trabalho referente ao Gerador de Frases com GLC
# que consiste em efetuar as devidas manipulações
# com a nossa gramatica, e gerar frases no portugues
# corretamente, por fim, gerar uma árvore de derivação.

# Instrução de uso:
# 1 - Executar o arquivo “geradorGLC.py” e clicar em gerar.

# Observação: 
# 1 - Como nosso código está criado em partes, deve-se rodar 
# apenas o arquivo geradorGLC.py para rodar corretamente.

import tkinter as tk
import tkinter.messagebox 
import RandomText
import os

bg = 'grey'
cms = ('terminal', 17, 'bold')

# função para manipular nossos dados (gramatica)
# recebida da função GeraOracao(), e utilizando
# uma interface gráfica mediante ao Tkinter
def random():
    oracao = RandomText.GeraOracao()
    oracao.GeraOracao('O')
    aux = ''
    # laço para corrigir e ajustar de maneira
    # que nossa frase fique correta
    for i in oracao.frase:
        if i == 'o' or i == 'a' or i == '.' or i == 'as' or i == 'os' or i == 'm' or i == ',' or i == 'r':
            aux += i
        else:
            aux += ' ' + i
        if i == ',':
            aux += '\n'
    os.system('cls' if os.name == 'nt' else 'clear')
    
    arvore = oracao.criaArvore(dot = False)
    
    # parte gráfica do nosso programa
    root_random = tk.Tk()
    root_random.resizable('False', 'False')
    root_random['bg'] = 'light grey'
    root_random.title('Frase Aleatoria')

    txt = tk.Label(root_random, text = f'{aux}', font = cms, bg = 'light grey').grid()

    tk.Label(root_random, text = f'Arvore', font = ('terminal', 20, 'underline'), bg = 'light grey').grid()

    # laço em conjunto utilizando a biblioteca
    # anytree, para desenhar nossa arvore de derivação
    # na nossa interface gráfica
    for pre, fill, node in arvore:
        tk.Label(root_random, text = "%s%s" % (pre, node.name), font = cms, bg = 'light grey').grid(sticky = tk.W)
    
    # função de aviso para mostrar que o arquivo externo
    # foi gerado com sucesso
    def notify(): 
        tkinter.messagebox.showinfo("Alerta!", "Arquivo gerado!!")
    # botão para gerar um arquivo separado do programa
    # para visualização da árvore se necessário
    tk.Button(root_random, text = 'Criar arquivo da arvore', bg = 'gray', font = cms, command = lambda:[oracao.criaArvore(),notify()]).grid()
    tk.Label(root_random, text = f'Obs: apenas a arvore da primeira frase', font = ('terminal', 12, 'bold'), bg = 'light grey', fg = 'red').grid()

root = tk.Tk()
root.resizable('False', 'False')
root['bg'] = bg
root.title('Gerador de Frases')

titulo = tk.Label(root, text = '\n\nGerador de Frases\nUtilizando GLC\n', bg = bg, font = cms)
titulo.pack()

main_frame = tk.Frame(root, bg = bg)
main_frame.pack()

# botão essencial, onde vai efetuar o comando
# random,ou seja, nossa função, que vai gerar 
# nossa frase e a árvore de derivação
enter_random = tk.Button(main_frame, text = 'Gerar', bg = 'light gray', font = cms, command = random)
enter_random.grid(row = 5, column = 1, padx = 100, pady = 1)

root.geometry('300x150')
root.mainloop()
