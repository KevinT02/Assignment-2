#-----------------------------------------------------------------------------
# Name:        Assignment (Assignment.py)
# Purpose:     Create a program that includes various conecpts in the criteria.
#
# Author:      Kevin Tu
# Created:     January 7th, 2019
# Updated:     January 18th, 2019
#-----------------------------------------------------------------------------
from colorama import Fore, Back, Style
import replit, time, logging
from math import pi 
import sys
'''
Username:
user

Password:
pass

'''
logging.basicConfig(filename='debug.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.info('Start program')

logging.debug('Generate list and dictionary')
accountStorage ={'user':'pass'}
textFile = ['Hamlet.txt', 'Macbeth.txt', 'Othello.txt', 'note.txt', 'story.txt']

def loginTerminal():
  logging.debug('Start of login terminal')
  print(Style.BRIGHT + Fore.GREEN + (" Login Terminal ".center(60, '=')) + Style.RESET_ALL)

  attempt = 3

  logging.debug('Looping username and password input process')

  userLogin = True
  while userLogin == True:
    if attempt == 0:
      userLogin = False
      createNewUser()
    else:
      name = input('\nUsername: ')
      if name in accountStorage:
        userLogin = False
      else:
        logging.debug('Subtract 1 chance from attempt')
        print(Fore.RED + 'Username Invalid. Try Again\n' + Style.RESET_ALL)
        attempt = attempt - 1
        userLogin = True

  logging.debug('Calculate if password and username match in dictionary') 
  passLogin = True
  while passLogin == True:
    if attempt == 0:
      passLogin = False
      logging.debug('call out the create account function and prompt user to make new account')
      createNewUser()
    else:
      password = input('Password: ')   
      if password in accountStorage[name]:
        print("\n" + Fore.GREEN + (" WELCOME ".center(24,'!')) + Style.RESET_ALL + "\n\n\n\n")
        replit.clear()
        animate()
        passLogin = False 
      else:
        print(Fore.RED + 'Password Invalid. Try Again\n' + Style.RESET_ALL)
        attempt = attempt -  1

  logging.debug('Call the mainMenu function')
  mainMenu()

def createNewUser():
  logging.debug('start to creat new account')
  print(Style.BRIGHT + Fore.GREEN + (" New User Terminal ".center(60, '=')) + '\nWelcome to the New User Terminal. This is where you will make your new account. You are either here because you are a new user or you have forgotten your password or username!\n' + Fore.RED + 'USERNAME & PASSWORD' + Style.RESET_ALL + '\nFor security purposes, an underscore will be inserted between each character of the username and the password may not end or begin with an asterisk. We will be analysisng this password for certain traits and will display your new password so you can comprehend some adjustments that are made')
 
  createUser = input('Create User: ')
    
  print('_'.join(createUser))
  print('Underscores have been added. Make sure you include these when logging back in!')
  logging.debug('correlate the password with the username (vlaue and key) and insert into dictionary')
  createPassword = input('Create Password: ')
  accountStorage[createUser] = createPassword
  logging.debug('run password through tests')
  for variable in createPassword:
    if variable.isalpha():
        print('\"' + variable + '\" is part of the alphabet')
    elif variable.isdecimal():
        print('\"' + variable + '\" is a number')
    elif variable.isspace():
        print('\"' + variable + '\" is a space!')
    elif not variable.isalnum(): 
        print('\"' + variable + '\" is not an alpha numeric character')
  logging.debug('strip asterik')
  if createPassword.startswith('*'):
    print('\nPlease listen! The asterik will be removed!')
    createPassword.lstrip('*')
  else:
    print('\nThank you for meeting the requirements!')
  
  createPassword.rjust('-')
  print ('This will be your final password. Remember this!' + createPassword)
  logging.debug('call main menu')
  mainMenu()

def mainMenu():
  '''
  Initializes the program with a quick introduction.
 
  Quickly introduces the general idea of this program. Talks about the 2 different options and the contents of them without going into too much detail. Gives the user a bief idea of how the program will be like and enough for them to chose a route. When route it chosen, it uses a function that bring user to the next screen, either the English Intro Screen or the Math Intro Screen.

  Parameters
  ----------
  None

  Returns
  -------
  None

  '''
  logging.debug('display menu on console')
  print(" ____  ____  _____ ____ _____ _____ _____ ___  ____  _____ ".center(90, '='))  
  print("|  _ \|  _ \| ____/ ___| ____|_   _|_   _/ _ \|  _ \| ____|".center(90, '='))
  print("| |_) | |_) |  _|| |   |  _|   | |   | || | | | |_) |  _|  ".center(90, '='))
  print("|  __/|  _ <| |__| |___| |___  | |   | || |_| |  _ <| |___ ".center(90, '='))
  print("|_|   |_| \_\_____\____|_____| |_|   |_| \___/|_| \_\_____|".center(90, '=')) 

  print(Style.BRIGHT + Fore.GREEN + ("\n\n") + (" Main Menu ".center(90, '=')) + '\nWelcome to Precettore or Tutor! This was built to help those students in need with their academics. Here you will advance your knowledge in the 2 major subjects of math and english!' + "\n" + 90*('='))

  print(Style.RESET_ALL + Back.BLACK + "\nThe English Section of this program is focussed on Secondary School literature. Feel free to fast track! The Math Section of this Program deals with mathematical concepts ranging from Grade 1 to Grade 8. To make this fun, we essentially created a game. Scoring points and competiting with your friends! Enjoy!" + Style.RESET_ALL)  

  input("\n\n>>> Press " + Fore.GREEN + "ENTER " + Style.RESET_ALL + "to continue to the next menu." + "\033[5;37;37m\n\n(Press ENTER to continue)\033[0;37;37m\n")

  print(Style.BRIGHT + Fore.GREEN + ("\n\n") + (" PATHWAYS ".center(90, '=')) + Style.RESET_ALL +  "\n\n1. EXPLORE THE WORLD OF MATHAMATIQUES THROUGH GAMES AND CHALLENGES\n\n2. READ FAMOUS, HISTORICAL AND WORLD RENOUND PLAYS BY WILLIAM SHAKESPEAR AND A FEW OTHER NOVELS AND USE SOME TOOLS TO HELP STUDY")

  pathwayChoice = input(Style.BRIGHT + Fore.BLUE + "\nInput the NUMBER of the CORRESPONDING PATHWAY you would like to explore!" + Style.RESET_ALL + "\n>>> ")
  logging.debug
  Menu = True

  while Menu == True:
    if pathwayChoice == '1' or pathwayChoice.lower() == 'math':
      Menu == False
      replit.clear()
      mathIntro()

    elif pathwayChoice == '2' or pathwayChoice.lower() == 'english':
      Menu == False
      replit.clear()
      englishIntro() 

    else:
      print('Option you have selected is' + Fore.RED + 'INVALID' + Style.RESET_ALL + 'Try Again!')


def englishIntro():
  animate()
  print(Style.BRIGHT + Fore.GREEN + (" English Menu ".center(80, '=')) + '\nWelcome to English, the section of the program that helps you with the analysis of secondary school litterature' + "\n" + 80*('=') + Style.RESET_ALL + '\n')
  
  input(Style.RESET_ALL + Back.BLACK + "\nThere will 3 books that you will be able to chose from depending on your grade and wil be an area to write you final notes when you are finished" + Style.RESET_ALL + "\n\n>>> Press " + Fore.GREEN + "ENTER " + Style.RESET_ALL + "to continue to the next menu." + 
  "\033[5;37;37m\n\n(Press ENTER to continue)\033[0;37;37m\n")

  logging.debug('call out english menu')
  printEnglishMenu()

def openFile():
  print(textFile)
  print('\n')
  time.sleep(1)
  logging.debug('prompt user input file name')
  fileOpen = True
  while fileOpen == True:
    fileName = input('Which file would you like to open?\n>>> ')
   
    if fileName in textFile:
      fileCheck(fileName)
      fileOpen = False
      print('\nFile Opened...')
    else:
      print(Fore.RED +'Invalid File Name!'+ Style.RESET_ALL)
  return fileName


def printEnglishMenu():
  
  logging.info('disply english main menu')
  print(Style.RESET_ALL)
  print(28 *("-") , ("MAIN MENU") , 28 * ("-"))
  print("\n1. TAKES A WORD COUNT OF FILE \n2. SEARCH NUMBER OF TIMES CHARACTER SPEAKS IN SHAKESPEAR PLAY \n3. SEARCH QUOTE WITHIN SHAKESPEAR PLAY\n4. TAKE FINAL NOTES\n5. DISPLAY NUMBER OF PHONICS IN TEXT (VOWELS & CONSONANTS\n6. FIND LINE OF DESIRED CHAPTER IN 'story.txt'\n0. EXIT")
  print("\n"+ 67 *("-"))

  logging.debug('call out logic function for engish menu')
  menuEnglishLogic()

def menuEnglishLogic():
  logging.debug('running through if statement for menu options based on user input')
  answerValid = True

  while answerValid == True:
    option = input(Fore.CYAN + "Chose an option from the main menu: " + Style.RESET_ALL) 
    if option.lower() == "word count" or option == "1": 
      answerValid = False
      animate()
      wordCount()

    elif option.lower() == "search frequency of character" or option == "2": 
      answerValid = False
      character = input('Character choice:')
      number = characterFrequency(character)
      print(number)

    elif option.lower() == "search quote" or option == "3":
      answerValid = False
      quoteSearch()

    elif option.lower() == "take notes" or option == "4":
      answerValid = False
      takeNotes()

    elif option.lower() == "display frequency of phonics" or option == "5":
      answerValid = False
      fileName = input("Enter the file to check: ")
      phonics(fileName)

    elif option.lower() == "find chapter" or option == "6":
      answerValid = False
      chapNumber = findChapter(int(input('What chapter would you like to find:')))
      print('The chapter you are looking for is on line number:' + chapNumber)

    elif option.lower() == "exit" or option == "0":
      answerValid = False
      printEnd()
    else: 
      print(Fore.RED + "\nUnknown Option Selected!" + Style.RESET_ALL)


def quoteSearch():
  logging.debug('read file that was called in menu')
  fileName = openFile()
  fileOpen = open(fileName, "r")
  fileContents = fileOpen.readlines()
  userAsk = input('Word: ')
  logging.debug('make list and insert line number')
  lines = []
  logging.debug('print list')
  for i in range(0, len(fileContents), 1):
    if userAsk in fileContents[i]:
      lines.append(i)
  print (i)
  


def characterFrequency(character):
  '''
  Parameters
	----------
	temperature : float
		This is the input temperature value from Celsius to convert

	Returns
	-------
	float
		The number of times the character talks in this play

	Raises
	------
	Exception
		If the character count goes awry
  '''  
  logging.debug('make list and append character and display frequency')
  numberCharacter = []

  def characterFrequency(character):
    fileName = openFile()
    fileOpen = open(fileName, "r")

    print('Initializing Search....')
    time.sleep(1)
    animate()
    numberCharacter = []
    for i in range (0, len(fileOpen),1):
      numberCharacter.append(i)
    numberCharacter = len(numberCharacter)

    if not isinstance(character, (str)):
      raise TypeError('characterFrequency expecting a string')

    if not isinstance(numberCharacter, float):
      raise Exception('number of characters did not return a float value as expected')

  return(numberCharacter)


  characterValid = True
  while characterValid == True:
    fileName = openFile()
    fileOpen = open(fileName, "r")
    if character in fileOpen and character.isupper():
      print('Character valid, now counting...')
      time.sleep(0.1)
      for character in range (0, len(fileOpen),1):
        numberCharacter.append(character)
        numberCharacter = len(numberCharacter)
        characterValid = False
    else:
      print('Invalid Request. Please Try Again!')
      characterValid = False

    if not isinstance(numberCharacter, float):
      raise Exception('Number of characters did not return a float value as expected.')
    
    return(numberCharacter)


def phonics(fileName):
  fileName = openFile()
  fileOpen = open(fileName, "r")
  logging.debug('count vowel and consonants')
  vowels = set("a e i o u")
  cons = set("b c d f g h j k l m n p q r s t v w x y z ")
  text = fileOpen.read()
  countV = 0
  for V in text:
    if V.lower() in vowels:
     countV += 1

  countC = 0
  for C in text:
    if C.lower() in cons:
      countC += 1

  print("There are %s vowels in this file"%(countV) ,"\nThere are %s cnsotants in this file"%(countC))
  


def wordCount():
  logging.debug('count total words in file')
  fileName = openFile()
  fileOpen = open(fileName, "r")
  fileContents = fileOpen.readlines()

  lineData = []
  for lines in fileContents:
    lineData += lines
  print('Number of Words:')
  print(len(lineData))
  
def countLines():
  logging.debug('countr frequency of word in file')
  fileName = openFile()
  fileOpen = open(fileName, "r")
  fileContents = fileOpen.readlines()
  userAsk = input('Word: ')

  lines = []

  for i in range(0, len(fileContents), 1):
    if userAsk in fileContents[i]:
      lines.append(i)
      x = len(lines)
      print (i)
  print(x)


def takeNotes():
  logging.debug('write notes onto note.txt')
  fileNote = open('note.txt', 'w')
  note = input('Begin typing your notes (press ENTER when done):')
  fileNote.write(note)


def animate():
  logging.debug('constantly returning and rewriting original text')
  stop = 0
  while stop < 10:
    stop = stop + 1
    sys.stdout.write('\rloading |')
    time.sleep(0.1)
    sys.stdout.write('\rloading /')
    time.sleep(0.1)
    sys.stdout.write('\rloading -')
    time.sleep(0.1)
    sys.stdout.write('\rloading \\')
    time.sleep(0.1)
  sys.stdout.write('\r          \n')
  return

def fileCheck(file):
    try:
      open(file, "r")
      return 
    except FileNotFoundError:
      x = logging.debug('Invalid File')
      return x 

romanNumerals = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

def findChapter(chapter):
  file = open('story.txt', 'r')
  number = romanNumerals[chapter]
  chapterName = ('BOOK ' + number + ' ')
  storyContents = file.readlines()   

  for line in range(0, len(storyContents), 1):
    if chapterName in storyContents[line]:
      lineNumber = line

  return lineNumber

def mathIntro():

  animate()
  print(Style.BRIGHT + Fore.GREEN + 80*('=') + '\nWelcome to MATH. Your excuse to play games before a test the next day!' + "\n" + 80*('='))
  input(Style.RESET_ALL + Back.BLACK + "\nDon't know how to play the game? Here are the RULES AND CONTROLS:" + Style.RESET_ALL + "\n\n>>> Press " + Fore.GREEN + "ENTER " + Style.RESET_ALL + "to check or continue to the next question." + 
  "\n>>> If you answer the question" + Fore.RED + " WRONG"+ Style.RESET_ALL + ", the question will repeat."+"\n>>> If you answer the question" + Fore.GREEN + " RIGHT" + Style.RESET_ALL + 
  "\033[5;37;37m\n\n(Press ENTER to continue)\033[0;37;37m\n")
  printMathMenu()


def printMathMenu():
  print(Style.RESET_ALL)
  print(28 *("-") , ("MAIN MENU") , 28 * ("-"))
  print("\n1. JUNIOR (Grade 1 to 3) \n2. INTERMEDIATE (Grade 4 to 5) \n3. SENIOR (Grade 6 to 8)\n0. EXIT")
  print("\n"+ 67 *("-"))
  menuMathLogic()

def menuMathLogic():
  answerValid = True

  while answerValid == True:
    option = input(Fore.CYAN + "Chose an option from the main menu: " + Style.RESET_ALL) 
    if option == "Junior" or option == "1" or option == "junior": 
      answerValid = False
      animate()
      menu1()
    elif option == "Intermediate" or option == "2" or option == "intermediate": 
      answerValid = False
      animate()
      menu2()
    elif option == "Senior" or option == "3" or option == "senior":
      answerValid = False
      animate()
      menu3()
    elif option == "Exit" or option == "0" or option == "exit":
      answerValid = False
      animate()
      printEnd()
    else: 
      print(Fore.RED + "\nUnknown Option Selected!" + Style.RESET_ALL)

def reconMathMenu():
  input("\nPlease consider chosing your level. This pathway maybe to advanced for you.")
  reconsiderStat = True
  while reconsiderStat == True:
    reconsider= input("Print 'y' is you would like to return to menu, print 'n' if you would like to exit the game\n>")
    if reconsider == "y":
        reconsiderStat = False
        printMathMenu()
    elif reconsider == "n":
        reconsiderStat = False
        printEnd()    
    else: 
      print(Fore.RED + "\nUnknown Option Selected!" + Style.RESET_ALL)

def advanceMathMenu():
  input("\nPlease consider changing your level. This pathway maybe to advanced for you.")
  advanceStat = True
  while advanceStat == True:
    advancement= input("\nWould you like to advance to the next level?\n\nPrint 'y' if you would like to advance 1 level higher.\nPrint 'n' if you would like to return to the main menu.\n\n>")
    if advancement == "y":
        advanceStat = False
        menu2()
    elif advancement == "n":
        advanceStat = False
        printMathMenu()    
    else: 
      print(Fore.RED + "\nUnknown Option Selected!" + Style.RESET_ALL)

def juniorPattern():
  for count in range(0, 20, 5):
    print(str(count), end='' + " ,")
  print("_")

def interPattern():
  for count in range (3 ,20, 4):
    print(str(count), end='' + ", ")
  print("_")

def calculateRadius(radius):
  radSquare = radius**2
  aCircle = radSquare * pi
  return aCircle

'''
Parameters
----------
radius : integer
  The radius of the circle (non-area)

Returns
-------
Integer
  The area of the circle using the given radius in the eqation for the area of the circle

'''
#Expecting a circle with the radius of 3 units to have a area of 28
#assert calRad(3) == 28.274333882308138

def menu1():
  score = 0
  input(Style.RESET_ALL + Fore.MAGENTA + Style.BRIGHT + "\n\nHey JUNIOR, welcome to MATH!")
  input("Before we begin, let's see what you have to offer!"+"\n" + 20*"-" + Style.RESET_ALL)
  input("\nLet's do a POP QUIZ!")
#JUNIOR test question 1
  attempt = 3
  while attempt > 0:
    question1 = input("\nDo the following without a calculator.\n50 + 63 =")
    if question1 == "113":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is 113")
#JUNIOR test question 2
  attempt =3 
  while attempt > 0:
    question2 = input("\nFill in the blanks.\n6 + 8 = _ + 5\n>")
    if question2 == "9":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is 9")
#JUNIOR test question3
  attempt =3 
  while attempt > 0:
    question3 = input("\nSolve the following equation.\n7 * 7 =")
    if question3 == "49":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is 49")
  
  if score >= 2:
    percentage = int(score/3 *100)
    input("\nWell Done! You have passed the test!")
    print("You have scored a: " + "%" + str(percentage))
    input("Let us begin the game!")

  elif score <= 2:
    reconMathMenu()
    


#JUNIOR game question 1
  score = 0
  attempt = 3
  while attempt > 0:
    question1 = input("\nDo the following without a calculator.\n120 + 63 =")
    if question1 == "183":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is 183")
#JUNIOR game question 2
  attempt =3 
  while attempt > 0:
    print("\nDetermine the number that comes next in the pattern below.")
    juniorPattern()
    question2 = input("\n>")
    if question2 == "20":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is 9")
#JUNIOR game question3
  attempt =3 
  while attempt > 0:
    question3 = input("\nHow many meters is 1 kilometer\n>")
    if question3 == "1000":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is 1000")
#JUNIOR game question4
  attempt =3 
  while attempt > 0:
    question3 = input("\nWhat is the standard unit you would use to measure a juice box?\na) km\nb) m\nc) cm\nd) feet\n\n>")
    if question3 == "c" or question3 =="cm":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is cm")
#JUNIOR game question5
  attempt =3 
  while attempt > 0:
    question3 = input("\nBill is carrying $20. He buys 5 hotdogs for $2 each and 3 burgers for $1.50 each. How much money does he have left? (answer must be in the correct format)\n\n$")
    if question3 == "5.50" or question3 == "5. 50":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is $1.50")

  if score >= 3:
    input("\nWell Done! You beat the level!")
    percentage = int(score/5 *100)
    print("You have scored a: " + "%" + str(percentage))
    printWin()
    advanceMathMenu()

  elif score <= 3:
    input("\nYou are below Average.")
    reconMathMenu()




def menu2():
  score = 0
  input(Style.RESET_ALL + Fore.MAGENTA + Style.BRIGHT + "\n\nHey INTERMEDIATE, welcome to MATH!")
  input( "Before we begin, let's see what you have to offer!" +"\n" + 20*"-" + Style.RESET_ALL)
  input("Let's do a POP QUIZ!")
#INTERMEDIATE test question 1
  attempt = 3
  while attempt > 0:
    question1 = input("\nDo the following without a calculator.\n5 * 26 =")
    if question1 == "130":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is 130")
#INTERMEDIATE test question 2
  attempt =3 
  while attempt > 0:
      question2 = input("\nFill in the blanks.\n6 + 250 + 9 = _ + 30\n>")
      if question2 == "235":
        input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
        score = score + 1
        attempt = -1
      else: 
        print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
        attempt = attempt -1
      if attempt == 0:
        input("\nThe correct answer is 235")
#INTERMEDIATE test question3
  attempt =3 
  while attempt > 0:
      question3 = input("\nSolve the following fractions are larger.\n'2/3' or '4/5'")
      if question3 == "4/5":
        input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
        score = score + 1
        attempt = -1
      else: 
        print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
        attempt = attempt -1
      if attempt == 0:
        input("\nThe correct answer is 4/5")
  
  if score >= 2:
    percentage = int(score/3 *100)
    input("\nWell Done! You have passed the test!")
    print("You have scored a: " + "%" + str(percentage))
    input("Let us begin the game!")

  elif score <= 2:
    reconMathMenu()
    
#INTERMEDIATE game question 1
  score = 0
  attempt = 3
  while attempt > 0:
    input ("\nDetermine the number that comes next in the pattern below")
    interPattern()
    question1 = input("\n>")
    if question1 == "23":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is 23")
#INTERMEDIATE game question 2
  attempt =3 
  while attempt > 0:
    print("\nJacob leaves for school at 12:12am. It takes 20 minutes to walk from his house to school. What time is it when he arrives at his school? (Format: HH:MM)")
    question2 = input("\n>")
    if question2 == "12:32":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is 12:32")
#INTERMEDIATE game question3
  attempt =3 
  while attempt > 0:
    question3 = input("\nSam buys 25 crayons for $12. How much did he pay for 1 crayon?\n>$")
    if question3 == "0.48":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is $0.48")
#INTERMEDIATE game question4
  attempt =3 
  while attempt > 0:
    question3 = input("\nOne math textbook costs $20. How much would it cost to buy 25 books.\n$")
    if question3 == "c" or question3 =="500":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is 500")
#INTERMEDIATE game question5
  attempt =3 
  while attempt > 0:
    question3 = input("\nIf John takes 1/5 of the pie, what percentage is he taking out\n\n%")
    if question3 == "20":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is %20")

  if score >= 3:
    input("\nWell Done! You beat the level!")
    percentage = int(score/5 *100)
    print("You have scored a: " + "%" + str(percentage))
    printWin()
    advanceMathMenu()

  elif score <= 3:
    input("\nYou are below Average.")
    reconMathMenu()
 
def menu3():
  score = 0
  input(Style.RESET_ALL + Fore.MAGENTA + Style.BRIGHT + "\n\nHey SENIOR, welcome to MATH!")
  input( "Before we begin, let's see what you have to offer!" +"\n" + 20*"-" + Style.RESET_ALL)
  input("Let's do a POP QUIZ! When you have answered, press enter to continue.")
  #SENIOR test question 1
  attempt = 3
  while attempt > 0:
    question1 = input("\nDo the following without a calculator.\n9 * 4 + 6/2=")
    if question1 == "39":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is 39")
#SENIOR test question 2
  attempt =3 
  while attempt > 0:
      question2 = input("\nIf the 12 hour clock says that it is currently 1:30pm, what will the time be on a 24 hour clock?\n>")
      if question2 == "13:30":
        input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
        score = score + 1
        attempt = -1
      else: 
        print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
        attempt = attempt -1
      if attempt == 0:
        input("\nThe correct answer is 13:30")
#SENIOR test question3
  attempt =3 
  while attempt > 0:
      question3 = input("\nIf Albert eats 2/50 of the pie. What percentage has he eaten\n%")
      if question3 == "4":
        input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
        score = score + 1
        attempt = -1
      else: 
        print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
        attempt = attempt -1
      if attempt == 0:
        input("\nThe correct answer is 4")
  
  if score >= 2:
    percentage = int(score/3 *100)
    input("\nWell Done! You have passed the test!")
    print("You have scored a: %s %"% (question3) + str(percentage))
    input("Let us begin the game!")

  elif score <= 2:
    reconMathMenu()
    


#SENIOR game question 1
  score = 0
  attempt = 3
  while attempt > 0:
    input ("\nDetermine the area of the circle with a radius of 3cm with the calculator below. (Round to the nearest 1)")
    print(Fore.MAGENTA +"\n"+14 *("-") , ("Area of Circle Calculator") , 14 * ("-") + Style.RESET_ALL)
    print("\nEnter the value of your radius below.(Note: Must be a valid integer)")
    radius = int(input(">"))
    print("\n")
    print(calculateRadius(radius))
    question1 = input("\nWhat is the area of the circle?\n>")
    if question1 == "28":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is 28")
#SENIOR game question 2
  attempt =3 
  while attempt > 0:
    print("\nIf the length of a soccer field is 48 meters and the area is 1728m squared, what is the width of the soceer field?")
    question2 = input("\n>")
    if question2 == "36" or question2 =="36m":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is 36m")
#SENIOR game question3
  attempt =3 
  while attempt > 0:
    question3 = input("\nSolve the following equation and answer in the lowest form.\n1/5 + 3/8 =")
    if question3 == "23/40":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is 23/40")
#SENIOR game question4
  attempt =3 
  while attempt > 0:
    question3 = input("\nDetermine the volume of a triangular prism with the following dimensions: L=5, H=6, B=7\n>")
    if question3 == "105":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is 105")
#SENIOR game question5
  attempt =3 
  while attempt > 0:
    question3 = input("\nSolve for 'x' in the following equation.\ny5x + 7 = 2x + 13\n>x = ")
    if question3 == "2":
      input(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      score = score + 1
      attempt = -1
    else: 
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      attempt = attempt -1
    if attempt == 0:
      input("\nThe correct answer is 2")

  if score >= 3:
    input("\nWell Done! You beat the level!")
    percentage = int(score/5 *100)
    print("You have scored a: " + "%" + str(percentage))
    printWin()
    advanceMathMenu()

  elif score <= 3:
    input("\nYou are below Average.")
    reconMathMenu()
 

def printEnd():
  leave = True
  print('┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼')
  print('███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀')
  print('██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼')
  print('██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀')
  print('██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼')
  print('███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄')
  print('┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼')
  print('███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼')
  print('██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼')
  print('██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼')
  print('██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼')
  print('███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄')
  print('┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼')
  print('┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼')
  print('┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼')
  print('┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼')
  print('┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼')
  print('┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼')
  print('┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼')
  print('┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼')
  print('┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼')
  print('┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼')
  print('┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼')
  print('┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼')
  print('┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼')

  print("Now Exiting...")
  if leave == True:
    replit.clear()
    sys.exit
    


def printWin():
  
  print('''             ._==_==_=_.     ''')
  print('''            .-\:      /-.    ''') 
  print('''           | (|:.     |) |   ''')
  print('''            '-|:.     |-'    ''')
  print('''              \::.    /      ''')
  print('''               '::. .'       ''')
  print('''                 ) (         ''')
  print('''               _.' '._       ''')
  print('''              `"""""""`      ''') 
  time.sleep(1)


loginTerminal()

