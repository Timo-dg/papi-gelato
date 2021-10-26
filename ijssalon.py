print('------------------------------------------------------------------------------------')
print('\nWelkom bij Papi Gelato.\n')
print('------------------------------------------------------------------------------------')

hoornBak = 0
aantalHoorntjes = 0
aantalBakjes = 0
berekeningBakje = 0
berekeningBolletjes = 0
berekeningHorrentje = 0

def stap1():
    aantalBollen =input('Hoeveel bolletjes wilt u? ')
    if aantalBollen.isdigit() == False:
        print('U kunt alleen getallen kiezen')
        stap1()
    if aantalBollen <= str(3):
        smaken(aantalBollen)
        stap2(aantalBollen)
    elif aantalBollen <= str(8):
        smaken(aantalBollen)
        print('Dan krijgt u van mij een bakje met ' + aantalBollen + ' bolletjes')
        keuze = 'bakje'
        global aantalBakjes
        aantalBakjes += 1
        stap3(keuze, aantalBollen)
    elif aantalBollen >= str(9):
        stap1()
        print('Sorry, zulke grote bakken hebben we niet')
        
    else:
        print('Sorry dat is geen optie die wij aanbieden')
        stap1()

def smaken(aantalBollen):
    x = 0
    while x < int(aantalBollen):
        x += 1
        keuzeSmaak =input('Welke smaak wilt u voor bolletje nummer ' + str(x) + ' ? A Aardbei, C Chocolade, M Munt of V Vanille? ').lower()
        if keuzeSmaak != 'a' and keuzeSmaak != 'c' and keuzeSmaak != 'm' and keuzeSmaak != 'v':
            x -= 1
            print('Sorry dat snap ik niet... ')

def hoornBak(keuze):
    if keuze == 'a':
        keuze = 'hoorntje'
        global aantalHoorntjes
        aantalHoorntjes += 1
        return keuze
        
    elif keuze == 'b':
        keuze = 'bakje'
        global aantalBakjes
        aantalBakjes += 1
        return keuze

def stap2(aantalBollen):
    keuze = input('Wilt u deze ' + aantalBollen + ' bollen in A een hoorntje of B een bakje? ').lower()
    if keuze == 'a' or keuze == 'b':   
        if keuze == 'a':
            global aantalHoorntjes
            aantalHoorntjes += 1
        else:
            global aantalBakjes
            aantalBakjes +=1
        stap3(keuze, aantalBollen)
        hoornBak(keuze)
    else:
        print('Sorry dat snap ik niet... ')
        stap2(aantalBollen)     

def bon(aantalBollen, aantalBakjes, aantalHoorntjes, keuze):
    prijsBolletjes = float(1.10)
    prijsHorrentje = float(1.25)
    prijsBakjes = float(0.75)
    global berekeningBakje
    global berekeningHorrentje
    print('\n------------[ Papi Gelato ]------------\n')
    berekeningBolletjes = round(float(aantalBollen)) * float(prijsBolletjes) 
    print('Bolletjes     =  ' + str(aantalBollen) + ' x ' + '€' + str(prijsBolletjes) + '  = ' + '€' + str(berekeningBolletjes))
    if aantalHoorntjes == 0 and aantalBakjes == 0:
        print('')
    if aantalHoorntjes > 0:
        berekeningHorrentje = round(float(aantalHoorntjes)) * str(prijsHorrentje)
        print('Horrentje     =  ' + str(aantalHoorntjes) + ' x ' + '€' + str(prijsHorrentje) + ' = ' + '€' + str(berekeningHorrentje))
    if aantalBakjes > 0:
        berekeningBakje = round(float(aantalBakjes)) * str(prijsBakjes)
        print('Bakje         =  ' + str(aantalBakjes) + ' x ' + '€' + str(prijsBakjes) + ' = ' + '€' + str(berekeningBakje))
    eindbedragCalc = float(berekeningBolletjes) + float(berekeningBakje) + float(berekeningHorrentje)
    print('\n                           ------------\n')
    print('Totaal                     = ' + str(eindbedragCalc))  

def stap3(keuze, aantalBollen):   
    bijbestellen =input('Hier is uw ' + keuze + ' met ' + aantalBollen + ' bolletje(s). Wilt u nog meer bestellen? (Y/N) ').lower()
    if bijbestellen == 'y':
        stap1()
    elif bijbestellen == 'n':
        bon(aantalBollen, aantalBakjes, aantalHoorntjes, keuze)
        print('\nBedankt en tot ziens!\n')
    else:
        print('Sorry dat snap ik niet...')
        stap3(keuze, aantalBollen)

stap1()