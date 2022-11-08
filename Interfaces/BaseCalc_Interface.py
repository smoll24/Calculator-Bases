#BaseCalc_Interface.py
###########################
# Importation des modules utiles
import tkinter as tk
from tkinter import messagebox

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

#Characteres qui peuvent etres saisis par l'utilisateur
CHARS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ+-/*%(). '

#All digits, characters used to represent values
VALUES = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
OPERATIONS = '+-/*%().'

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
    saisieFlot = (saisieFlot + '00')[:2] # on veut que deux valeur
    num = float(saisieFlot)/100
    
    #Calculation loop
    while (i < 10) and round(temp,2)!=int(temp):
        temp = float(num*convert_to)
        res += VALUES[int(temp)]
        num = temp - int(temp)
        i += 1
    return res

def baseToDec(saisieFlot,convert_from):
    """Convertit la partie flottante d'un nombre dans la base choisie en decimal

    Arguments:
    saisieFlot -- int, la partie flottante du nombre saisie
    convert_from -- int, la base dans laquelle est saisieFlot
    
    Return :
    int
    """
    res = 0
    #Calculation loop
    for i in range(len(saisieFlot)):
        value = VALUES.find(saisieFlot[i])
        assert value < convert_from, "invalid literal for baseToDec() with base %d: '%d'"%(convert_from,value)
        res += float(VALUES.find(saisieFlot[i])*(convert_from**(-(i+1))))
    
    res = str(res)
    return (res[2:])

def convertReel(saisie, convert_from = 10, convert_to = 10):
    #We make sure that the bases are integers and num is a string
    convert_from = int(convert_from)
    convert_to = int(convert_to)
    saisie = str(saisie)
    
    resFlot = ''
    x = saisie.find('.')
    if x >= 0: #si il y a une virgule
        saisie += '0'
        saisie = saisie[:x+3] #arrondi a deux chiffres apres la virgule
        saisieFlot = saisie[x+1:]
        saisie = saisie[:x]
    
    #Convert the decimal
    if x >= 0:
        if convert_from == 10:
            resFlot = '.' + decToBase(saisieFlot,convert_to)
        else:
            decRes = baseToDec(saisieFlot,convert_from)
            resFlot = '.' + decToBase(decRes,convert_to)
        
    #Convert the number
    result = numberToBase(saisie,convert_from,convert_to) + resFlot
    return result

def stringToBase(saisie, convert_from = 10, convert_to = 10):
    '''Converts all the numbers in an operation inputed as a string from one base to another
    Arguments:
    > saisie -- string
    > convert_from, base to convert from -- int [2,36]
    > convert_to, base to convert to -- int [2,36]
    returns:
    - string
    '''
    saisie = saisie.replace(' ','')
    conv_saisie=''
    temp = ''
    for i in range(len(saisie)):
        if saisie[i] not in OPERATIONS or saisie[i] == '.':
            temp += saisie[i]
        else:
            if temp != '':
                conv_saisie += convertReel(temp,convert_from)
            conv_saisie += saisie[i]
            temp = ''
    if temp:
        conv_saisie += convertReel(temp,convert_from)
    return conv_saisie

def baseEval_str(saisie,convert_from,convert_to):
    ''' Takes an oppeartion formated as a string and calculates the result as a string
    
    Arguments:
    > saisie -- str (operation in original base)
    > convert_from -- int (base to convert from)
    > convert_to -- int (base to convert to)
    
    returns:
    - string (result of operation in wanted base)
    '''
    try:
        #First, we parse saisie and we convert the numbers to decimal
        conv_saisie = stringToBase(saisie,convert_from)
        print('conv_saisie:',conv_saisie)
        #Calculate operation in decimal, put into 'resultat'
        resultat = str(eval(conv_saisie))
        
        #Convert to base
        resultat = convertReel(resultat,10,convert_to)
        
        print(resultat)
        return resultat
    
    except Exception as e:
        print(e)
        raise

def calculate() :
    
    saisie = champSaisie.get()
         
    convert_from = OPTIONS.get(clicked.get())
    convert_to = OPTIONS.get(clicked2.get())
    
    try:
        #Check that inputed operation is valid
        for i in range(len(saisie)):
            assert CHARS.find(saisie[i]) > -1
        #calculate result of operation
        calc_result = baseEval_str(saisie,convert_from,convert_to)
    except Exception as e:        
        messagebox.showerror(title='Erreur de saisis', message='Erreur de saisis. \nSaisissez une opération valide.')
        result_data.config(text='Enter valid operation')
        print(e)
        
    else:
        #Checks if complement a deux is applicable
        if convert_to == 2 and calc_result[0] == '-' and calc_result.find('.') < 0:
            if complement() == 'yes':
                calc_result = str(comp2(calc_result[1:]))
        
        #Affiche resultat
        result_data.config(text=calc_result)
        
def octets(bit_s):
    if len(bit_s)%4 != 0:
        bit_s = ''.join('0' for i in range(4-len(bit_s)%4)) + bit_s
    
    return bit_s
 
def comp2(bit_s):
    bit_s = str(bit_s)
    result = str(bit_s)
    if int(bit_s) != 0:
        bit_s = octets('0'+bit_s)
        inverse_s = ''.join(['1' if i == '0' else '0' for i in bit_s])
        dec = int(inverse_s,2)+1
        result = bin(dec)[2:]
    result = octets(result)
    result = ' '.join(result[i:i+4] for i in range(0, len(result), 4))
    return result

def complement():
    complement = messagebox.askquestion("Complément à deux",
                            "Votre resultat est un nombre entier négatif binaire.\nVoulez-vous le convertir en complément à deux ?",
                           icon = 'question')
    return complement
    
def aide() :
    
    print('aide')
        
    return
    
def create_window():
  global root, result_data, champSaisie, clicked, clicked2
  
  # Création de la fenêtre tkinter
  root = tk.Tk()
  root.geometry('320x190')
  root.title('Calculatrice de réels')
  root.configure(background='#e4e4e4')
  
  # Création d'une autre frame pour la centrer
  fenetre = tk.Frame(root)
  fenetre.pack()
  fenetre.configure(background='#e4e4e4')
  
  # Création des boutons 
  bouton_lancer = tk.Button(fenetre, text='Calculer', command=calculate)
  bouton_lancer.grid(row=4, column=0, padx=6, pady=6, ipadx=5)
  
  bouton_quitter = tk.Button(fenetre, text='Quitter', command=quitter)
  bouton_quitter.grid(row=4, column=1, padx=6, pady=6, ipadx=5)
  
  bouton_aide = tk.Button(fenetre,text='?',command=aide)
  bouton_aide.grid(row=0,column=1,sticky='E')
  
  # Création des zones de texte 
  entete = tk.Label(fenetre, text='Calculatrice de réels', font=('Arial', 14, 'bold'), fg='#0c6bab', bg='#e4e4e4')
  entete.grid(row=0, column=0, columnspan=2, pady=10)
  
  calcul_label = tk.Label(fenetre, text='Opération', pady=5, bg='#e4e4e4')
  calcul_label.grid(row=1, column=0)
  
  result_label = tk.Label(fenetre, text='Résultat', pady=5, bg='#e4e4e4')
  result_label.grid(row=2, column=0)
  
  result_data = tk.Label(fenetre, text='',width=15, font=('Arial', 11), bg="#fff") 
  result_data.grid(row=2, column=1)
  
  # Création du champ de saisie
  champSaisie = tk.Entry(fenetre, font='12', width=15)
  champSaisie.grid(row=1, column=1)
  
  # Création des menus
  clicked = tk.StringVar(fenetre)
  clicked.set( "Decimal (10)" )
  base1_menu = tk.OptionMenu(fenetre, clicked, *OPTIONS.keys())
  base1_menu.grid(row=3, column=0)
  
  clicked2 = tk.StringVar(fenetre)
  clicked2.set( "Decimal (10)" )
  base2_menu = tk.OptionMenu(fenetre, clicked2, *OPTIONS.keys())
  base2_menu.grid(row=3, column=1)
  
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
