def cipher(text, shift, encrypt=True):
    """
    Encrypts/decrypts string.

    Parameters
    ----------
    text : str
        A string that you want to encrypt/decrypt.
    shift : int
        An integer for how many fixed positions down the alphabet you want each letter to be shifted.
    encrypt : bool
        A boolean to designate whether to encrypt (True) or decrypt (False) the string.

    Returns
    -------
    str
        The new encrypted/decrypted string

    Examples
    --------
    
    Encrypting
    ----------
    >>> from cipher_kmh2259 import cipher_kmh2259
    >>> cipher_kmh2259.cipher('apple', 3)
    'dssoh'
    string: 'dssoh'
    
    Decrypting
    ----------
    >>> from cipher_kmh2259 import cipher_kmh2259
    >>> cipher_kmh2259.cipher('apple', 3, encrypt=False)
    'Xmmib'
    string: 'Xmmib'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
