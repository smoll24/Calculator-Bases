# Design inspiré de https://www.youtube.com/watch?v=QZPv1y2znZo (seulement le design, fonctionnalité crée par nous même)
import tkinter as tk
from PIL import Image, ImageTk

total_calculation = ""
current_calculation = ""
result_on_screen = False

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
CHARS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ+-/*%()'

#All digits, characters used to represent values
VALUES = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
OPERATIONS = '+-/*%()'

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
          result = VALUES[num%toB].upper() + result
          num //= toB
      if negative:
          result = '-' + result
    
    return result

def update():
    total_calc_label.config(text=total_calculation)
    calc_label.config(text=current_calculation)
    total_calc_label.pack(expand=True, fill="both")
    calc_label.pack(expand=True, fill="both")


def add_to_exp(value):
    global current_calculation
    global total_calculation
    global result_on_screen
    
    if result_on_screen:
        if value != '**':
            current_calculation = ''
        total_calculation = ''
        result_on_screen = False
    
    if len(current_calculation) >= 1:   
        if current_calculation[0] !=  "0":
            current_calculation += str(value)
        else:
            current_calculation = current_calculation[1:] + str(value)
    elif value != '**':
        current_calculation += str(value)
    update()
    
def operator_update(op):
    global total_calculation
    global current_calculation
    global result_on_screen
    
    if result_on_screen:
        total_calculation = ''
        result_on_screen = False
    
    print(current_calculation)
    if current_calculation:
        total_calculation += current_calculation
        total_calculation += op
    else:
        total_calculation = total_calculation[:-1] + op
    current_calculation=""
    update()
    
def clear():
    global current_calculation
    global total_calculation
    current_calculation = ""
    total_calculation = ""
    update()

def evaluate():
    global total_calculation
    global current_calculation
    global result_on_screen
    
    if result_on_screen:
        total_calculation = ''
        
    total_calculation += current_calculation    
    current_calculation = baseEval_str(total_calculation, 16, 16)
    
    result_on_screen = True
    #total_calculation = ""
    update()
    return current_calculation
    
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
        conv_saisie=''
        temp = ''
        for i in range(len(saisie)):
            if saisie[i] not in OPERATIONS:
                temp += saisie[i]
            else:
                if temp.isalnum():
                    conv_saisie += numberToBase(temp,convert_from)
                conv_saisie += saisie[i]
                temp = ''
        if temp:
            conv_saisie += numberToBase(temp,convert_from)
        print('conv_saisie:',conv_saisie)
        #Calculate operation in decimal, put into 'resultat'
        resultat = round(eval(conv_saisie))
        #convert result to wanted base
        resultat = numberToBase(resultat,10,convert_to)
        print(resultat)
        return(resultat)
    
    except Exception as e:
        print(e)
        raise

def create_window():
    global total_calc_label, calc_label
    # Création de la fenêtre tkinter
    win = tk.Tk()
    win.geometry('375x650')
    win.title('Calculator GUI')
    win.configure(background='#e4e4e4')
    win.resizable(0,0)

    calcframe = tk.Frame(win)
    calcframe.pack(expand=True, fill="both")

    buttonframe = tk.Frame(win, height=221, bg = "#F5F5F5")
    buttonframe.pack(expand=True, fill="both")


    total_calc_label = tk.Label(calcframe, text=total_calculation, anchor=tk.E,fg="#570861", padx=40,font=("Arial",16))
    total_calc_label.pack(expand=True, fill="both")

    calc_label = tk.Label(calcframe, text=current_calculation, anchor=tk.E,fg="#570861", padx=40,font=("Arial",45))
    calc_label.pack(expand=True, fill="both")

    digits_grid = {
        'F':(1,1), 'E':(1,2), 'D':(1,3), 'C':(1,4),
        'B':(2,1), 'A':(2,2), 9: (2,3), 8: (2,4),
        7: (3,1), 6: (3,2), 5: (3,3), 4:(3,4),
        3: (4,1), 2: (4,2), 1: (4,3), 0: (4,4)
        }

    for digit, gridval in digits_grid.items():
        button = tk.Button(buttonframe, text=str(digit), bg= "white", fg = "#570861", font=("Arial", 24, "bold"),
                           borderwidth=0, command=lambda x = digit: add_to_exp(x)) #i hate lambdas >:(
        button.grid(row=gridval[0], column=gridval[1], sticky=tk.NSEW)

    current_expression = "0"
    print(current_expression)
    update()

    operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

    r = 0
    for operator,symbol in operations.items():
        button = tk.Button(buttonframe, text=symbol, bg="#F8FAFF", fg = "#570861",
                           font=("Arial", 20), borderwidth=0, command= lambda x = operator: operator_update(x))
        button.grid(row=r, column=5, sticky=tk.NSEW)
        r+=1

    clearbutton = tk.Button(buttonframe, text="C", bg="#F8FAFF", fg="#570861",
                            font=("Arial",20), borderwidth=0, command = clear)
    clearbutton.grid(row=0, column=1, sticky=tk.NSEW)

    equalbutton = tk.Button(buttonframe, text="=", bg="#F8FAFF", fg="#570861",
                            font=("Arial",20), borderwidth=0, command= evaluate)
    equalbutton.grid(row=4, column=5, sticky = tk.NSEW)

    parenthesis1 = tk.Button(buttonframe, text="(", bg="#F8FAFF", fg="#570861",
                            font=("Arial",20), borderwidth=0, command = lambda x="(": add_to_exp(x))
    parenthesis1.grid(row=0, column=2, sticky = tk.NSEW)

    parenthesis = tk.Button(buttonframe, text=")", bg="#F8FAFF", fg="#570861",
                            font=("Arial",20), borderwidth=0, command = lambda x=")": add_to_exp(x))
    parenthesis.grid(row=0, column=3, sticky = tk.NSEW)

    square = tk.Button(buttonframe, text="x\u02B8", bg="#F8FAFF", fg="#570861",
                            font=("Arial",20), borderwidth=0, command = lambda x="**": add_to_exp(x))
    square.grid(row=0, column=4, sticky = tk.NSEW)

    buttonframe.rowconfigure(0,weight=1)
    for r in range(0,5):
        for c in range(1,6):   
            buttonframe.rowconfigure(r, weight=1)
            buttonframe.columnconfigure(c,weight=1)

    win.mainloop()


def main():
  create_window()
if __name__ == "__main__":
    main()
