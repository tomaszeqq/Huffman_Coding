import math

with open('skompresowany.txt','rb') as plik:
    compressed_tekst = [i for i in plik.read()]

    chars_count = compressed_tekst[0]

    dictionary = [chr(compressed_tekst[i]) for i in range(1, chars_count + 1)]

    list_to_decompress = [bin(compressed_tekst[i])[2:].zfill(8)
                            for i in range(chars_count + 1, len(compressed_tekst))]

    bin_text = ''.join(list_to_decompress)

    to_decompress = bin_text[3:len(bin_text)-(int(bin_text[:3], 2))]

    N = math.ceil(math.log2(chars_count))

    decompress = [dictionary[int(to_decompress[i:i+N], 2)]
                    for i in range(0, len(to_decompress), N)]

    with open('zde.txt', 'w') as file2:
        file2.write(''.join(decompress))