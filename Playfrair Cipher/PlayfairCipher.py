from string import *
def key_matrix(alphabets,key):
    result, key_matrix = [], []
    list(map(lambda x: x not in result and result.append(x), key))
    list(map(lambda x: x not in result and result.append(x), alphabets))
    a = b = 0
    for i in range(5):
        key_matrix.append(result[a + i:b + 5])
        a += 4; b += 5
    return key_matrix

def plaintextpair(plaintext):
    plaintextpair = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = 'X' if (i + 1) == len(plaintext) else plaintext[i + 1]
        if a != b:
            plaintextpair.append(a + b)
            i += 2
        else:
            plaintextpair.append(a + 'X')
            i += 1
    return plaintextpair

def cipher(plaintextpair,key_matrix,flag):
    ciphertextpair = []
    for pair in plaintextpair:
        pair, applied_rule = pair.replace('J','I'), False
        for row in key_matrix:
            if pair[0] in row and pair[1] in row:
                if flag:
                    ciphertextpair.append(row[(row.index(pair[0]) + 1) % 5] + row[(row.index(pair[1]) + 1) % 5])
                else:
                    ciphertextpair.append(row[(row.index(pair[0]) - 1) % 5] + row[(row.index(pair[1]) - 1) % 5])
                applied_rule = True
        if applied_rule: continue

        for j in range(5):
            col = ''.join([key_matrix[i][j] for i in range(5)])
            if pair[0] in col and pair[1] in col:
                if flag:
                    ciphertextpair.append(col[(col.index(pair[0]) + 1) % 5] + col[(col.index(pair[1]) + 1) % 5])
                else:
                    ciphertextpair.append(col[(col.index(pair[0]) - 1) % 5] + col[(col.index(pair[1]) - 1) % 5])
                applied_rule = True
        if applied_rule: continue

        x1 = x2 = y1 = y2 = 0
        for i in range(5):
            row = key_matrix[i]
            if pair[0] in row:
                x1,y1 = i,row.index(pair[0])
            if pair[1] in row:
                x2,y2 = i,row.index(pair[1])
        ciphertextpair.append(key_matrix[x1][y2] + key_matrix[x2][y1])
    return ciphertextpair

if __name__ == '__main__':
    alphabets = ascii_uppercase.replace('J','')
    plaintext = input('Enter plaintext: ').upper().replace(' ','')
    key = input('Enter Key: ').upper().replace(' ','')

    key_matrix = key_matrix(alphabets,key)
    plaintextpair = plaintextpair(plaintext)

    encryptedtext = cipher(plaintextpair,key_matrix,True)
    decryptedtext = cipher(encryptedtext,key_matrix,False)
    for i in range(5):
        for j in range(5):
            print(key_matrix[i][j],end='    ')
        print()

    char = 0
    ciphertext, deciphertext = '',''
    while char < len(encryptedtext):
        ciphertext += encryptedtext[char]
        deciphertext += decryptedtext[char]
        char += 1

    print('Encryptedtext: ',ciphertext,'\nDecryptedtext: ',deciphertext)

