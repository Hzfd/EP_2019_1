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
                "descricao":"você corre, passa pelo monstro e pula da janela numa tentativa de se salvar, porém a queda, apesar de pequena, foi fatal",
                "opcoes":{}       
        },
        "correr de volta para o saguão":{
                "titulo":"Corre irmão",
                "descricao":"você fica com medo e corre o mais rapido que pode de volta para o saguão, sua fuga foi um sucesso, porém o monstro ainda está lá",
                "opcoes":{
                        "inicio":"você está no saguao de entrada novamente"
            }
        },
                #ALTERAR AS OPÇÕES
        "enfrentar o monstro":{
                "titulo":"Você ganhou!",
                "descricao":"Você está no andar do professor",
                "opcoes":{
                        "bater":"da um ataque básico no adversário",
                        "bater forte":"ataca o adversário com mais força e alguns golpes a mais",
                        "bater muito forte":"Usa um combo de golpes no monstro"
            }
        },
                #ESSES CENÁRIOS DE COMBATE N EXISTEM MAIS
        "bater muito forte":{
                "titulo":"O exagero",
                "descricao":"você tenta bater muito forte no monstro, porém ao exagerar na força, você se desequilibra e cai, o monstro aproveita a brecha.............você morreu (D:)",
                "opcoes":{}
        },
        "bater":{
                "titulo":"A luta",
                "descricao":"você bate no monstro e reduz levemnete a sua vida, porém o monstro te atinge e te machuca levemente",
                "opcoes":{
                        "bater":"bate novamente no montro",
                        "bater forte":"bate com força no monstro"
                        }
        },
        "bater forte":{
                "titulo":"A luta",
                "descricao":"você bate com força no monstro, tirando uma quantidade aleatoria de vida, o monstro tambem te acerta te machucando levemente",
                "opcoes":{
                        "bater":"bate no monstro",
                        "bater forte":"bate com força no monstro"
            }         
        }       
    }        
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual
#codigo de sistema de combate e prêmios abaixo
nomes=["Monstro de Acrílico","Rei dos Armários","Josicreide"]
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
            if escolha=="sim, puxar alavanca":
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
            elif escolha=='enfrentar o monstro':
                mon = nomes[randint(0,len(nomes)-1)]
                resultado = combate(mon,randint(1,3),randint(1,3),randint(1,jogador[1]-1))
                if not resultado:
                    game_over = True
                '''monstro= True
                life=3
                life_monstro=5
                print('sua vida:',life,'/','vida do monstro:',life_monstro)
                print(cenarios['enfrentar o monstro'])
                for a1,a2 in cenarios['enfrentar o monstro'].items():
                         print('opção:')
                         print(a1,':',a2)
                 #consertar o sistema de combate      
                cenario_atual=cenarios['enfrentar o monstro']        
                while life_monstro>=0:
                    print (cenario_atual["titulo"])
                    print('-'*len(cenario_atual['titulo']))
                    print(cenario_atual["descricao"])
                    for o,p in cenario_atual['opcoes'].items():
                        print('opção:')
                        print(o,':',p)
                    opcoes = cenario_atual['opcoes']
                    escolha=input('digite sua opção: ')
                    print('sua vida:',life,'/','vida do monstro:',life_monstro)
                    print(cenarios['enfrentar o monstro'])
                    for a1,a2 in cenarios['enfrentar o monstro'].items():
                             print('opção:')
                             print(a1,':',a2)
                    if life<=0:
                        print('o monstro te derrotou')
                        game_over= True
                    elif escolha=='bater':
                        life_monstro-=1
                        life-=1
                    elif escolha=='bater forte':
                        life_monstro-=3
                        life-=1
                        print(life_monstro)
                    if life_monstro<=0:
                        print('você derrotou o monstro, parabens!!!')
                        cenarios=cenarios['inicio']
                        break'''
            
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
    
if __name__ == "__main__":
    main()
        
            
    
    
