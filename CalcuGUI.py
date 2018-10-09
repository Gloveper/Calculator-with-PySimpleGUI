# This is the PySimpleGUI-based Basic Calculator program
#
# This calculator can do simple calculation such as plus, minus, multiplied and divided
#
# This project is a part of Software Development Practice 1 course
#
# Developed by Tikamporn nontarom
# Computer Engineering student at KMUTNB
# Student ID: 5901012630067

import PySimpleGUI as sg

sg.SetOptions(button_color=('Black', 'White'),
              background_color='#CCCCFF')

# Create a standard calculator
calculator = sg.FlexForm('Calculator', default_button_element_size=(5, 2), auto_size_buttons=False, grab_anywhere=False)
# Layout the design of the GUI
layout = [
          [sg.Input(size=(31, 1), do_not_clear=True, justification='right', key='input')],
          [sg.ReadFormButton('AC'), sg.ReadFormButton('del'), sg.ReadFormButton('('),sg.ReadFormButton(')')],
          [sg.ReadFormButton('7'), sg.ReadFormButton('8'), sg.ReadFormButton('9'),sg.ReadFormButton('÷')],
          [sg.ReadFormButton('4'), sg.ReadFormButton('5'), sg.ReadFormButton('6'),sg.ReadFormButton('×')],
          [sg.ReadFormButton('1'), sg.ReadFormButton('2'), sg.ReadFormButton('3'),sg.ReadFormButton('-')],
          [sg.ReadFormButton('0'), sg.ReadFormButton('.'), sg.ReadFormButton('='),sg.ReadFormButton('+')],
          ]
# Show the calculator to the user
calculator.Layout(layout)


keys_entered = ''
result = ''

# Event loop
while True:
    # Read the calculator
    button, values = calculator.Read()

    # Process button click
    if button is None:  # if the X button clicked, just exit
        break
    if button is 'AC':  # clear keys if clear button
        keys_entered = ''
    elif button in '1234567890.':
        keys_entered = values['input']  # get what's been entered so far
        keys_entered += button  # add the new digit
    elif button is 'del':
        keys_entered = keys_entered[:-1]
    elif button is '(':
        keys_entered = keys_entered + "("
    elif button is ')':
        keys_entered = keys_entered + ")"
    elif button is '=':
        try :
            result = str(eval(keys_entered))
            keys_entered = result
        except ZeroDivisionError:
            keys_entered = 'Infinity'
        except TypeError:
            equation = "Invalid input"
        except SyntaxError:
            equation = "Invalid input"
    elif keys_entered[-1] not in '+-*/':
        if button in '+-':
            keys_entered = values['input']
            keys_entered += button
        elif button is '×':
            keys_entered = values['input']
            keys_entered += '*'
        elif button is '÷':
            keys_entered = values['input']
            keys_entered += '/'

    calculator.FindElement('input').Update(keys_entered)  # change the calculator to reflect current result

