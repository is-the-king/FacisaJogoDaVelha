'''Linguagem de programação
Atividade Avaliativa II
Reunidos em grupos de até 5 pessoas, os alunos devem elaborar e implementar o código de um Jogo da Velha. O código fonte da aplicação deve ser enviado em arquivo texto,
podendo também ser utilizado o arquivo do programa de desenvolvimento recomendado nas orientações em vídeo disponíveis no matéria da disciplina(links abaixo).
No arquivo de texto deve constar a identificação dos componentes do grupo.
Jogo da velha em meu repositorio do github: https://github.com/smile-dev-Gos/FacisaJogoDaVelha
INTEGRANTES DO GRUPO:
GLEISON DE OLIVEIRA ADS 3 - Mat 17061
'''
#JOGO DA VELHA, FACISA - GLEISON DE OLIVEIRA ADS 3.
print('Repositorio github: https://github.com/smile-dev-Gos/FacisaJogoDaVelha')
print('  ___     _      ___   ___   ___     _  ')
print(' | __|   /_\    / __| |_ _| / __|   /_\ ')
print(' | _|   / _ \  | (__   | |  \__ \  / _ \ ')
print(' |_|   /_/ \_\  \___| |___| |___/ /_/ \_\ ')
print('                                         ')

print('   ___   _         _                     ')
print('  / __| | |  ___  (_)  ___  ___   _ _    ')
print(' | (_ | | | / -_) | | (_-< / _ \ | . \   ')
print('  \___| |_| \___| |_| /__/ \___/ |_||_|  ')
print('')
print('JOGO DA VELHA FACISA - GLEISON DE OLIVEIRA ADS 3')
print('INSTRUÇÕES:')
print('Use o teclado numerico para definir as posições, igual fiz nesse exemplo abaixo')
print('')
print('7' + '|' + '8' + '|' + '9')
print('-+-+-')
print('4' + '|' + '5' + '|' + '6')
print('-+-+-')
print('1' + '|' + '2' + '|' + '3')
print('INICIO DO JOGO')
print('--------------------------------------------------------------------')
print('')
''' Fiz o tabuleiro usando um dicionário
as chaves serão as posições ex: superior esquerdo, superior direito etc.
no início todos os espaços serão vazios 
o movimento alterado será de acordo com a escolha do jogador 
 '''

Tabuleiro = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in Tabuleiro:
    board_keys.append(key)

''' atualizarei o tabuleiro a cada movimento, por isso a função printBoard. '''

def printBoard(board):
    print()
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print()
# Função principal .
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(Tabuleiro)
        print("É sua vez," + turn + ".Para qual lugar quer mover?")

        move = input()        

        if Tabuleiro[move] == ' ':
            Tabuleiro[move] = turn
            count += 1
        else:
            print("Esse lugar já está preenchido. \ Mover para qual lugar?")
            continue

        # verificar se o jogador X ou O ganhou, para cada jogada após 5 jogadas.
        if count >= 5:
            if Tabuleiro['7'] == Tabuleiro['8'] == Tabuleiro['9'] != ' ': # Passou do Topo
                printBoard(Tabuleiro)
                print("\nFim De Jogo.\n")                
                print(" **** " +turn + " Ganhou. ****")                
                break
            elif Tabuleiro['4'] == Tabuleiro['5'] == Tabuleiro['6'] != ' ': # No Meio
                printBoard(Tabuleiro)
                print("\nFim De Jogo.\n")                
                print(" **** " +turn + " Ganhou. ****")
                break
            elif Tabuleiro['1'] == Tabuleiro['2'] == Tabuleiro['3'] != ' ': # através do fundo
                printBoard(Tabuleiro)
                print("\nFim De Jogo.\n")                
                print(" **** " +turn + " Ganhou. ****")
                break
            elif Tabuleiro['1'] == Tabuleiro['4'] == Tabuleiro['7'] != ' ': # abaixo do lado esquerdo
                printBoard(Tabuleiro)
                print("\nFim De Jogo.\n")                
                print(" **** " +turn + " Ganhou. ****")
                break
            elif Tabuleiro['2'] == Tabuleiro['5'] == Tabuleiro['8'] != ' ': # Pelo meio
                printBoard(Tabuleiro)
                print("\nFim De Jogo.\n")                
                print(" **** " +turn + " Ganhou. ****")
                break
            elif Tabuleiro['3'] == Tabuleiro['6'] == Tabuleiro['9'] != ' ': # desça pelo lado direito
                printBoard(Tabuleiro)
                print("\nFim De Jogo.\n")                
                print(" **** " +turn + " Ganhou. ****")
                break 
            elif Tabuleiro['7'] == Tabuleiro['5'] == Tabuleiro['3'] != ' ': # diagonal
                printBoard(Tabuleiro)
                print("\nFim De Jogo.\n")                
                print(" **** " +turn + " Ganhou. ****")
                break
            elif Tabuleiro['1'] == Tabuleiro['5'] == Tabuleiro['9'] != ' ': # diagonal
                printBoard(Tabuleiro)
                print("\nFim De Jogo.\n")                
                print(" **** " +turn + " Ganhou. ****")
                break 

        # Quando empata '.
        if count == 9:
            print("\nFim De Jogo.\n")                
            print("É um empate!!")

        # Mudar depois de movimentar.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Reiniciar ?.
    restart = input("Quer jogar de novo? (S / n)")
    if restart == "s" or restart == "S":  
        for key in board_keys:
            Tabuleiro[key] = " "

        game()

if __name__ == "__main__":
    game()
