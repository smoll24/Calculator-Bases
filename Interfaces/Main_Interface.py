#Main_Interface.py
###########################
# Importation des modules utiles
import tkinter as tk
import BaseConverter_Interface
import BaseCalc_Interface
import Calculator_Gui
import BasePowers_Interface

# Définition des fonctions 
def ouvre_convertisseur():
  #Ouvre le code python pour le convertisseur
  BaseConverter_Interface.main()

def ouvre_calculatrice():
  #Ouvre le code python pour la calculatrice
  BaseCalc_Interface.main()

def ouvre_calculatrice2():
  #Ouvre le code python pour la calculatrice avec GUI
  Calculator_Gui.main()

def ouvre_puissances():
  #Ouvre le code python pour la table de base
  BasePowers_Interface.main()

def create_window():
  global root
  # Création de la fenêtre tkinter
  root = tk.Tk()
  root.geometry('240x290')
  root.title('Main Base Interface')
  root.configure(background='#e4e4e4')
  
  # Création d'une autre frame pour la centrer
  fenetre = tk.Frame(root)
  fenetre.pack(side = tk.TOP)
  fenetre.configure(background='#e4e4e4')
  
  #CREATION DES BOUTONS
  # Création du bouton "Convertisseur"
  bouton_lancer = tk.Button(fenetre, text='Convertisseur', command=ouvre_convertisseur, anchor=tk.CENTER)
  bouton_lancer.grid(row=2, column=0, padx=6, pady=6, ipadx=5)
  
  # Création du bouton "Calculatrice"
  bouton_lancer = tk.Button(fenetre, text='Calculatrice Réels', command=ouvre_calculatrice, anchor=tk.CENTER)
  bouton_lancer.grid(row=3, column=0, padx=6, pady=6, ipadx=5)
  
  # Création du bouton "Calculatrice 2"
  bouton_lancer = tk.Button(fenetre, text="Calculatrice Entiers", command=ouvre_calculatrice2, anchor=tk.CENTER)
  bouton_lancer.grid(row=4, column=0, padx=6, pady=6, ipadx=5)
  
  # Création du bouton "Puissances"
  bouton_lancer = tk.Button(fenetre, text='Puissances', command=ouvre_puissances, anchor=tk.CENTER)
  bouton_lancer.grid(row=5, column=0, padx=6, pady=6, ipadx=5)
  
  #Creation du bouton "Close Programs"
  bouton_closeprog = tk.Button(fenetre, text='Close Programs', command=close_programs)
  bouton_closeprog.grid(row=6, column=0, padx=6, pady=6, ipadx=5)
  
  #Creation du bouton "Quitter"
  bouton_quitter = tk.Button(fenetre, text='Quitter', command=quitter)
  bouton_quitter.grid(row=7, column=0, padx=6, pady=6, ipadx=5)
  
  #CREATION DES ZONES DE TEXTE 
  entete = tk.Label(fenetre, text='Main Base Hub', font=('Arial', 14, 'bold'), fg='#0c6bab', bg='#e4e4e4')
  entete.grid(row=0, column=0, pady=10)
  
  # Programme principal 
  fenetre.mainloop()    # Boucle d'attente des événements

def close_programs():
    BaseConverter_Interface.quitter()
    BaseCalc_Interface.quitter()
    Calculator_Gui.quitter()
    BasePowers_Interface.quitter()

def quitter():
    global root
    try:
        root.destroy()
    except:
        pass

def main():
    quitter()
    create_window()
    
if __name__ == "__main__":
    main()
