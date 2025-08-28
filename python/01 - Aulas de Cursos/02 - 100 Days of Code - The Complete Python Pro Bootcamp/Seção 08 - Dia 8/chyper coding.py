import art

print(art.logo)

# Criar uma lista de cada letra, para acessarmos com index
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# Criar função principal 
def ceasar(original_text, shift_amount, encode_or_decode):
    output_text = "" # Começa vazio para guardar oo resultado final

    # Se o user decodificar, a gente vai voltar atrás
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount # index pega a posição da letra e faz + qtd de vezes p mudar
            shifted_position %= len(alphabet) # Se passar de 25, vai recomeçar
            output_text += alphabet[shifted_position] # adiciona nova letra no final
        
    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceasar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
