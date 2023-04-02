import math

def dec_to_bin(x, to_display): # x to wartosc dec do zamiany na bin, to_display informacja na ilu bitach zapisuje wartosc
    bina = str(bin(x)[2:]) # usuwamy "0b" na poczatku
    bina = bina.rjust(to_display, "0")
    return bina


with open("do_kompresji.txt", "r") as file: # odczytujemy plik z tekstem do kompresji
    text = file.read()

bin_text = "" # zmienna na skompresowany tekst
length = len(text) # dlugosc tekstu w pliku
code_dict = sorted(list(set(text))) # lista unikalnych znakow w tekscie
dict_length = len(code_dict) # ilosc unikalnych znakĂłw
N = math.ceil(math.log2(dict_length)) # minimalna ilosc bitow na zakodowanie jednego znaku

with open("skompresowany.txt", "wb") as comp: # tworzymy plik ze skompresowanym tekstem
    zmienna = bytearray()
    zmienna.append(dict_length)

    for element in code_dict: # zapisujemy do pliku jako kolejne znaki unikalne znaki w tekscie
        zmienna.append(ord(element))
        print(element)

    rest = (8 - (3 + length * N) % 8) % 8 # wzĂłr na ilosc nadmiarowych bitow

    bin_text += dec_to_bin(rest, 3) # informacja o bitach nadmiarowych zapisana na trzech bitach

    bin_second = ''

    for chara in text:
        bin_second += dec_to_bin(code_dict.index(chara), N)

    bin_second += str(1) * rest
    bin_text += bin_second

    print(bin_text)

    for i in range(0, len(bin_text), 8):

        temp = chr(int(bin_text[i:(i + 8)], 2)) # zapisujemy jako char
        print(bin_text[i:(i + 8)], int(bin_text[i:(i + 8)], 2))
        print(temp)
        print(ord(temp))
        zmienna.append(ord(temp))
    comp.write(bytes(zmienna))