""" Projet codage : Malespin """


def malspin_code():
     print("voici le message clair :",msg)
     message_chiffre= [] #le messeage chiffré

     for ele in msg:
         
         if ele  == "a":
              message_chiffre.append("e")
         elif ele  == "b":
              message_chiffre.append("t")
         elif ele  == "f":
              message_chiffre.append("g")
         elif ele  == "i":
              message_chiffre.append("o")
         elif ele  == "m":
              message_chiffre.append("p")
         elif ele  == "o":
              message_chiffre.append("i")
         elif ele  == "g":
              message_chiffre.append("f")
         elif ele== "t":
              message_chiffre.append("b")
         elif ele == "e":
              message_chiffre.append("a")
         elif ele  == "p":
              message_chiffre.append("m")
         else:
              message_chiffre.append(ele)
     # on convertit le messaage chiffre en chaine de caractère
     print(" voici le message chiffré :","".join(message_chiffre))
msg =list(input("")) # le message clair
malspin_code()