import wc

def main():
    fname = input("Enter the Filename: ")
    log_content = {}
    try:
        log_content['fname'] = fname
        log_content['Number of Lines'] = wc.num_lines(fname)
        log_content['Number of Words'] = wc.num_words(fname)
        log_content['Number of Characters'] = wc.num_char(fname)
        log_content['Number of Punctuations'] = wc.num_punctuations(fname)
    except FileNotFoundError:
        print("File Doesnot Exist")

if __name__ == '__main__':
    main()