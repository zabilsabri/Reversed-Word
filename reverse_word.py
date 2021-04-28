def reversed_word(kata = input("Masukkan Kata: ").split()):

    for i in reversed(range(len(kata))):
        print(kata[i], end=' ')

reversed_word()