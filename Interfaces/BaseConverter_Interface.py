#BaseConverter_Interface.py
###########################
# Importation des modules utiles
import tkinter as tk
VALUES = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Dictionnaire des options pour les menus
OPTIONS = {
    "Binary (2)" : 2,
    "Trinary (3)" : 3,
    "Quarternary (4)" : 4,
    "Quinary (5)" : 5,
    "Seximal (6)" : 6,
    "Septimal (7)" : 7,
    "Octal (8)" : 8,
    "Nonary (9)" : 9,
    "Decimal (10)" : 10,
    "Elevenary (11)" : 11,
    "Dozenal (12)" : 12,
    "Baker's Dozenal (13)" : 13,
    "Biseptimal (14)" : 14,
    "Triquinary (15)" : 15,
    "Hexadecimal (16)" : 16
}

# Définition des fonctions
def numberToBase(num,fromB = 10,toB = 10):
    '''Converts a number inputed as a string from one base to another
    Arguments:
    > num -- string
    > fromB, base to convert from -- int [2,36]
    > toB, base to convert to -- int [2,36]
    returns:
    - string
    '''
    #We make sure that the bases are integers and num is a string
    fromB = int(fromB)
    toB = int(toB)
    num = str(num)
    #We make sure that the bases are in between 2 and 36
    assert fromB >= 2 and fromB <= 36
    assert toB >= 2 and toB <= 36
    #we convert num to decimal, making num an integer
    num = int(num, fromB)
    result = ''
    #If num is 0 or we want base 10, then we are done
    if num == 0 or toB == 10:
      result = str(num)
    else:
      #we convert num to a string in the target base and store it in result
      #We remove the negative sign and add it back at the end
      negative = False
      if num < 0:
          num = abs(num)
          negative = True
      while num > 0:
          result = VALUES[num%toB] + result
          num //= toB
      if negative:
          result = '-' + result
    
    return result

def convertBase() :
    """Affiche la conversion de la base

    Arguments:
    None -- (fonction déclenchée par le bouton - pas de saisie)
    
    Return :
    None -- (remplissage d'une zone de texte)
    """
    
    #Gets entry from user
    saisie = champSaisie.get()
    
    #Gets the two bases for conversion from user
    convert_from = OPTIONS.get(clicked.get())
    convert_to = OPTIONS.get(clicked2.get())
    
    #Changes text in the base fields
    base1_label.config(text=convert_from)
    base2_label.config(text=convert_to)
    
    try:
        #Checks the entry is a valid number that can be converted
        result = numberToBase(saisie,convert_from,convert_to)
        #Changes label box to show result
        result_data.config(text=result)
    except:
        result_data.config(text='Enter valid number')
    
    return

def aide() :
    
    aide_txt = "Convertisseur de Base\n\nFonction\n\nCe programme permet à l'utilisateur d'entrer un nombre dans\nn'importe quelle base (de 2 à 16) et de le convertir dans une autre base.\n\nUtilisation\n\nL'utilisateur doit d'abord choisir la base dans laquelle se trouve le\nnombre saisi et la base vers laquelle il veut convertir le nombre.\nEnsuite, l'utilisateur doit saisir le nombre qu'il souhaite convertir et\n appuyer sur le bouton « Convertir » pour effectuer le calcul.\n\nRemarques\n\nLa zone de saisie ne fonctionne qu'avec les caractères possible.\ndans la base choisie, et renvoie une erreur lorsque ce n'est pas le cas.\n"
    
    popup = tk.Toplevel(root)
    popup.geometry('450x320')
    popup.title('Aide Calculator')
    popup.configure(background='#e4e4e4')
    aide_label = tk.Label(popup, text=aide_txt,padx=50,pady=25,bg='#e4e4e4')
    aide_label.pack()
        
    return

# Création de la fenêtre tkinter
def create_window():
  global root, result_data, champSaisie, clicked, clicked2, base1_label, base2_label, root, fenetre
  
  root = tk.Tk()
  root.geometry('400x250')
  root.title('Convertisseur de base')
  root.configure(background='#e4e4e4')
  
  # Création d'une autre frame pour la centrer
  fenetre = tk.Frame(root)
  fenetre.pack()
  fenetre.configure(background='#e4e4e4')
  
  #CREATION DES BOUTONS
  bouton_quitter = tk.Button(fenetre, text='Quitter', command=quitter)
  bouton_quitter.grid(row=6, column=0, padx=6, pady=6, ipadx=5)
  
  bouton_convertir = tk.Button(fenetre, text='Convertir', command=convertBase)
  bouton_convertir.grid(row=4, column=1, padx=6, pady=6, ipadx=5)
  
  bouton_aide = tk.Button(fenetre,text='?',command=aide)
  bouton_aide.grid(row=0,column=4,sticky='E')
  
  #CREATIONS DES ZONES DE TEXTE
  entete = tk.Label(fenetre, text='       Convertisseur de Base       ', font=('Arial', 14, 'bold'), fg='#0c6bab', bg='#e4e4e4')
  entete.grid(row=0, column=0, columnspan=4,pady=10)
  
  from_label = tk.Label(fenetre, text='From', bg='#e4e4e4')
  from_label.grid(row=1, column=0)
  
  to_label = tk.Label(fenetre, text='To', bg='#e4e4e4')
  to_label.grid(row=2, column=0)
  
  enter_label = tk.Label(fenetre, text='Saisis', bg='#e4e4e4')
  enter_label.grid(row=3, column=0)
  
  result_label = tk.Label(fenetre, text='Resultat', bg='#e4e4e4')
  result_label.grid(row=5, column=0)
  
  base1_label = tk.Label(fenetre, text='N/A', bg='#e4e4e4')
  base1_label.grid(row=3, column=2)
  
  base2_label = tk.Label(fenetre, text='N/A', bg='#e4e4e4')
  base2_label.grid(row=5, column=2)
  
  result_data = tk.Label(fenetre, text='',width=15, font=('Arial', 11), bg="#fff")  # par exemple
  result_data.grid(row=5, column=1)
  
  #CREATION DES CHAMPS DE SAISIE
  champSaisie = tk.Entry(fenetre, font='12', width=15)
  champSaisie.grid(row=3, column=1)
  
  #CREATION DES MENUS
  #clicked is variable for choice of base form user
  clicked = tk.StringVar(fenetre)
  clicked.set( "Choose base" )
  #creation of menu using options from the keys of options dictionary
  base1_menu = tk.OptionMenu(fenetre, clicked, *OPTIONS.keys())
  base1_menu.grid(row=1, column=1)
  
  #clicked is variable for choice of base form user
  clicked2 = tk.StringVar(fenetre)
  clicked2.set( "Choose base" )
  #creation of menu using options from the keys of options dictionary
  base2_menu = tk.OptionMenu(fenetre, clicked2, *OPTIONS.keys())
  base2_menu.grid(row=2, column=1)
  
  # Programme principal 
  fenetre.mainloop()    # Boucle d'attente des événements


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
