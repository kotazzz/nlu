#. ^ $ * + ? { } [ ] \ | ( )
import random,time
random.seed(time.time())
def main():
    s = [', а',':',",","'",'"',".",";"," а она", "и ведь главное то", "что", "и тип", "ну и", "сказал"]
    i = 0
    si=''
    while i < random.randrange(10,90):
        f = 0
        while f < random.randrange(30,50):
            si+='&#13; '
            f += 1
        si+=s[random.randrange(0,len(s))]
        i+=1
    print(si)
if __name__ == '__main__':
    main()
