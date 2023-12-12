from tkinter import *
from ia import ia
import random

rond = 1
croix = 0
count = 0
d = {}
of = True #on/off
try :
    player = int(input("1. Vous jouez O\n2. Vous jouez X\n3. PvP\n"))
except :
    print("Entrez un chiffre entre 1 et 3.")
state = player
def start() :
    global d
    lbout = [boutton1,boutton2,boutton3,boutton4,boutton5,boutton6,boutton7,boutton8,boutton9]
    for x in lbout :
        x.config(state=NORMAL)
    boutton.config(state=DISABLED)
    label_play.config(text="Joueur 1 c'est à vous.")
    if player == 2 :
        ia(lbout, d, replace_with_image)

def reset() :
    global d, rond, croix, count, player, state 
    lbout = [boutton1,boutton2,boutton3,boutton4,boutton5,boutton6,boutton7,boutton8,boutton9]
    boutton.config(state=NORMAL)
    rond = 1
    croix = 0
    count = 0
    player = state
    d = {}
    for x in lbout:
        x.config(image="")
    return d

def start_reset() :
    global of
    if of == False :
        reset()
    start()

def replace_with_image(i):
    global rond, croix, count, d, of, player
    of = True
    bout = [boutton1,boutton2,boutton3,boutton4,boutton5,boutton6,boutton7,boutton8,boutton9]
    if rond == 1 and croix == 0 :
        img = PhotoImage(file=r"rond.png")
        bout[i].config(image=img, compound=CENTER, state=DISABLED)
        bout[i].image = img
        d[i] = "rond"
        rond = 0
        croix = 1
        count += 1
        label_play.config(text="Joueur 2 c'est votre tour.")
        gagner()
        if count < 8 and player == 1 :
            ia(bout, d, replace_with_image)
        
    else :     
        img = PhotoImage(file=r"croix.png")
        bout[i].config(image=img, compound=CENTER, state=DISABLED)
        bout[i].image = img
        d[i] = "croix"
        rond = 1
        croix = 0
        count += 1
        label_play.config(text="Joueur 1 c'est à vous.")
        gagner()
        if count < 8 and player == 2 :
            ia(bout, d, replace_with_image)
            
    if count == 9:
            label_play.config(text="Match Nul !")
            boutton.config(text="Recommencer la partie", state=NORMAL)
            of = False
    return of


def gagner() :
    global of, player
    verif = [
        (0,1,2), (3,4,5), (6,7,8), # lignes
        (0,3,6), (1,4,7), (2,5,8), # colonnes
        (0,4,8), (2,4,6) # diagonales    
    ]
    lbout = [boutton1,boutton2,boutton3,boutton4,boutton5,boutton6,boutton7,boutton8,boutton9]
    for combinaison in verif :
        combo_rond = combo_croix = 0
        for x in combinaison :
            if x in d and d[x] == "rond" :
                combo_rond += 1
            elif x in d and d[x] == "croix" :
                combo_croix += 1
        if combo_rond == 3 :
            label_play.config(text="Joueur 1 a gagné !") 
            boutton.config(text="Recommencer la partie", state=NORMAL)
            for j in lbout :
                j.config(state=DISABLED)
            of = False
            player = 0
        elif combo_croix == 3 :
            label_play.config(text="Joueur 2 a gagné !")
            boutton.config(text="Recommencer la partie", state=NORMAL)
            for j in lbout :
                j.config(state=DISABLED)
            of = False
            player = 0
        


def history(d) :
    for k,v in d.items():
        
        label_history.config(text=f"Case {k+1}, {v}")
                           
def deux_fonc(i) :
    replace_with_image(i)
    gagner()
    history(d)
    if "Joueur 1 a gagné" in label_play.cget("text") or "Joueur 2 a gagné" in label_play.cget("text"):
        partie_gagnee = True
        
#CREATION DE MA FENETRE
###################################################################

# Creer la fenetre 
root = Tk()

# Personaliser la fenetre
root.title("Tic Tac Toe")
root.iconbitmap("rond.ico")
root.minsize(900, 700)
root.maxsize(900,700)
root.config(bg="#3e3346")


# Fenetre d'historique
frame1 = Frame(root, bg="grey", width=250, height=700)
frame1.grid(row=0, column=0, padx=3, sticky="nsew")

# Titre :
label_title = Label(frame1, text="Tour :", font=("Helvetica", 30), bg="grey", fg="#f1f1f1")
label_title.grid(row=0, column=0, pady=1, padx=80)
label_play = Label(frame1, text="", font=("Helvetica", 15), bg="grey", fg="#f1f1f1")
label_play.grid(row=1, column=0, pady=15)
label_history = Label(frame1, text="", font=("Helvetica", 15), bg="grey", fg="#f1f1f1")
label_history.grid(row=2, column=0, pady=15)


# Fenetre de Jeu
frame2 = Frame(root, width=500, height=500)
frame2.grid(row=0, column=1, sticky="nsew")

root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

# Creation de bouton invisible
## Les boutons prendront 100% de la place de frame2
for i in range(3):
    frame2.columnconfigure(i, weight=1)
    frame2.rowconfigure(i, weight=1)
    
boutton1 = Button(frame2, bg="#3e3346", command=lambda num=0 :deux_fonc(num), width=1, height=1, state=DISABLED)
boutton2 = Button(frame2, bg="#3e3346", width=1, height=1, command=lambda num=1 :deux_fonc(num), state=DISABLED)
boutton3 = Button(frame2, bg="#3e3346", width=1, height=1, command=lambda num=2 :deux_fonc(num), state=DISABLED)
boutton4 = Button(frame2, bg="#3e3346", width=1, height=1, command=lambda num=3 :deux_fonc(num), state=DISABLED)
boutton5 = Button(frame2, bg="#3e3346", width=1, height=1, command=lambda num=4 :deux_fonc(num), state=DISABLED)
boutton6 = Button(frame2, bg="#3e3346", width=1, height=1, command=lambda num=5 :deux_fonc(num), state=DISABLED)
boutton7 = Button(frame2, bg="#3e3346", width=1, height=1, command=lambda num=6 :deux_fonc(num), state=DISABLED)
boutton8 = Button(frame2, bg="#3e3346", width=1, height=1, command=lambda num=7 :deux_fonc(num), state=DISABLED)
boutton9 = Button(frame2, bg="#3e3346", width=1, height=1, command=lambda num=8 :deux_fonc(num), state=DISABLED)
boutton1.grid(row=0, column=0, sticky="nsew")
boutton2.grid(row=0, column=1, sticky="nsew")
boutton3.grid(row=0, column=2, sticky="nsew")
boutton4.grid(row=1, column=0, sticky="nsew")
boutton5.grid(row=1, column=1, sticky="nsew")
boutton6.grid(row=1, column=2, sticky="nsew")
boutton7.grid(row=2, column=0, sticky="nsew")
boutton8.grid(row=2, column=1, sticky="nsew")
boutton9.grid(row=2, column=2, sticky="nsew")

# Bouton pour commencer la partie
boutton = Button(root, text="Commencer la partie", font=("Courrier", 30), bg="#3e3346", fg="#f1f1f1", command=start_reset)
boutton.grid(row=1, column=1, columnspan=3, sticky="nsew")



# Afficher la fenetre
root.mainloop()
#######################################################################