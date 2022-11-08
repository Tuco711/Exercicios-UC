#Desasfio do professor
#Jogo consistem em um numero de pedras e um numero max de pedras que pode se tirar por jogada;
#Aquele jogador que tirar a ultima pedra vence o jogo.

def jogo (n_pedras, n_max_tirar):
   
    print(f"O numoero de pedras é {n_pedras}")
    
    while n_pedras > 0:
        tira = int(input("Quantas pedras quer tirar?"))
        
        if tira <= n_max_tirar:
            n_pedras -= tira
            if n_pedras > 0:
                print (f"o numero de pedras restantes é {n_pedras}")
            elif n_pedras <= 0:
                print("Voce ganhou!")
                break
            else: continue
        
        else:
            print("numero invalido, digite outro!!")


jogo(20, 5)
