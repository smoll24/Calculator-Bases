#Calculator_Gui.py
###########################
# Design inspiré de https://www.youtube.com/watch?v=QZPv1y2znZo (seulement le design, fonctionnalité crée par nous même)
import tkinter as tk

#initialise variables that keep track of what's on screen
total_calculation = ""
current_calculation = ""
result_on_screen = False

#Dictionnaire des options pour le menu
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

#All digits, characters used to represent values
VALUES = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
OPERATIONS = '+-/*%()'

# Définition des fonctions
def numberToBase(num,fromB = 10,toB = 10):
    '''Converts a number inputed as a string from one base to another
    Arguments:
    > num -- string (number)
    > fromB (base to convert from) -- int [2,36]
    > toB (base to convert to) -- int [2,36]
    returns:
    - string
    '''
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
        #We remove the negative sign and add it back at the end
        negative = False
        if num < 0:
            num = abs(num)
            negative = True
        #we convert num to a string in the target base and store it in result
        while num > 0:
            result = VALUES[num%toB] + result
            num //= toB
        if negative:
            result = '-' + result
    
    return result

def stringToBase(saisie, convert_from = 10, convert_to = 10):
    '''Converts all the numbers in an operation inputed as a string from one base to another
    Arguments:
    > saisie -- string (operation)
    > convert_from (base to convert from) -- int [2,36]
    > convert_to (base to convert to) -- int [2,36]
    returns:
    - string
    '''
    conv_saisie=''
    temp = ''
    #we parse saisie and convert each number in the string into the wanted base
    for x in saisie:
        if x not in OPERATIONS:
            temp += x
        else:
            #special case for NaN just for fun
            if temp == 'NaN':
                conv_saisie += 'NaN'
            elif temp.isalnum():
                conv_saisie += numberToBase(temp,convert_from,convert_to)
            conv_saisie += x
            temp = ''
    if temp == 'NaN':
        conv_saisie += 'NaN'
    elif temp:
        conv_saisie += numberToBase(temp,convert_from,convert_to)
    return conv_saisie

def display(string):
    string = string.replace('**','^')
    
    result = ''
    for i in range(len(string)):
        if string[i] in '+-/*^/' and i>0 and string[i-1] != '(':
            result += ' ' + string[i] + ' '
        else:
            result += string[i]
            
    result = result.replace('/','\u00F7')
    return result

def update():
    total_calc_label.config(text=display(total_calculation))
    calc_label.config(text=display(current_calculation))
    total_calc_label.pack(expand=True, fill="both")
    calc_label.pack(expand=True, fill="both")

def add_to_exp(value):
    global current_calculation, total_calculation, result_on_screen
    value = str(value)
    
    #Only works if the value is smaller than the base
    if VALUES.find(value) < OPTIONS.get(clicked.get()):
        #if the result is on the screen then we clear the whole screen
        if result_on_screen:
            current_calculation = ''
            total_calculation = ''
            result_on_screen = False
        
        #special cases:
        if value in VALUES and current_calculation ==  '0':   
            current_calculation = ''
        if value == '(' and current_calculation and current_calculation[-1] in VALUES:
            operator_update('*')
        if (value == ')' and not current_calculation) or (value == ')' and current_calculation[-1] == '('):
            value = ''
        
        current_calculation += value
        update()
    
def operator_update(op):
    global total_calculation, current_calculation, result_on_screen
    op = str(op)
    
    #if the result is on the screen then we clear the upper line
    #and we replace the upper line with the result
    if result_on_screen:
        total_calculation = ''
        result_on_screen = False
    #cases:
    if current_calculation:
        if current_calculation[-1] != '(' or (op == '+' or op == '-'):
            total_calculation += current_calculation
            total_calculation += op
            current_calculation = ''
    elif len(total_calculation)>1:
        if len(total_calculation) > 2 and total_calculation[-2] == '*':
            total_calculation = total_calculation[:-2] + op
        else:
            total_calculation = total_calculation[:-1] + op
    elif op == '+' or op == '-':
        total_calculation = op
    update()

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
        resultat = round(eval(conv_saisie))
        #convert result to wanted base
        resultat = numberToBase(resultat,10,convert_to)
        print(resultat)
        return(resultat)
    
    except Exception as e:
        print(e)
        raise

def evaluate():
    global total_calculation, current_calculation, result_on_screen, prev_base
    #if the result is on the screen then we clear the upper line
    #and we replace it with the result
    if result_on_screen:
        total_calculation = ''
    
    convert_from = OPTIONS.get(clicked.get())
    prev_base = convert_from
    
    total_calculation += current_calculation
    
    if not total_calculation:
        return
    
    #We correct the operation's signs and parenthesies
    if total_calculation[-1] == '(':
        total_calculation = total_calculation[:-1]
        if not total_calculation:
            return
    
    if total_calculation[-1] in '+-':
        total_calculation += '0'
    elif total_calculation[-1] in '/*%':
        total_calculation += '1'
    
    po = total_calculation.count('(')
    pc = total_calculation.count(')')
    if po > pc:
        total_calculation += ')' * (po-pc)
    elif pc > po:
        total_calculation = '(' * (pc-po) + total_calculation
    
    try:
        current_calculation = baseEval_str(total_calculation, int(convert_from), int(convert_from))
    except Exception as e:
        current_calculation = 'NaN' #e
    
    result_on_screen = True
    update()

def clear():
    global current_calculation, total_calculation
    current_calculation = ""
    total_calculation = ""
    update()

def get_button_color(value):
    if value < OPTIONS.get(clicked.get()):
        background = 'white'
        foreground = "#570861"
    else:
        background = 'white'#"#FFE0E0"
        foreground = '#C0C0C0'#"#FF5050"
    return background, foreground

def switch_base(x):
    global current_calculation, total_calculation, prev_base
    
    new_base = OPTIONS.get(clicked.get())
    
    #if there is a current_calc then we convert it to the new base
    if current_calculation:
        current_calculation = stringToBase(current_calculation,prev_base,new_base)
    if total_calculation:
        total_calculation = stringToBase(total_calculation,prev_base,new_base)
    prev_base = new_base
    
    #edit the colors of the buttons to match if their input is correct
    for i in range(len(ButtonL)):
        background, foreground = get_button_color(len(ButtonL)-i-1)
        ButtonL[i].configure(bg= background, fg=foreground)
    update()

def key_pressed(event):
    char = event.char
    name = event.keysym
    #print(event)
    if char != '':
        if char.upper() in VALUES or char in '()':
            add_to_exp(char.upper())
        elif char in '+-/*%':
            operator_update(char)
        elif char == '^':
            operator_update('**')
        elif name == 'Return' or char == '=':
            evaluate()
        elif name == 'BackSpace':
            clear()
    

def create_window():
    global win, total_calc_label, calc_label, ButtonL, clicked, prev_base

    # Création de la fenêtre tkinter
    win = tk.Tk()
    win.geometry('375x650')
    win.title('Calculator GUI')
    win.configure(background='#e4e4e4')
    #win.resizable(0,0)

    calcframe = tk.Frame(win)
    calcframe.pack(expand=True, fill="both")
    
    buttonframe = tk.Frame(win, height=221, bg = "#F5F5F5")
    buttonframe.pack(expand=True, fill="both")

    clicked = tk.StringVar(calcframe)
    clicked.set( "Decimal (10)" )
    prev_base = OPTIONS.get(clicked.get())
    
    base1_menu = tk.OptionMenu(calcframe, clicked, *OPTIONS.keys(), command=lambda x = clicked: switch_base(x))
    base1_menu.configure(font=("Arial",12), bg="#F8FAFF", fg = "#570861")
    base1_menu.pack(fill="both")

    total_calc_label = tk.Label(calcframe, text=total_calculation, anchor=tk.E,fg="#570861", padx=40,font=("Arial",16))
    total_calc_label.pack(expand=True, fill="both")

    calc_label = tk.Label(calcframe, text=current_calculation, anchor=tk.E,fg="#570861", padx=40,font=("Arial",45))
    calc_label.pack(expand=True, fill="both")
    
    digits_grid = {
        'F':(1,1),'E':(1,2),'D':(1,3),'C':(1,4),
        'B':(2,1),'A':(2,2), 9 :(2,3), 8 :(2,4),
         7 :(3,1), 6 :(3,2), 5 :(3,3), 4 :(3,4),
         3 :(4,1), 2 :(4,2), 1 :(4,3), 0 :(4,4)
        }
    
    #used to configure the colors of the buttons later on
    ButtonL = []
    
    for digit, gridval in digits_grid.items():
        background, foreground = get_button_color(VALUES.find(str(digit)))
            
        button = tk.Button(buttonframe, text=str(digit), bg= background, fg = foreground, font=("Arial", 24, "bold"),
                           borderwidth=0, command=lambda x = digit: add_to_exp(x)) #i hate lambdas >:(
        button.grid(row=gridval[0], column=gridval[1], sticky=tk.NSEW)
        
        ButtonL.append(button)
    
    current_expression = "0"
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
                            font=("Arial",20), borderwidth=0, command = lambda x = '**': operator_update(x))
    square.grid(row=0, column=4, sticky = tk.NSEW)

    buttonframe.rowconfigure(0,weight=1)
    for r in range(0,5):
        for c in range(1,6):   
            buttonframe.rowconfigure(r, weight=1)
            buttonframe.columnconfigure(c,weight=1)
    
    win.bind("<Key>",key_pressed)
    
    win.mainloop()

def quitter():
    global win
    try:
        win.destroy()
    except:
        pass

def main():
    quitter()
    create_window()
    
if __name__ == "__main__":
    main()
