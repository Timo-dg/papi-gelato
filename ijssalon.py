print('------------------------------------------------------------------------------------')
print('\nWelkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.\n')
print('------------------------------------------------------------------------------------')

def stap1():
    aantalBollen =input('Hoeveel bolletjes wilt u? ')
    if aantalBollen.isdigit() == False:
        print('U kunt alleen getallen kiezen')
        stap1()
    if aantalBollen <= str(3):
        stap2(aantalBollen)
    elif aantalBollen <= str(8):
        print('Dan krijgt u van mij een bakje met ' + aantalBollen + ' bolletjes')    
    elif aantalBollen > str(9):
        print('Sorry, zulke grote bakken hebben we niet')
        stap1()
    else:
        print('Sorry dat is geen optie die wij aanbieden')
        stap1()

def stap2(aantalBollen):
    hoornBak =input('Wilt u deze ' + aantalBollen + ' in A een hoorntje of B een bakje? ').lower()
    if hoornBak == 'a' or hoornBak == 'b':
        stap3(hoornBak, aantalBollen)
    else:
        print('Sorry dat snap ik niet... ')
        stap2(aantalBollen)     
    
def stap3(hoornBak, aantalBollen):   
    if hoornBak.lower() == 'a':
        keuzeHorentje =input('Hier is uw horentje met ' + aantalBollen + ' bolletje(s). Wilt u nog meer bestellen? (Y/N) ').lower()
        if keuzeHorentje == 'y':
            stap1()
        elif keuzeHorentje == 'n':
            print('Bedankt en tot ziens!')
        else:
            print('Sorry dat snap ik niet...')
            stap3(hoornBak, aantalBollen)
    elif hoornBak.lower() == 'b':
        keuzeBakje =input('Hier is uw bakje met ' + aantalBollen + ' bolletje(s). Wilt u nog meer bestellen? (Y/N) ').lower()
        if keuzeBakje == 'y':
            stap1()
        elif keuzeBakje == 'n':
            print('Bedankt en tot ziens!')         
        else:
            print('Sorry dat snap ik niet...')
            stap3(hoornBak, aantalBollen)

stap1()