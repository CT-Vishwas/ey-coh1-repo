from string import punctuation

VOWELS = 'aeiouAEIOU'
def num_words(fname):
    with open(fname) as fh:
        data = fh.readlines()
        word_count = 0
        for line in data:
            word_count += len(line.split())
        
        return word_count

def num_char(fname):
    with open(fname) as fh:
        data = fh.read()
        return len(data)

def num_lines(fname):
    with open(fname) as fh:
        data = fh.readlines()
        return len(data)

def num_vowels(fname):
    with open(fname) as fh:
        data = fh.read()
        vowel_count = 0
        for chr in data:
            if chr in VOWELS:
                vowel_count += 1
        
        return vowel_count

def num_punctuations(fname):
    with open(fname) as fh:
        data = fh.read()
        punctuation_count = 0
        for chr in data:
            if chr in punctuation:
                punctuation_count += 1
        
        return punctuation_count

def write_log():
    pass