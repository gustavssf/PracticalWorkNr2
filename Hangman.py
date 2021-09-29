import random

"""
Zemāk redzamajā kodā ir atrodama visa loģika un algoritmi, kas tiek izpildīti, lai darbotos spēle.
Izveidotā spēle ir "Karātavas" un tā ģenerē nejauši izvēlētu vārdu, kuru lietotājs vēlāk min.
"""

#Vārdi, kas tiks ģenerēti spēlētājam, tov ir iespēja mainīt.
words = ["zilonis", "stienis", "putns", "pitons", "zeme", "kapibara", "printeris", "simps", "dators", "krasts", "kosmoss", "papīrs", "spēle", "korespondence", "konfidencialitāte", "spārni"]

#Funkcija, kas uzsāk spēli, ģenerējot vārdu, nosakot tā garumu un izsaucot minēšanas metodi.
def startGame(words : list):
    word = random.choice(words)
    #Vārda sadalīšana pa burtiem
    letters = list(word)
    print('Tavs vārds sastāv no', len(letters), 'burtiem. Aiziet!')
    wordToGuess = ''
    for letter in range(len(letters)):
        #Tiek izveidots teksta mainīgais ar tik apakšsvītrām, cik vajag vārdam.
        wordToGuess = wordToGuess + '_'
    #Tiek izsaukta mnēšanas metode
    guessWord(word, wordToGuess)

def guessWord(word, wordLength):
    isGuessed = False
    lives = 7
    print('Minot raksti vienu burtu, kas varētu atrasties vārdā vai arī visu vārdu uzreiz.')
    print('Tev ir', lives, 'dzīvības.')
    #Tiek izdrukāts iepriekš izveidotais apakšsvītru teksta mainīgais.
    print(wordLength)
    wordLengthList = list(wordLength)
    #Cikls, kas newbeidzas, kamēr netiek uzminēts vārds vai zaudēta spēle.
    while isGuessed == False:
        if lives == 0:
            print('Tu zaudēji! Pareizā atbilde bija', word)
            print('Dont cry because its over. Smile because it happened.')
            print('Vai vēlies spēlēt atkal? (y - jā, n - nē)')
            break
        playerAnswer = input('Tavs minējums> ')
        if len(playerAnswer) > 1:
            #Ja spēlētājs uzmin vārdu, tad tiek iziets no cikla un metodes.
            if playerAnswer == word:
                print('Tu uzminēji! pareizā atbilde ir', word)
                print('Vai vēlies spēlēt atkal? (y - jā, n - nē)')
                #Tiek uzstādīta true vērtība, kas pārtrauc ciklu un izved ārā no metodes.
                isGuessed = True
            else:
                #Nepareizas atbildes gadījumā tiek noņemta dzīvība.
                lives = lives - 1
                print('Nepareizi! Atlikušas', lives, 'dzīvības.')
        elif len(playerAnswer) == 1:
            letters = list(word)
            #Ar for iterāciju tiek pārbaudīts vai vārdā ir spēlētāja ievadītais burts.
            for index, letter in enumerate(letters):
                if playerAnswer == letter:
                    wordLengthList[index] = playerAnswer
            #Tiek salikts atpakaļ teksta mainīgais no saraksta elementiem.
            output = ''.join(wordLengthList)
            #Ja spēlētājs ir uzminējis burtu, kas ir vārdā, tad tiek izdrukāta burta atrašanās vieta.
            if playerAnswer in output:
                print(output)
            else:
                #Ja vārdā nav šāda burta, tad tiek atņemta dzīvība un brīdināts spēlētājs par nepareizu atbildi.
                lives = lives - 1
                print('Nepareizi! Atlikušas', lives, 'dzīvības. Nav nemaz tik grūti kā tev šķiet.')
            #Ja ir vēl kāda apakšsvītra, tad vārds nav uzminēts un spēle turpinās.
            if '_' in output:
                isGuessed = False
            else:
                #Ja ir uzminēti visi burti, tad vārds ir uzminēts un spēle beidzas.
                print('Tu uzminēji! pareizā atbilde ir', word)
                print('Vai vēlies spēlēt atkal? (y - jā, n - nē)')
                isGuessed = True
        print('')

#Spēles sākums, sasveicināšanās ar spēlētāju un darbību izvēle
print('Esi sveicināts karātavu spēlē! Vai vēlies sākt? (y - Jā, n - Nē)')
while True:
    answer = input('> ')
    #Ievadot y, tiek uzsākta spēle, ar n, aizvērta programma
    if answer == 'y':
        startGame(words)
    elif answer == 'n':
        #Tiek aizvērta spēle.
        print('Visu labu!')
        break
    else:
        #Ja lietotājs ievada ko tādu, ko nesaprot dators.
        print('Es tevi nesapratu, lūdzu, iemācies rakstīt un nākamreiz ievadi y vai n!')