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
  
  return

def ouvre_calculatrice():
  #Ouvre le code python pour la calculatrice
  BaseCalc_Interface.main()
    
  return

def ouvre_calculatrice2():
  #Ouvre le code python pour la calculatrice
  Calculator_Gui.main()
    
  return

def ouvre_puissances():
  #Ouvre le code python pour la table de base
  BasePowers_Interface.main()
    
  return

def create_window():
  # Création de la fenêtre tkinter
  root = tk.Tk()
  root.geometry('240x270')
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
  bouton_lancer = tk.Button(fenetre, text='Calculatrice', command=ouvre_calculatrice, anchor=tk.CENTER)
  bouton_lancer.grid(row=3, column=0, padx=6, pady=6, ipadx=5)
  
  # Création du bouton "Calculatrice 2"
  bouton_lancer = tk.Button(fenetre, text="Calculatrice 2 GUI", command=ouvre_calculatrice2, anchor=tk.CENTER)
  bouton_lancer.grid(row=4, column=0, padx=6, pady=6, ipadx=5)
  
  # Création du bouton "Puissances"
  bouton_lancer = tk.Button(fenetre, text='Puissances', command=ouvre_puissances, anchor=tk.CENTER)
  bouton_lancer.grid(row=5, column=0, padx=6, pady=6, ipadx=5)
  
  #Creation du bouton "Quitter"
  bouton_quitter = tk.Button(fenetre, text='Quitter', command=root.destroy)
  bouton_quitter.grid(row=6, column=0, padx=6, pady=6, ipadx=5)
  
  #CREATION DES ZONES DE TEXTE 
  entete = tk.Label(fenetre, text='Main Base Hub', font=('Arial', 14, 'bold'), fg='#0c6bab', bg='#e4e4e4')
  entete.grid(row=0, column=0, pady=10)
  
  # Programme principal 
  fenetre.mainloop()    # Boucle d'attente des événements

def main():
  create_window()
if __name__ == "__main__":
    main()
