import random
import unidecode


def RAND():
    return random.randint(random.randint(1,5),random.randint(5,8))

def addDiaretics(char,nec):
    a = ["ā","ă","ą","ä","à","á","â","ã"]
    e = ["ė","ę","ě","ĕ","è","é","ê","ë","ē"]
    i = ["ı","į","ī","ï","î","í","ì"]
    o = ["ø","õ","ô","ó","ò","ö"]
    u = ["ū","ů","ų","ü","ù","ú","û"]
    y = ["ý","ÿ"]
    h = ["ħ"]
    w = ["ŵ"]
    c = ["č","ç"]
    r = ["ř"]
    s = ["š"]
    n = ["ň"]
    d = ["đ"]
    l = ["ł"]
    g = ["ğ"]

    if nec==True:
        return random.choice(o)
    if random.randint(0,10)>=3:
        return char

    if char=='a':
        return random.choice(a)
    elif char=='e':
        return random.choice(e)
    elif char=='i':
        return random.choice(i)
    elif char=='o':
        return random.choice(o)
    elif char=='u':
        return random.choice(u)
    elif char=='y':
        return random.choice(u)
    elif char=='h':
        return random.choice(h)
    elif char=='w':
        return random.choice(w)
    elif char=='c':
        return random.choice(c)
    elif char=='r':
        return random.choice(r)
    elif char=='s':
        return random.choice(s)
    elif char=='n':
        return random.choice(n)
    elif char=='d':
        return random.choice(d)
    elif char=='l':
        return random.choice(l)
    elif char=='g':
        return random.choice(g)
    else:
        return char




def trueLen(s):
    num = False
    final = 0
    for char in range(len(s)):
        if s[char]>='1' and s[char]<='9':
            if num==False:
                num = True
        else:
            if num == True:
                num = False
                final += 1
            final += 1
    if num==True:
        return final + 1
    else:
        return final


def trueLast(s):
    final = len(s)-1
    while((s[final]>='1' and s[final]<='9') and final>0):
        final-=1
    if s[-1]>='1' and s[-1]<='9':
        return final+1
    else:
        return final


def CONV(n):
    if(n>26):
        final = chr(n%26 + 96)
        n = n//26
        while n>0:
            final = chr(n%26 + 96) + '°' + final
            n = n//26
        return final
    else:
        return chr(n%26 + 96)


def toCocanb(s):
    words = s.split(' ')
    final1 = ""
    final2 = ""
    endl = []
    endn = []
    
    for word in words:
        if len(word) == 0 or word==' '*len(word):
            continue
        
        endl.append(trueLast(word))
        endn.append(trueLen(word))
        final1 += word[:endl[-1]]
        final2 += word[endl[-1]::] + CONV(endn[-1])


    temp1 = list(final1)

    for x in range(len(temp1)):
        temp1[x] = addDiaretics(temp1[x],False)

    temp2 = list(final2)

    for x in range(len(temp2)):
        temp2[x] = addDiaretics(temp2[x],False)



    final = ''.join(temp1) + "non" + ''.join(temp2)
    nonO = False
    for x in range(len(final),2,-1):
        if final[x-3:x] == "non":
            if nonO==False:
                nonO=True
            else:
                temp = list(final)
                temp[x-2] = addDiaretics("o",True)
                final = ''.join(temp)

    i = RAND()
    while(i<len(final)):
        final = final[:i] + " " + final[i::]
        i += RAND()

    leng = len(final)//3
    for x in range(1,leng):
        final = final.replace(' '*x, ' ')

    return final[0].upper() + final[1::]

def handleSentences(s):
    final = ""

    sens = []
    punc = []
    prev=0

    for x in range(len(s)-1,1,-1):
        if s[x] != ' ':
            if s[x] not in ['.','?','!']:
                s = s + '.'
            break
                
    size = len(s)

    for x in range(size):
        if s[x] == '.' or s[x] == '?' or s[x] == '!':
            punc.append(s[x])
            sens.append(s[prev:x])
            prev = x+1
    

    sens.append(s[prev::])

    i=0

    for sen in sens:
        if(len(sen.replace(' '*len(sen),'')))==0:
            continue
        final = final + toCocanb(sen[0].upper() + sen[1::]) + punc[i] + " "
        i+=1

    return final
