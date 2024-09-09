def main():
    path = "books/frankenstein.txt"
    txt = book_txt(path)
    num = count_words(txt)
    cc = count_char(txt)
    rep = reporting(cc)
    print(f"it was {num} words!")

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

def hint(d):
    return d["num"]

def msg(ncc):
    print("Your report is getting ready")
    for letter in ncc:
        print (f"Letter {letter['char']} was used {letter['num']} times")
    print("Thank you for reading")

def reporting(cc):
    ncc = []
    for letter in cc:
        if letter.isalpha():
            ncc.append({"char": letter, "num": cc[letter]})
    ncc.sort(reverse=True, key=hint)
    brr = msg(ncc)
    return ncc

main()
