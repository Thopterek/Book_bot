def main():
    path = "books/frankenstein.txt"
    txt = book_txt(path)
    num = count_words(txt)
    print(num)
    cc = count_char(txt)
    print(cc)
    
def book_txt(path):
    with open(path) as f:
        return f.read()

def count_words(txt):
    words = txt.split()
    return (len(words))

def count_char(txt):
    low = txt.lower()
    cc = {}
    for char in low:
        if char in cc:
            cc[char] += 1
        else:
            cc[char] = 1
    return cc

main()
