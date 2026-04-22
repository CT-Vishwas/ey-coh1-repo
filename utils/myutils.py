from string import ascii_letters, digits, punctuation, ascii_uppercase
import re

def is_secure(pwd: str) -> bool:
    '''
    Returns True if pwd is strong
    '''

    # if length of pwd >=8
    # if it contains combination of Capitals, Small, Numbers & Special Chars
    num_count = 0
    spl_chr_count = 0
    caps_count = 0
    if len(pwd) >= 8:
        for chr in pwd:
            if chr in ascii_uppercase:
                caps_count += 1
            
            if chr in digits:
                num_count += 1
            
            if chr in punctuation:
                spl_chr_count += 1
    
    if not (num_count >= 1 and caps_count >= 1 and spl_chr_count >= 1):
        return False
    
    return True
def is_valid_email(email_id: str) -> bool:
    '''
    Returns True if email is valid
    '''
    pat = r'^\S[a-z0-9.]+@[a-z]+.[a-z]+'
    result = re.match(pat, email_id)
    if result != None:
        return True
    else:
        return False

def uname_extracter(email_id: str) -> str:
    '''
    Returns Extracted Email Id
    '''
    if is_valid_email(email_id):
        return email_id[:email_id.find('@')]
    else:
        return "Invalid Email"


if __name__ == '__main__':
    print(is_secure("Abc123!45"))
    print(is_secure("abc123!45"))
    print(is_secure("Abc12345"))
    print(is_secure("Abc123"))
    print(uname_extracter("vishwas@cloudthat.com"))
    print(uname_extracter("vishwas"))