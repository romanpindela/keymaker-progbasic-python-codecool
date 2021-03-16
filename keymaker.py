import string

def shift_characters(word, shift):
    """
    >>> shift_characters('abby', 5)
    'fggd'
    """
    alphabet = string.ascii_lowercase
    alphabet_lenght = len(alphabet)

    shifted_word = []

    for letter in word:
        shifted_letter = alphabet[(alphabet.index(letter)+shift) % alphabet_lenght]
        shifted_word.append(shifted_letter)

    return "".join(shifted_word)



def pad_up_to(word, shift, n):
    """
    >>> pad_up_to('abb', 5, 11)
    'abbfggkllpq'
    """
    shifted_word = word
    pad_up_to_word = []

    for iteration in range(shift):
        pad_up_to_word += shifted_word
        shifted_word = shift_characters(shifted_word, shift)
        
    while len(pad_up_to_word) <= 11:
        shifted_word = shift_characters(shifted_word, shift)    
        pad_up_to_word += shifted_word
    #
    #    pad_up_to_word = "".join(pad_up_to_word, pad_up_to(shifted_word,1,n))
    
    return ("".join(pad_up_to_word[0:11]))
    


def abc_mirror(word):
    """
    >>> abc_mirror('abcd')
    'zyxw'
    """
    alphabet = string.ascii_lowercase
    alphabet_lenght = len(alphabet)

    mirrored_word = []
    for letter in word:
        new_letter = alphabet[-(alphabet.index(letter)+1)]
        mirrored_word += new_letter

    return "".join(mirrored_word)

'''
Implement function create_matrix(word1, word2) which returns a list of strings where the nth row is word1 shifted by the value of the nth character of word2. Example: create_matrix('mamas', 'papas') returns ['bpbph', 'mamas', 'bpbph', 'mamas', 'esesk'] ('bpbph' is 'mamas' shifted by 15, the character value of 'p').
The return value is a list of strings. The length of the strings is the length of word1, the length of the list is the length of word2
Each row of the list is the shifted variant of word1, shifted by the corresponding character value of word2
'''

# A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z

#zadanie
def create_matrix(word1, word2):
    """
    >>> create_matrix('mamas', 'papas')
    ['bpbph', 'mamas', 'bpbph', 'mamas', 'esesk']
    """
    alphabet = string.ascii_lowercase
    alphabet_lenght = len(alphabet)

    matrix_hash_words = []

    #for letter in word1:


    return matrix_hash_words


def zig_zag_concatenate(matrix):
    """
    >>> zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl'])
    'adgjkhebcfil'
    """
    pass


def rotate_right(word, n):
    """
    >>> rotate_right('abcdefgh', 3)
    'fghabcde'
    """
    pass


def get_square_index_chars(word):
    """
    >>> get_square_index_chars('abcdefghijklm')
    'abej'
    """
    pass


def remove_odd_blocks(word, block_length):
    """
    >>> remove_odd_blocks('abcdefghijklm', 3)
    'abcghim'
    """
    pass


def reduce_to_fixed(word, n):
    """
    >>> reduce_to_fixed('abcdefghijklm', 6)
    'bafedc'
    """
    pass


def hash_it(word):
    """
    >>> hash_it('morpheus')
    'trowdo'
    """
    padded = pad_up_to(word, 15, 19)
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    rotated = rotate_right(elongated, 3000003)
    cherry_picked = get_square_index_chars(rotated)
    halved = remove_odd_blocks(cherry_picked, 3)
    key = reduce_to_fixed(halved, 6)
    return key


if __name__ == '__main__':
    #name = input("Enter your name! ").lower()
    #print(f'Your key: {hash_it(name)}')
    print(shift_characters("abby",5))
    print(pad_up_to('abb', 5, 11))
    print(abc_mirror('abcd'))
    pass