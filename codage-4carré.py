"""             projet codage : code 4 carré                """

from string import ascii_uppercase as alphabet
# on import l'alphabet en majscule 
listofexecptions = ["’"," ","?","!",",",".",";","j","J"]
charlist = []
listofindexs = []
def standard(string):
    return ''.join(ch for ch in string.upper() if ch in alphabet)
#cette  fonction renvoie la chaine de caractère en majscule 


def create_grid(key):
    base = standard(key) + alphabet
    return ''.join(sorted(set(base), key=base.index))
# on crée un grille et on insère la clef en premier 
def creat_matrice(mystring):
    mamatrice = []
    list = []
    l = 0
    for letter in  mystring:
        if len(list) <= 4 and l <=4 : # il  ne faut pas que dépasse la  5 eme colonne
            list.append(letter) 
        else:
            #sinon retour on creée une autre ligne
            l = l+1
            mamatrice.append(list)
            list = []
            list.append(letter)
        if letter == mystring[-1]:
            mamatrice.append(list)

    return mamatrice

def return_index(matrice,letter):
    ligne =  0
    coll = 0
    for i in range(len(matrice)):
        for y in range(len(matrice[i])):
            if matrice[i][y] == letter: # on cherche les coordonné horizontal  et vertical de la lettre 
                ligne = i
                coll = y
                return ligne,coll

def cipher(clear, key_1, key_2, key_3, key_4):
    for t in listofexecptions:
        while t in clear:
            listofindexs.append(clear.find(t))
            charlist.append(t)
            clear = clear.replace(t,'')
# on supprime les cartères speciaux et la lettre 'j' et on mémorise leur index(clear) dans une liste(charlist)
    
    print("le message clair est :",clear)
    

    matrice_1 = create_grid(key_1)
    matrice_1 = matrice_1.replace('J','')
    matrice_2 = create_grid(key_2)
    matrice_2 = matrice_2.replace('J', '')
    matrice_3 = create_grid(key_3)
    matrice_3 = matrice_3.replace('J', '')
    matrice_4 = create_grid(key_4)
    matrice_4 = matrice_4.replace('J', '')
# on supprime la lettre 'j' dans chaque  matrice (grille)
    creat_matrice(matrice_1)
    clear = standard(clear)
    matrice_1 = creat_matrice(matrice_1)
    matrice_2 =creat_matrice(matrice_2)
    matrice_3 = creat_matrice(matrice_3)
    matrice_4 = creat_matrice(matrice_4)
    print("""
       matrice 1 :
       length : {}
       {}
       matrice 2 :
       {}
       matrice 3 :
       {}
       matrice 4 :
       {}
       """.format(str(len(matrice_1)), matrice_1, matrice_2, matrice_3, matrice_4))
    if len(clear) % 2: #Si à la fin du message il ne reste qu’une lettre  on ajoute un 'x' au message d’origine (un v si celui-ci se termine par un x)

        if clear[-1] == 'X':
            clear += 'V'
        else:
            clear += 'X'
    print("le message qu' on doit chiffré",clear)
    
    ciphered = ''

    for i in range(int((len(clear)/2))): # on découpe le message clair en parties et chaque  partie doit contenir 2 lettres
        if i == 0:
            l = i
            j = 1
        else: # on repère la première lettre dans la grille 1 et la seconde lettre dans la grille 4.  on intersecte les lignes et les colonnes des lettres trouvées jusqu’au deux autres grilles adjacentes et  on note ces 2 nouvelles lettres.
            l = i*2
            j = l + 1      
        index1,index2 = return_index(matrice_1,clear[l])
        index3,index4 = return_index(matrice_4,clear[j])
        premiere_lettre = matrice_2[index1][index4] 
        deuxieme_lettre = matrice_3[index3][index2]
        ciphered += premiere_lettre
        ciphered  += deuxieme_lettre

    if len(charlist)>0:
        for i in range(len(charlist)):
            ciphered = ciphered[:listofindexs[i]]+charlist[i]+ciphered[listofindexs[i]:]

    return ciphered


def main():
    msg = input("entrez votre message ")

    key_1 = input("entrez votre clef 01")# pas de lettre 'j' dans la clef 
    key_2 = input("entrez votre clef 02")# pas de lettre 'j' dans la clef
    key_3 = input("entrez votre clef 03")# pas de lettre 'j' dans la clef
    key_4 = input("entrez votre clef 04")# pas de lettre 'j' dans la clef

    print("voici le message votre :",msg)
    print("le message chiffré est :",cipher(msg, key_1, key_2, key_3, key_4)) 


if __name__ == '__main__':
    main()  
#fonction main qui permet de voir le resultat 
