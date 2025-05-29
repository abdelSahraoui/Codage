""" Projet codage : beaufort """

def beaufort_cipher():
    print("le message clair est :",msg_clear)

    key=input("clef ?")*((len(msg_clear)-1)//3) # la clef 
    longueur_key= len(msg_clear)- len(key)
    if longueur_key>0 and longueur_key<=1: #on cherche à  déterminer la longueur da la  clef en fonnc de la longueur du message
        key+="c"
    elif longueur_key>1 and longueur_key<=2:
        key+="cl"
    elif longueur_key>2 and longueur_key<=3:
        key+="cle"
    else :
        print("on  ne peut pas le chiffrer")
    print("voici la clef : " , key)
    ciphered=[]
    
    indiceCle=0 
    for i in range(0,len(msg_clear),1):

        if msg_clear[i] =="." or msg_clear[i] =="," or msg_clear[i] =="?" or msg_clear[i] =="!" or msg_clear[i]==";" or msg_clear[i]=="’"or msg_clear[i]==" " :
        #au lieu de passer, on recopie juste le carractere
            ciphered.append(msg_clear[i])
        #on avance pas dans lindice de cle
        else:
            cipher=(ord(msg_clear[i])-97)-(ord(key[i])-97)
            if cipher<0:
                cipher+=26
            else:
               pass
            r=chr(cipher+97)
            ciphered.append(r)    
            indiceCle = indiceCle+1 # indice cle permet de passer à l'indice suivant cle de la clef
    
    print("le message crypté est :","".join(ciphered))
msg_clear=input("entrez votre message ?") # le message qu'on doit chiffrer

beaufort_cipher()

