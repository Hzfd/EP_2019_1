# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Hélio Zaia Franciscon, heliozf@al.insper.edu.br 
# - aluno B: Bruno Eboli, brunove@al.insper.edu.br

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
                "professor": "Falar com o professor"
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
                    "sim, puxar alavanca":"Puxa a alavanca",
                    "nao, nao puxar a alavanca":"voltar para o inicio"
            }
        },
        "sim, puxar alavanca":{
                "titulo":"você escolheu puxar a alavanca",
                "descricao":"voce puxa a alavanca, escuta um barulho metalico e percebe que uma chave caiu no chão, você pega a chave",
                "opcoes":{
                        "inicio":"voltar ao saguão de entrada"
            }           
        }
    }        
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


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
    inventario=[] 
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        # Aluno A: substitua este comentário pelo código para imprimir 
        # o cenário atual.
        #título do cenario
        print (cenario_atual["titulo"])
        print("----------------------")
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
            
            if escolha=='biblioteca': 
                #print(cenarios['biblioteca'])
                print('------------------------')
                for b,c in cenarios['biblioteca'].items():
                    print('opção:')
                    print(b,':',c)
            elif escolha=="sim, puxar alavanca":
                inventario.append('chave')
                print(inventario)
                
            elif escolha=='andar professor':
                print(cenarios['andar professor'])
                for e,f  in cenarios['andar professor'].items():
                    print('opção:')
                    print(e,':',f)
            
       
            
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
    
if __name__ == "__main__":
    main()
        
                
    
    
