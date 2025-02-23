def encode(message,key):
    alphabet =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    returned_message = []
    
    for letter in message:
        if letter in alphabet:
            index_original = alphabet.index(letter)
            index_encoded = index_original + key
            if index_encoded > len(alphabet)-1:
                index_encoded = index_encoded % len(alphabet)
            returned_message.append(alphabet[index_encoded])
        else:
            returned_message.append(letter)
        
    return "".join(returned_message)