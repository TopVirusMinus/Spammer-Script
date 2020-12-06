import pyautogui, time, keyboard, os
os.system("color A")
print("Made with love in the Hostcell")
again ='y'
while again=='y' or again=='Y':
    choice= input("enter 'f' for file or 'c' for custom word: ")

    if choice=='f':
        print("make sure to open the window where you are spamming the victim")
        fname= input("Enter File name without extention: ")
        f=open(fname+".txt",'r')
        print("Click in text Place")
        print("press S to stop...")
        time.sleep(5)
        for word in f:
            if(keyboard.is_pressed('s')):
                break
            pyautogui.typewrite(word)
            pyautogui.press("enter")

    if choice=='c':
        print("make sure to open the window where you are spamming the victim")
        os.system("color 4")
        customWord= input('Enter your text: ')
        repetition= int(input("how much time: "))
        os.system("color A")
        print("Click in text Place")
        print("press S to stop")
        time.sleep(5)
        for word in range(repetition):
            if(keyboard.is_pressed('s')):
                break
            pyautogui.typewrite(customWord)
            pyautogui.press("enter")
    c= input("Restart? (y/n)")
    os.system('cls')
    again= c
