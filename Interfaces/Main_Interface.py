#Main_Interface.py
###########################
# Importation des modules utiles
import tkinter as tk
import importlib

#Dict of file names as keys and display name as value
MODNAMES = {
    "BaseConverter_Interface" : 'Convertisseur',
    "BaseCalc_Interface" : 'Calculatrice de réels',
    "Calculator_Gui" : "Calculatrice d'entiers",
    "IEEE_Interface" : 'Convertisseur IEEE 754',
    "BasePowers_Interface" : 'Puissances',
    }

#Dict of modules (so we can call their functions)
Modules = {}

# Définition des fonctions 
def create_window():
    global root
    # Création de la fenêtre tkinter
    root = tk.Tk()
    root.geometry('240x340')
    root.title('Main Base Interface')
    root.configure(background='#e4e4e4')
  
    # Création d'une autre frame pour la centrer
    fenetre = tk.Frame(root)
    fenetre.pack(side = tk.TOP)
    fenetre.configure(background='#e4e4e4')
  
    #CREATION DES BOUTONS
    i = 2
    for file_name, name in MODNAMES.items():
        try:
            # Import du module
            Modules[file_name] = importlib.import_module(file_name)
            
            # Création du bouton
            main = Modules[file_name].main
            bouton_lancer = tk.Button(fenetre, text=name, command = main, anchor=tk.CENTER)
            bouton_lancer.grid(row=i, column=0, padx=6, pady=6, ipadx=5)
            i += 1
        except ImportError:
            print("No module named '%s'"%file_name)
    
    #Si on a trouve des modules on cree le button 'Close Pograms'
    if Modules:
        tk.Label(fenetre, bg='#e4e4e4').grid(row = 7, pady=0)
        #Creation du bouton "Close Programs"
        bouton_closeprog = tk.Button(fenetre, text='Close Programs', command=close_programs)
        bouton_closeprog.grid(row=8, column=0, padx=6, pady=6, ipadx=5)
    else:
        #Si on n'a pas trouve de modules on l'affiche
        text = tk.Label(fenetre, text='No modules found.', bg='#e4e4e4')
        text.grid(row=1, column=0, padx=6, pady=6, ipadx=5)

    #Creation du bouton "Quitter"
    bouton_quitter = tk.Button(fenetre, text='Quitter', command=quitter)
    bouton_quitter.grid(row=9, column=0, padx=6, pady=6, ipadx=5)

    #CREATION DES ZONES DE TEXTE 
    entete = tk.Label(fenetre, text='Main Base Hub', font=('Arial', 14, 'bold'), fg='#0c6bab', bg='#e4e4e4')
    entete.grid(row=0, column=0, pady=10)

    # Programme principal 
    fenetre.mainloop()    # Boucle d'attente des événements

def close_programs():
    for mod in Modules.values():
        mod.quitter()

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
