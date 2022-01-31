alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser_cipher(message: str, shift: int, encode: bool = False):
  if encode:
    shift = shift * -1
  result = ""
  for letter in message:
    if letter.isdigit() or letter.isspace():
      result += letter
    elif letter.isupper():
      result += chr((ord(letter) + shift - 65) % 26 + 65)
    else:
      result += chr((ord(letter) + shift - 97) % 26 + 97)
  return result

def hack_ceaser_cipher(text: str):
  decrypted_messages = []
  for i in range(1, 26):
    decrypted_message = ceaser_cipher(text, i, True)
    decrypted_messages.append(decrypted_message)
  for index, decrypted_message in enumerate(decrypted_messages):
    print(f"{index}#: {decrypted_message}")


plain_text = input("Type plain text to encrypt by Ceaser Cipher algorithm: ")
shift = int(input("Type shift number: "))
encrypted_text = ceaser_cipher(plain_text, shift)
print(f"Encrypted text with shift patter ({shift}): {encrypted_text}")
print(f"Decrypted text with shift patter ({shift}): {ceaser_cipher(encrypted_text, shift, True)}")
hack_ceaser_cipher(encrypted_text)