tekst = "W pewnym małym miasteczku żył sobie stary stary zegarmistrz. Zegarmistrz ten codziennie naprawiał zegarki, stare zegarki, nowe zegarki i nawet bardzo stare zegarki. Ludzie z miasteczka przychodzili do niego codziennie, codziennie rano i codziennie wieczorem, by odebrać swoje zegarki."
for znak in ",.":
    tekst = tekst.replace(znak, "")

words = tekst.lower().split()
countOfWords = {}
for word in words:
    if  word in countOfWords:
        countOfWords[word] += 1
    else:
        countOfWords[word] = 1

for word, amount in countOfWords.items():
    if amount > 1:
        print(f"{word}, ilość: {amount}")

