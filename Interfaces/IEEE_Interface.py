#IEEE.py
###########################
# Importation des modules utiles
from tkinter import messagebox
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

def baseToDec(saisieFlot,convert_from):
    """Convertit la partie flottante d'un nombre dans la base choisie en decimal

    Arguments:
    saisieFlot -- int, la partie flottante du nombre saisie
    convert_from -- int, la base dans laquelle est saisieFlot
    
    Return :
    int
    """
    res = 0
    saisieFlot = str(saisieFlot)
    #Calculation loop
    for i in range(len(saisieFlot)):
        value = VALUES.find(saisieFlot[i])
        assert value < convert_from, "invalid literal for baseToDec() with base %d: '%d'"%(convert_from,value)
        res += float(VALUES.find(saisieFlot[i])*(convert_from**(-(i+1))))
    
    res = str(res)
    return (res[2:])

def decToBase(saisieFlot,convert_to):
    """Convertit la partie flottante d'un nombre decimal en la base choisie

    Arguments:
    saisieFlot -- int, la partie flottante du nombre saisie
    convert_to -- int, la base dans laquelle convertir saisieFlot
    
    Return :
    int
    """
    #Define variables
    i=0
    res = ''
    temp = 0.1
    saisieFlot = (saisieFlot + '000')[:3] # on ne veut que trois valeurs
    num = float(saisieFlot)/1000
    
    #Calculation loop
    while (i < 10) and round(temp,3)!=int(temp):
        temp = float(num*convert_to)
        res += VALUES[int(temp)]
        num = temp - int(temp)
        i += 1
    return res

def convert(num,base):
    """Convertit un nombre flottant en IEEE 754, retourne son signe, exposant, et mantisse en binaire"""
    
    #Trouve le signe
    if num.find('-')>=0:
        sign = 1
        num = num[1:]
    else:
        sign = 0
    
    #Trouve s'il y a un point decimal dans le nombre
    if num.find('.')>=0:
        x = num.find('.')
        #Prend la position du point
        num_int = num[:x]
        num_float = num[x+1:]
    else:
        num_int = num
        num_float = 0
    
    #Transforme nombre en decimal
    num_int = int(str(num_int),base)
    num_float = baseToDec(num_float,base)
    
    #Transforme nombre en binaire
    num_int = bin(int(num_int))[2:]
    num_float = decToBase(num_float,2)
    
    #Trouve l'exposant en notation scientifique
    if int(num_int) > 0:
        exp = len(num_int)-1
    else:
       exp = -1
       while str(num_float)[0] == '0':
            num_float = num_float[1:]
            exp -= 1
       print('exp:'+str(exp))
       num_int = ''
    
    #Temp = le nombre total binaire sans point decimal
    temp = str(num_int)+str(num_float)
    print('int: '+str(num_int)+' float: '+str(num_float))
    
    #Trouve mantisse en prenant chiffres flottant de temp
    mantisse = temp[1:]
    
    #Calcul l'exposant en ajoutant 127, puis transformer en binaire
    exp2 = exp+127
    exp2 = bin(exp2)[2:]
    
    #Transformer en 8 bits
    while len(exp2) != 8:
        exp2 = '0'+str(exp2)
        
    #Transformer en 23 bits
    while len(mantisse) != 23:
        mantisse = str(mantisse)+'0'
    
    return sign,exp,exp2,mantisse,num_int,num_float
    

def afficheConversion() :
    """Affiche la conversion de la base

    Arguments:
    None -- (fonction déclenchée par le bouton - pas de saisie)
    
    Return :
    None -- (remplissage d'une zone de texte)
    """
    
    #Gets entry from user
    saisie = champSaisie.get()
    
    #Gets the two bases for conversion from user
    base = OPTIONS.get(clicked.get())
    
    try:
        sign,expDec,exp,mantisse,num_int,num_float = convert(saisie,base)
        
        if sign == 0:
            signe_data_dec.config(text='+1')
        else:
            signe_data_dec.config(text='-1')
            
        exp_data_dec.config(text='2^'+str(expDec))
        mant_data_dec.config(text='1.'+str(int(mantisse,2)))
        
        signe_data_bin.config(text=sign)
        exp_data_bin.config(text=exp)
        mant_data_bin.config(text=mantisse)
        
        hexa = str(sign)+str(exp)+str(mantisse)
        hexa = int(hexa,2)
        hexa = hex(hexa)[2:]

        hex_data.config(text=hexa.upper())
    except:
        messagebox.showerror(title='Erreur de saisis', message='Erreur de saisis. \nSaisissez un nombre valide.')
            
    return

def aide() :
    
    aide_txt = "..."
    
    popup = tk.Toplevel(root)
    popup.geometry('450x320')
    popup.title('Aide Convetisseur')
    popup.configure(background='#e4e4e4')
    aide_label = tk.Label(popup, text=aide_txt,padx=50,pady=25,bg='#e4e4e4')
    aide_label.pack()
        
    return

# Création de la fenêtre tkinter
def create_window():
  global champSaisie, clicked, root, fenetre, signe_data_dec, signe_data_bin, exp_data_dec, exp_data_bin, mant_data_dec, mant_data_bin, hex_data
  
  root = tk.Tk()
  root.geometry('490x260')
  root.title('Convertisseur IEEE 754')
  root.configure(background='#e4e4e4')
  
  # Création d'une autre frame pour la centrer
  fenetre = tk.Frame(root)
  fenetre.pack()
  fenetre.configure(background='#e4e4e4')
  
  #CREATION DES BOUTONS
  bouton_quitter = tk.Button(fenetre, text='Quitter', command=root.destroy)
  bouton_quitter.grid(row=11, column=0, padx=6, pady=6, ipadx=5,columnspan=5)
  
  bouton_convertir = tk.Button(fenetre, text='Convertir', command=afficheConversion)
  bouton_convertir.grid(row=1, column=4, padx=6, pady=6, ipadx=5)
  
  bouton_aide = tk.Button(fenetre,text='?',command=aide)
  bouton_aide.grid(row=0,column=4,sticky='E')
  
  #CREATIONS DES ZONES DE TEXTE
  entete = tk.Label(fenetre, text='Convertisseur IEEE 754', font=('Arial', 14, 'bold'), fg='#0c6bab', bg='#e4e4e4')
  entete.grid(row=0, column=0, columnspan=5,pady=10)
  
  value_label = tk.Label(fenetre, text='Dec', bg='#e4e4e4')
  value_label.grid(row=4, column=0)
  
  bin_label3 = tk.Label(fenetre, text='Binaire', bg='#e4e4e4')
  bin_label3.grid(row=5, column=0)
  
  hex_label3 = tk.Label(fenetre, text='Hex', bg='#e4e4e4')
  hex_label3.grid(row=6, column=0)
  
  signe_label = tk.Label(fenetre, text='Signe', bg='#e4e4e4')
  signe_label.grid(row=3, column=1)
  
  exp_label = tk.Label(fenetre, text='Exponent', bg='#e4e4e4')
  exp_label.grid(row=3, column=2)
  
  mant_label = tk.Label(fenetre, text='Mantisse', bg='#e4e4e4')
  mant_label.grid(row=3, column=3, columnspan=2)
  
  #VALUES
  signe_data_dec = tk.Label(fenetre, text='', width=3, font=('Arial', 11), bg="#fff")
  signe_data_dec.grid(row=4, column=1,pady=5)
  
  exp_data_dec = tk.Label(fenetre, text='', width=10, font=('Arial', 11), bg="#fff")
  exp_data_dec.grid(row=4, column=2,pady=5)
  
  mant_data_dec = tk.Label(fenetre, text='', width=23, font=('Arial', 11), bg="#fff")
  mant_data_dec.grid(row=4, column=3, columnspan=2, pady=5)
  
  #BINARY
  signe_data_bin = tk.Label(fenetre, text='', width=3, font=('Arial', 11), bg="#fff")
  signe_data_bin.grid(row=5, column=1, pady=5)
  
  exp_data_bin = tk.Label(fenetre, text='', width=10, font=('Arial', 11), bg="#fff")
  exp_data_bin.grid(row=5, column=2, pady=5)
  
  mant_data_bin = tk.Label(fenetre, text='', width=23, font=('Arial', 11), bg="#fff")
  mant_data_bin.grid(row=5, column=3, columnspan=2, pady=5)
  
  #HEX
  hex_data = tk.Label(fenetre, text='', width=40, font=('Arial', 11), bg="#fff")
  hex_data.grid(row=6, column=1, pady=5, columnspan=4)
  
  enter_label = tk.Label(fenetre, text='Saisis', bg='#e4e4e4')
  enter_label.grid(row=1, column=0)
  
  #CREATION DES CHAMPS DE SAISIE
  champSaisie = tk.Entry(fenetre, font='12', width=15)
  champSaisie.grid(row=1, column=1, columnspan=2)
  
  #CREATION DES MENUS
  #clicked is variable for choice of base form user
  clicked = tk.StringVar(fenetre)
  clicked.set( "Decimal (10)" )
  #creation of menu using options from the keys of options dictionary
  base1_menu = tk.OptionMenu(fenetre, clicked, *OPTIONS.keys())
  base1_menu.grid(row=1, column=3)
  
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

