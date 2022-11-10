#BasePowers_Interface.py
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

def base_text(base,n,base2):
    if n == 1:
        c = chr(0x00b9)
    elif 2 <= n <= 3:
        c = chr(0x00b0 + n)
    elif n == 10:
        c = chr(0x00b9)+chr(0x2070)
    else:
        c = chr(0x2070 + n)
    return str(base)+c+" = "+str(numberToBase(base**n,10,base2))

def initialize():
    
    base = OPTIONS.get(clicked.get())
    base2 = OPTIONS.get(clicked2.get())
    n = 0
    n += 1
    power_1.config(text=base_text(base,n,base2))
    n += 1
    power_2.config(text=base_text(base,n,base2))
    n += 1
    power_3.config(text=base_text(base,n,base2))
    n += 1
    power_4.config(text=base_text(base,n,base2))
    n += 1
    power_5.config(text=base_text(base,n,base2))
    n += 1
    power_6.config(text=base_text(base,n,base2))
    n += 1
    power_7.config(text=base_text(base,n,base2))
    n += 1
    power_8.config(text=base_text(base,n,base2))
    n += 1
    power_9.config(text=base_text(base,n,base2))
    n += 1
    power_10.config(text=base_text(base,n,base2))
    
    return


def aide() :
    
    fonction_text = "Ce programme permet à l'utilisateur de voir le tableau de puissances (de 1 à 10)\npour un nombre entier de 2 à 16, et affiche les résultats en n'importe quelle base\n(de 2 à 16)."
  
    popup2 = tk.Toplevel(root)
    popup2.geometry('460x150')
    popup2.title('Aide Calculator')
    popup2.configure(background='#e4e4e4')
    
    # Création d'une autre frame pour la centrer
    popup = tk.Frame(popup2)
    popup.pack()
    popup.configure(background='#e4e4e4')
        
    titre = tk.Label(popup, text='AIDE Tableau de puissances', font=('Arial', 14, 'bold'), fg='#0c6bab', bg='#e4e4e4',anchor="center")
    titre.grid(row=0, column=0,pady=5)
    
    fonction = tk.Label(popup, text='Fonction',bg='#e4e4e4',font=('Arial', 10, 'bold'))
    fonction.grid(row=1, column=0,pady=2)
  
    fonction_label = tk.Label(popup, text=fonction_text,bg='#e4e4e4',anchor="center",justify='left')
    fonction_label.grid(row=2, column=0,pady=2)
 
    return


# Création de la fenêtre tkinter

def create_window():
  global root
  global power_1,power_2,power_3,power_4,power_5,power_6,power_7,power_8,power_9,power_10
  global clicked,clicked2
  
  root = tk.Tk()
  root.geometry('260x530')
  root.title('Tableau de puissances')
  root.configure(background='#e4e4e4')
  
  # Création d'une autre frame pour la centrer
  fenetre = tk.Frame(root)
  fenetre.pack(side = tk.TOP)
  fenetre.configure(background='#e4e4e4')
  
  #CREATION DES BOUTONS
  bouton_lancer = tk.Button(fenetre, text='Lancer', command=initialize, anchor=tk.CENTER)
  bouton_lancer.grid(row=3, column=0, padx=6, pady=6, ipadx=5, columnspan=2)
  
  bouton_quitter = tk.Button(fenetre, text='Quitter', command=quitter)
  bouton_quitter.grid(row=14, column=0, padx=6, pady=6, ipadx=5, columnspan=2)
  
  bouton_aide = tk.Button(fenetre,text='?',command=aide)
  bouton_aide.grid(row=14,column=1)
  
  #CREATION DES ZONES DE TEXTE 
  entete = tk.Label(fenetre, text='Tableau de puissances', font=('Arial', 14, 'bold'), fg='#0c6bab', bg='#e4e4e4')
  entete.grid(row=0, column=0, pady=10, columnspan=2)
  
  power_1 = tk.Label(fenetre, text='',width=20, font=('Arial', 11), bg="#fff")  # par exemple
  power_1.grid(row=4, column=0, pady=5, columnspan=2)
  
  power_2 = tk.Label(fenetre, text='',width=20, font=('Arial', 11), bg="#fff")  # par exemple
  power_2.grid(row=5, column=0, pady=5, columnspan=2)
  
  power_3 = tk.Label(fenetre, text='',width=20, font=('Arial', 11), bg="#fff")  # par exemple
  power_3.grid(row=6, column=0, pady=5, columnspan=2)
  
  power_4 = tk.Label(fenetre, text='',width=20, font=('Arial', 11), bg="#fff")  # par exemple
  power_4.grid(row=7, column=0, pady=5, columnspan=2)
  
  power_5 = tk.Label(fenetre, text='',width=20, font=('Arial', 11), bg="#fff")  # par exemple
  power_5.grid(row=8, column=0, pady=5, columnspan=2)
  
  power_6 = tk.Label(fenetre, text='',width=20, font=('Arial', 11), bg="#fff")  # par exemple
  power_6.grid(row=9, column=0, pady=5, columnspan=2)
  
  power_7 = tk.Label(fenetre, text='',width=20, font=('Arial', 11), bg="#fff")  # par exemple
  power_7.grid(row=10, column=0, pady=5, columnspan=2)
  
  power_8 = tk.Label(fenetre, text='',width=20, font=('Arial', 11), bg="#fff")  # par exemple
  power_8.grid(row=11, column=0, pady=5, columnspan=2)
  
  power_9 = tk.Label(fenetre, text='',width=20, font=('Arial', 11), bg="#fff")  # par exemple
  power_9.grid(row=12, column=0, pady=5, columnspan=2)
  
  power_10 = tk.Label(fenetre, text='',width=20, font=('Arial', 11), bg="#fff")  # par exemple
  power_10.grid(row=13, column=0, pady=5, columnspan=2)
  
  from_label = tk.Label(fenetre, text='Base', bg='#e4e4e4')
  from_label.grid(row=1, column=0)
  
  to_label = tk.Label(fenetre, text='Display as', bg='#e4e4e4')
  to_label.grid(row=2, column=0)
  
  #CREATION DES MENUS
  #clicked is variable for choice of base form user
  clicked = tk.StringVar(fenetre)
  clicked.set( "Choisis base" )
  #creation of menu using options from the keys of options dictionary
  base1_menu = tk.OptionMenu(fenetre, clicked, *OPTIONS.keys())
  base1_menu.grid(row=1, column=1)
  
  clicked2 = tk.StringVar(fenetre)
  clicked2.set( "Decimal (10)" )
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
