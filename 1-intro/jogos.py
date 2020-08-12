import adivinhacao as adv
import forca as fc

def escolhe_jogo():
    print("    /////////////////////////////////")
    print("   // Bem vindo! Escolha um jogo: //")
    print("  //  (1) Adivinhação            //")
    print(" //   (2) Forca                 //")
    print("/////////////////////////////////")
    print("       (\__/)  //")
    print("       (•ㅅ•) //")
    print("       ( 　 づ||")

    jogo = int(input("Jogo: "))

    if ( jogo == 1):
        adv.jogar()
    elif ( jogo == 2 ):
        fc.choseAction()
    else:
        print("Opção inválida!")


if ( __name__ == "__main__"):
    escolhe_jogo()