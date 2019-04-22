# -*- coding: utf-8 -*-z
import json
from random import randint
# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Hélio Zaia Franciscon, heliozf@al.insper.edu.br 
# - aluno B: Breno Eboli, brenove@al.insper.edu.br
inventario=[]
nome = input("Digite o seu nome: ")
jogador = [5, 3, 3, inventario, nome]
nomes=["Monstro de Acrílico","Rei dos Armários","Josicreide"]
premios=["hp","escudo"]

def carregar_cenarios():
    with open("aqv_cenarios.py","r",encoding="utf-8") as arquivo_cenarios:
        arquivo=arquivo_cenarios.read()
    cenarios=json.loads(arquivo)
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual
#codigo de sistema de combate e prêmios abaixo
nomes=["Monstro de Acrílico","Rei dos Armários","Vergs, o terrível"]
premios=["hp","escudo"]

def combate(n_mon, v_mon, a_mon, d_mon):
    global jogador
    if "espada" in jogador[3]:
        jogador[1] += 1
    if "hp" in jogador[3]:
        jogador[0] += 2
    if "escudo" in jogador[3]:
        jogador[2] += 2

    print("Título: A luta contra " + n_mon + "\n")
    while v_mon > 0 and jogador[0] > 0:
        print("------------------------------------\n"+
              "Nome: "+jogador[4]+"; Vida: "+str(jogador[0])
              +"; Ataque: "+str(jogador[1])+"; Defesa: "+str(jogador[2])+"\n\n"+
              "-------------------------------------------\n"+
              "Nome: "+n_mon+"; Vida: "+str(v_mon)
              +"; Ataque: "+str(a_mon)+"; Defesa: "+str(d_mon)+"\n\n"+
              "opções:\n"+"1 - atacar\n2 - Defender")
        opcao=(input(">> "))
        if opcao=='1':
            dano= jogador[1]-d_mon
            if dano<0:
                dano=0
            v_mon-=dano
            dano=a_mon-jogador[2]
            if dano<0:
                dano=0
            jogador[0]-=dano
        elif opcao=="2":
            dano=a_mon-(jogador[1]+jogador[2])
            if dano<0:
                dano=0
            jogador[0]-=dano
    if v_mon<=0:
        print("você venceu, parabéns")
        p = premios[randint(0,len(premios)-1)]
        inventario.append(p)
        print("Você ganhou " + p)
        return True
    else:
        return False

def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False 
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        # Aluno A: substitua este comentário pelo código para imprimir 
        # o cenário atual.
        #título do cenario
        print (cenario_atual["titulo"])
        print('-'*len(cenario_atual['titulo']))
        print(cenario_atual["descricao"])
        for o,p in cenario_atual['opcoes'].items():
            print('opção:')
            print(o,':',p)
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário
            escolha=input('digite sua opção: ')
            
            #cod principal:
            for b,c in cenarios['biblioteca'].items():
                    print('opção:')
                    print(b,':',c)
            if escolha=="puxar":
                inventario.append('chave')
                print(inventario)
            elif escolha=='andar professor':
                print(cenarios['andar professor'])
                for e,f  in cenarios['andar professor'].items():
                    print('opção:')
                    print(e,':',f)
            elif escolha=="explorar":
                print(cenarios['explorar'])
                for k,i in cenarios['explorar'].items():
                    print('opção')
                    print(k,':',i)
            elif escolha=="abrir o armario":
                inventario.append("leptop do ben 10")
                print("inventario:",inventario)
            elif escolha=='enfrentar o monstro':
                mon = nomes[randint(0,len(nomes)-1)]
                resultado = combate(mon,randint(1,3),randint(1,3),randint(1,jogador[1]-1))
                if not resultado:
                    game_over = True
            elif "chave" in inventario:
                cenarios["abrir o armario"]={
                "titulo":"O armario misterioso",
                "descricao":"Você decide abrir o armario,usando a chave encontrada na bilbioteca. Ao abrir você encontra um item, aparentemente um laptop do ben 10, o que isso estaria fazendo ali?",
                "opcoes":{
                        "falar com o professor":"você vai até a sala do professor tentar barganhar com ele"
                        }
                }
                print("inventario:",inventario)
            if escolha=="fazer o ep":
                print("você faz o ep e entrega na data, VOCÊ CONSEGUIU!!!!")
                break
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
                print("Você morreu!")


# Programa principal.
    
if __name__ == "__main__":
    main()
        
            
    
    
