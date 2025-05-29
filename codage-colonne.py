"""                     projet coadage : code Colonne            """


def colonne_cipher():

    
    print("voici le message clair :",message) # message clair
    if column_count == len(column_order):
            lines =[] 
            line_count = list(message + '+' * (column_count - (len(message) % column_count)))  # on découpe le messeage et on ajoute un  +  si len(message) != la clef  
            print(line_count)
            line_number=[line_count[colonne_no:colonne_no+ column_count] for colonne_no in range(0, len(line_count), column_count)] # on détermine  le nombre de collone dans une ligne
            error=['+']*column_count
            for ele in lines:

                if ele==error:
                        lines.remove(ele)  # pour éviter l'errueur 
            print("voici le message dans un tableeau :",line_number)
            
            for cle in line_number:  

                for order in column_order :

                    assert int(order)>0

                    try:
                        lines.append( cle[int(order)-1],)

                    except IndexError:
                        print("on ne peut pas le chiffré")
                        break

                    except ValueError:
                        print("on ne peut pas le chiffré")
                        break
                    
                    except AssertionError:
                        print("on ne peut pas le chiffré")
                        break                   
                
            print("voici le messeage chiffré dans un tableau :",lines) # message chiffré
            chaine="".join(lines)
            print("voici le messeage chiffré :",chaine)       # on convertit en chaine de cara
    else: 
        print("?")

message=input("quel est le message")
column_count=int(input("quel est la cle numero 1")) # la clef 01 : Un nombre (non nul) représentant le nombre de colonnes
column_order=list(input("quel est la cle numero 2")) #  la clef 02 :Un nombre d’autant de chiffre que de colonne représentant la permutation des colonnes

colonne_cipher()