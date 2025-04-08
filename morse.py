import flet as ft
import pyperclip
def main(page):
    page.theme = ft.Theme( color_scheme_seed=ft.Colors.GREEN_900)#https://flet.dev/docs/cookbook/theming/
    page.update()
    morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',  
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',  
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',  
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',  
        'Y': '-.--', 'Z': '--..',  
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',  
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',  
        ' ': '//'
    } 

    polar = {
        'P': 'C', 'O': 'E', 'L': 'N', 'A': 'I', 'R': 'T',
        'C': 'P', 'E': 'O', 'N': 'L', 'I': 'A', 'T': 'R',
        'B': 'B', 'D': 'D', 'F': 'F', 'G': 'G', 'H': 'H',
        'J': 'J', 'K': 'K', 'M': 'M', 'Q': 'Q', 'S': 'S',
        'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z',
        ' ': ' '
    }

    morseINV = {}
    for letra in morse:
     morseINV[morse[letra]] = letra
    polarINV = {}
    for letra in polar:
     polarINV[polar[letra]] = letra
    def encryptM(txt):
     resultado = ""
     for letra in txt:
      if letra in morse:
       resultado += morse[letra] + "/"
     return resultado.strip()
    def desencriptarMorse(txt):
     resultado = ""
     palabras = txt.split('/')
     for simbolo in palabras:
      if simbolo in morseINV:
       resultado += morseINV[simbolo]
      elif simbolo == '':
       resultado += ' '
     return resultado
    def encriptarPolar(txt):
     resultado = ""
     for letra in txt:
      if letra.upper() in polar:
       resultado += polar[letra.upper()]
      else:
       resultado += letra
     return resultado
    def desencriptarPolar(txt):
     resultado = ""
     for letra in txt:
      if letra.upper() in polarINV:
       resultado += polarINV[letra.upper()]
      else:
       resultado += letra
     return resultado
    def encriptarA1Z26(txt):
     resultado = ""
     for letra in txt:
      if letra == ' ':
       resultado += '/ '
      else:
       resultado += str(ord(letra.upper()) - ord('A') + 1) + " "
     return resultado.strip()
    def desencriptarA1Z26(txt):
     resultado = ""
     numeros = txt.split()
     for num in numeros:
      if num == '/':
       resultado += ' '
      else:
       resultado += chr(int(num) + ord('A') - 1)
     return resultado
    def encriptar(e):
     txt = input.value.upper()
     if metodo.value == "Morse":
      result.value = encryptM(txt)
     elif metodo.value == "Polar":
      result.value = encriptarPolar(txt)
     elif metodo.value == "A1Z26":
      result.value = encriptarA1Z26(txt)
     page.update()
    def desencriptar(e):
     txt = input.value
     if metodo.value == "Morse":
      result.value = desencriptarMorse(txt)
     elif metodo.value == "Polar":
      result.value = desencriptarPolar(txt)
     elif metodo.value == "A1Z26":
      result.value = desencriptarA1Z26(txt)
     page.update()
    def ctrlC(e):
     pyperclip.copy(result.value)
     page.update()

    input = ft.TextField(label="Texto:", width=400)
    metodo = ft.Dropdown(width=200, options=[ft.dropdown.Option("Morse"), ft.dropdown.Option("Polar"), ft.dropdown.Option("A1Z26")], value="Morse")
    encriptarB = ft.ElevatedButton("Encriptar", on_click=encriptar)
    desencriptarB = ft.ElevatedButton("Desencriptar", on_click=desencriptar)
    ctrlCB = ft.ElevatedButton("Copiar", on_click=ctrlC)
    result = ft.Text("resultado")

    page.add(input, metodo, encriptarB, desencriptarB, ctrlCB, result)
ft.app(main)
