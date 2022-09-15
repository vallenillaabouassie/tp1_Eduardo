def word_count(string):
    #on va split la phrase a chaque fois qu'il y a un espace
    words = string.split(" ")
    #retournera le nombre de mots dans notre liste
    return len (words)
#Demande de la phrase a l'utilisateur
chaine = input("Ecrivez votre texte: ")
#On va print la phrase "Nombre de mots:" et par la suite le nombre de mots en string
print("Nombre de mots:")
print(word_count(chaine))