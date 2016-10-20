with open('sod.txt') as f:
	sod=f.readlines()
f.close()
f = open("sod.txt","r")
fsod = f.read()
f.close

with open('sod1.txt') as f:
	sod1=f.readlines()
f.close()
f = open("sod1.txt","r")
fsod1 = f.read()
f.close

with open('sod2.txt') as f:
	sod2=f.readlines()
f.close()
f = open("sod2.txt","r")
fsod2 = f.read()
f.close
print()
print("Mostest impressivestest SUDOKU HYPE game 2k16!!4!!!4!")
print()
print(fsod2)
while 1:
    if fsod == fsod2:
        print('Youre the man (or woman)!!!!!!!!!!4!')
        break
    else:
        print()
        x = input('Type row, column and number to write (e.g:3 4 5): ')
        lst = x.split(' ')
        r=lst[0]
        c=lst[1]
        n=lst[2]

        a=((int(r))*29)+((((int(c))-1)*2)+((int(c))+3))
        
        while 1:
            folyt=input("Wanna check? y/n ")
            if folyt == 'y':
                if n == fsod[int(a)]:
                    fsod2 = fsod2[0:int(a)-1]+' '+n+fsod2[int(a)+1:]  
                    print(fsod2)
                    print('WP dude :----)')
                else:
                    print('No-no, try harder...')
                break
            elif folyt == 'n':
                if fsod2[int(a)] == '_':
                    fsod2 = fsod2[0:int(a)-1]+' '+n+fsod2[int(a)+1:]
                    print(fsod2)
                    break
                else:
                    print('We already filled that space you dumbie...smh')
                    break
            else:
                exit