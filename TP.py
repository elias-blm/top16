import matplotlib.pyplot as plt
from collections import Counter
def extraction_donnees():
    '''
    Fonction qui transforme le fichier .csv en liste contenant les informations utiles
    '''

    listeall = open("JoueursTop14.csv", "r", encoding='utf8') #ouvre le fichier
    listeall = listeall.readlines()#prends chaque ligne et la transforme en sous liste

    del listeall[0] #supprime le premier item
    for i in range(0, len(listeall)): #analyse chaque element de la liste
        listeall[i] = listeall[i].rstrip('\n') #retire les sauts de ligne
        listeall[i] = listeall[i].split(';') #cree des sous items pour chaque élement (taille, poids, poste, équipe)
        del listeall[i][1]
        del listeall[i][3]
        del listeall[i][1] # ces trois lignes suprimment les 3 élément inutiles (le prénom, le poste (!= type de poste), et la date de naissance)
        listeall[i][2]=int(listeall[i][2]) 
        listeall[i][3]=int(listeall[i][3])#ces 2 lignes transforment la taille et le poids en nombre entiers
        listeall[i][0]=str(listeall[i][0]).upper() #transforme le nom de l'équipe en chaîne de caractère majuscule
    
    return listeall #retourne la liste

def extraire_equipe (listeall,team):
    '''
    fonction qui extrait les données d'une équipe dans l'ensemble de la liste
    '''
    liste_team=[] #crée une liste vide
    

    for i in range(0, len(listeall)): #analyse chaque élément de la liste
        if listeall[i][0]== team: #si l'équipe dans la liste correspond à celle recherchée
            liste_team.append(listeall[i]) #on l'ajoute à la liste contenant les données de l'équipe
   
            
    return liste_team #retourne contenant les données de l'équipe
   
def représentation(liste_team):
    '''
    fonction qui crée un repère avec les différents types de postes en fonction de la taille (x) et du poids (y)
    '''
    avantx=[]
    avanty=[]
    deuxiemelignex=[]
    deuxiemeligney=[]
    troisiemelignex=[]
    troisiemeligney=[]
    demix=[]
    demiy=[]
    troisquartsx=[]
    troisquartsy=[]
    arrièrex=[]
    arrièrey=[]
    #créee plusieurs listes qui contiendront les abscisses et ordonnéees pour chaque type de poste
    for i in range(0, len(liste_team)):  #pour chaque élément de la liste, ajoute les données(taille en abscisses et poids en ordonnées) à la liste correspondant au poste  
        if liste_team[i][1]=='Avant':
            avantx.append(liste_team[i][2])
            avanty.append(liste_team[i][3])
        if liste_team[i][1]=='2ème ligne':
            deuxiemelignex.append(liste_team[i][2])
            deuxiemeligney.append(liste_team[i][3])
        if liste_team[i][1]=='3ème ligne':
            troisiemelignex.append(liste_team[i][2])
            troisiemeligney.append(liste_team[i][3])
        if liste_team[i][1]=='Demi':
            demix.append(liste_team[i][2])
            demiy.append(liste_team[i][3])
        if liste_team[i][1]=='Trois-Quarts':
            troisquartsx.append(liste_team[i][2])
            troisquartsy.append(liste_team[i][3])
        if liste_team[i][1]=='Arrière':
            arrièrex.append(liste_team[i][2])
            arrièrey.append(liste_team[i][3])
    maxdesx=max([max(avantx),max(deuxiemelignex),max(troisiemelignex),max(demix),max(arrièrex)])
    maxdesy=max([max(avanty),max(deuxiemeligney),max(troisiemeligney),max(demiy),max(arrièrey)])
    mindesy=min([min(avanty),min(deuxiemeligney),min(troisiemeligney),min(demiy),min(arrièrey)])
    mindesx=min([min(avantx),min(deuxiemelignex),min(troisiemelignex),min(demix),min(arrièrex)])
    #ces quatres fonctions recherchent le maximum et minimum en ordonnées et abscisses
    
    plt.grid(True) #affiche une grille pour la légende
    plt.plot(avantx, avanty, "bs", marker="*", label="Avant")# prend les listes associées au poste, crée un nuage de points dont les points sont une certaine couleur et un figuré spécifique. Dans la légende, le poste associé sera affiché comme légende
    plt.plot(deuxiemelignex, deuxiemeligney, "rs", marker="o", label="Deuxième ligne")
    plt.plot(troisiemelignex, troisiemeligney, "gs", marker="1", label="Troisième Ligne")
    plt.plot(demix, demiy, "ys", marker="p", label="Demi")
    plt.plot(troisquartsx, troisquartsy, "ks", marker="h", label="Trois Quarts")
    plt.axis([mindesx-20, maxdesx+20, mindesy-20, maxdesy+20]) #les deux axes des ordonnées et des abscisses auront comme maximum et minimum les maximums+20 et minimums-20 comme étendue
    plt.xlabel('Taille') #nom de laxe des abscisses
    plt.ylabel('Poids') #nom de l'axe des ordonnées
    plt.legend() #affiche la légende pour l'axe x et y   
    plt.show() #affiche le graphique
    return

def classification(liste_team,joueurx,joueury,e):
    '''
    fonction qui recommande un poste en fonction des statistiques des autres joueurs de l'équipe via la distance
    '''
    ensemble=[]
    dist1=0
    for i in range(0,len(liste_team)): #analyse toute la liste
        dist1=distance(liste_team[i][2],liste_team[i][3],joueurx,joueury) #calcule la distance
        prop=liste_team[i][1],dist1 #variable contenant le poste et la distance
        ensemble.append(prop) #l'ajoute à la liste ensemble
    ensemble=sorted(ensemble, key=lambda colonnes: int(colonnes[1])) #tri la liste en fonction de la distance 
    nombreoccurences(ensemble,e) #lance la fonction
    return

def distance(averagex,averagey,joueurx,joueury):
    '''
    fonction qui calcule la distance
    '''
    distance=((joueurx-averagex)**2+(joueury-averagey)**2)**0.5 #calcule la distance entre la donnée rentrée par l'utilisateur et celle dans la liste
    return distance

def classification_efficace(liste,x,y,e):
    '''
    fonction qui recommande un poste en fonction des statistiques des autres joueurs de l'équipe via la différence entre le poids et la taille des joeueurs et celle rentrée par l'utilisateur 
    '''
    print('On essaye avec une autre méthode')
    tri=[['poste',100000]]*e

    for k in range(0,len(liste)):
        z=((x-liste[k][2])**2)**0.5 #calcule la différence entre la taille
        u=((y-liste[k][3])**2)**0.5 #calcule la différence entre la taille
        total=z+u #additionne les deux valeurs
        item=[liste[k][1],total] #cree une liste contenant le poste et le total calculé plus tôt
        tri.append(item) #on ajoute la liste 'item'
        tri=sorted(tri, key=lambda colonnes: int(colonnes[1])) #on tri la liste par ordre croissant en fonction des differents totaux
        tri.pop() #on supprime la dernière liste (total le plus grand)
    nombreoccurences(tri,e) #lance la fonction

def nombreoccurences(liste,k):
    '''
    compte le nombre d'occurences d'un mot
    '''
    tri=[]
    for i in range (0,k):
        tri.append(liste[i][0]) #on ajoute le poste des k joueurs dont la distance/total est la plus proche de 0
    cnt = Counter(tri) #compte le nombre d'occurence d'un des postes et le transforme en dictionnaire  
    maxi = False
    for k in cnt:
        if maxi ==False or cnt[k] > maxi: #si la valeur du dictionnaire est plus grande que celle dans maxi ou que maxi est égal à False
            maxi = cnt[k]
    key_list = [k  for (k, val) in cnt.items() if val == maxi] #récupère la clé associée à la valeur maximale (maxi)
    print('Le Joueur devrait jouer en tant que :',key_list[0]) #recommande le poste qui a le plus d'occurence

#Pour l'utilisateur final
#team=str(input('Quelle équipe?')).upper() #demande le nom de l'équipe recherchée et la transforme en majuscule
#k= int(input("A combien de joueurs voulez-vous comparer? "))
#listeall= extraction_donnees()
#liste_team= extraire_equipe(listeall)
#représentation(liste_team)
#joueurx=int(input("Entrez la taille (en cm)"))
#joueury=int(input("Entrez le poids (en kg)"))
#classification(liste_team,joueurx,joueury,k)
#classification_efficace(liste_team,joueurx,joueury,k)

#Pour la correction
k=3
team="TOULOUSE" #demande le nom de l'équipe recherchée et la transforme en majuscule
listeall= extraction_donnees()
liste_team= extraire_equipe(listeall,team)
représentation(liste_team)
joueurx=180
joueury=90
classification(liste_team,joueurx,joueury,k)
classification_efficace(liste_team,joueurx,joueury,k)
