def caesar_encrypt(plaintext, k):
    result = ""
    k = k % 26 
    for char in plaintext:
        if char.isalpha(): 
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + k) % 26 + base)
        else:
            result += char 
    return result

k = 36
plaintext = "NguyenPhuongNhi"
ciphertext = caesar_encrypt(plaintext, k)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
