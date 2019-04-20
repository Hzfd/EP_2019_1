from random import randint
# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Hélio Zaia Franciscon, heliozf@al.insper.edu.br 
# - aluno B: Breno Eboli, brenove@al.insper.edu.br
#problemas:
#sistema de combate não funciona
#jogador pode pegar as chaves o quanto quiser
#monstro não some depois do ataque, e não tem jeito de derrota-lo
#inventário não está funcionando
#fazer a parte do aluno B
inventario=[]
nome = input("Digite o seu nome: ")
jogador = [5, 3, 3, inventario, nome]
nomes=["Monstro de Acrílico","Rei dos Armários","Josicreide"]
premios=["hp","escudo"]
def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor",
                "explorar":"você explora o andar"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "andar": "Andar pela biblioteca"
            }
        },
        "andar": {
                "titulo": "andar na biblioteca",
                "descricao": "você está andando na biblioteca quando derrepente encontra um alçapão",
                "opcoes":{
                    "Inicio":"Voltar para o saguao de entrada",
                    "entrar":"entrar no alçapão"
            }
        },
        "entrar":{
                "titulo":"alçapão",
                "descricao": "você entra em um alçapão, é meio escuro, mas você consegue enxergar, ao explorar o alçapão você encontra uma alavanca,Puxar a alavanca?",
                "opcoes": {
                    "puxar":"Puxa a alavanca",
                    "nao":"voltar para o inicio"
            }
        },
        "puxar":{
                "titulo":"você escolheu puxar a alavanca",
                "descricao":"voce puxa a alavanca, escuta um barulho metalico e percebe que uma chave caiu no chão,aparentemente você pode pegar quantas chaves quiser, que legal!!!, e parece que você desbloqueoou um sistema de teletransporte, toda vez que quiser se mover rapidamente pelo mapa, basta vir aqui",
                "opcoes":{
                        "inicio":"voltar ao saguão de entrada",
                        "chave":"pega a chave que caiu no chao",
                        "tp":"teletransporta para qualquer lugar do mapa"
            }
        },
        "tp":{
                "titulo":"O teletransporte",
                "descricao":"você desbloqueou o teletransporte, venha aqui sempre que quiser se mover rapidamente pelo mapa",
                "opcoes":{
                        "inicio":"voltar para o saguão de entrada",
                        "andar professor":"ir para o andar do professor",
                        "biblioteca":"ir para a biblioteca"
                        
           } 
        },
        "explorar":{
                "titulo":"o monstro do andar",
                "descricao":"você esta andando tranquilamente até que um estrondo te assusta, sua visão se turva e ao recobrar os sentindos você se depara com um monstro,se ele te acertar 3 vezes é o seu fim, SUA VIDA ESTÁ EM JOGO!!!",
                "opcoes":{
                          "pular da janela":"é uma decisão arriscada, porém seu desespero é maior",
                          "correr de volta para o saguão":"você está com medo e decide correr de volta ao saguão",
                          "enfrentar o monstro":"você tira coragem de algum lugar e decide enfrentar o mostro à sua frente"
            } 
        },
        "pular da janela":{
                "titulo":"você decidiu pular da janela",
                "descricao":"você corre e pula da janela a queda, apesar de pequena, foi fatal",
                "opcoes":{}       
        },
        "correr de volta para o saguão":{
                "titulo":"Corre irmão",
                "descricao":"você fica com medo e corre o mais rapido que pode de volta para o saguão, sua fuga foi um sucesso, porém o monstro ainda está lá",
                "opcoes":{
                        "inicio":"você está no saguao de entrada novamente"
            }
        },
        "enfrentar o monstro":{
                "titulo":"O monstro do andar",
                "descricao":"Você derrotou o monstro, PARABENS!!!",
                "opcoes":{
                        "inicio":"volta para o saguão de  entrada",
                        "continuar a explorar":"agora que o mosntro ja se foi, por enquanto, você pode explorar mais o andar",
                        "pular da janela":"não parece uma boa ideia"
            }         
        },
        "continuar a explorar":{
                "titulo":"O Armario misterioso",
                "descricao":"você eliminou o monstro temporariamente, ao continuar explorando o andar, encontrou um armario fora do normal, o que pode haver dentro dele?",
                "opcoes":{
                        "abrir o armario":"você tenta abrir o armario",
                        "inicio":"volta ao saguão de entrada, porém o monstro resurge"
            }
        },
        "abrir o armario":{
                "titulo":"o armario misterioso",
                "descricao":"você encontrou um armario meio estranho, o que ele pode conter?",
                "opcoes":{
                        "tentar abrir o armario":"voce tenta abrir o armario",
                        "inicio":"voltar ao saguão de entrada"
            }
        },
        "tentar abrir o armario":{
                "titulo":"O armario misterioso",
                "descricao":"você tenta abrir o armario, porém uma chave é necessaria",
                "opcoes":{
                        "inicio":"voltar ao inicio"
           }
       },
       "dar o laptop":{
               "titulo":"A barganha",
               "descricao":"você conversa com o professor Toshi e barganha com ele, ao dar o laptop do ben 10 para ele você nota que ele fica extremamente feliz, e aproveitando desse momento de euforia do professor, você o convence a mudar a data de entrega do ep, meus parabéns você conseguiu!!!!",
               "opcoes":{
                       "ir pra casa fazer o ep":"você vai pra casa fazer o ep para acabar o quanto antes e conseguir entregar no prazo"
           }
       },
       "ir pra casa fazer o ep":{
               "titulo":"O ep",
               "descricao":"você foi para susa casa e se empenhou em fazer o ep",
               "opcoes":{
                       "fazer o ep":"faz o ep pra entregar em dia dessa vez"
           }
       },
       "falar com o professor":{
                        "titulo":"O professor",
                        "descricao":"O professor Toshi está calmo na sala dele, melhor não irrita-lo falando de adiar o ep, a não ser que você tenha algo para barganhar",
                        "opcoes":{
                                "dar o laptop":"você da o laptop do ben 10 pro professor na esperança de que com isso ele adie o ep",
                                "desistir":"desiste da ideia e volta para o saguão, sabendo que não terá tempo de acabar o ep, a derrota é certa"
             }
       },
       "desistir":{
               "titulo":"O sem esperança",
               "descricao":"você desistiu de tentar barganhar com o professor, foi para casa e n entregou o ep, você perdeu",
               "opcoes":{}
       }
    }        
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
            
                #print(cenarios['biblioteca'])
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
        
            
    
    
