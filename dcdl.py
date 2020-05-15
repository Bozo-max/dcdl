import renardo
import renarda

def main():
    print('==========')
    choice = ''
    choice = input(" [1] Chiffres \n [2] Lettres \n [3] Quitter \n Faites votre choix : ")
    while True:
        if(choice=='1'):
            renardo.main()
        elif(choice=='2'):
            renarda.main()
        elif(choice=='3'):
            break
        choice = input(" [1] Chiffres \n [2] Lettres \n [3] Quitter \n Faites votre choix : ")

    print('==== Au revoir ====')

if __name__ =="__main__":
    main()
