import time
    
# from words import a
a= [["vinod"],["dojo"],["fire"]]

import random


sar1=(random.choice(a)[0])


user_name=input("Enter Your Name: ")

print("---Welcome",user_name,",","Enjoy your play!!---")
print("\n")
def game(): 
    
    
    
    time.sleep(1)
    cnt= 10
    print("You have",cnt,"lives")

    time.sleep(1)
    print("Start guessing...")
    time.sleep(0.5)
    print("\n")

    sar=sar1

    string= sar[1]+sar[3]
    guesses= sar[1]+sar[3]
    used_letters=[]

    
    for i in range(0,cnt):
        
        for char in sar:      
                if char in guesses:    
                    print(char)
                else:
                    print("-" ) 
        
        
        print("\n")
        guess=input("Guess the missing letter: ")
        
        
        
        for i in guess:
            used_letters.append(guess)

        print("used_letters",used_letters,end="")
        print("\n")
        
        if guess in sar :
            if guess not in guesses:
                guesses += guess 
        if len(guesses)==len(sar):
            # for i in range(0,cnt):
        
            for char in sar:      
                    if char in guesses:    
                        print(char)
                    else:
                        print("-" )
            print("\n")

            print("------*You Won*-------")
            print("\n")
            break
        
            
        if guess in sar:
            
            print("super! Your letter is matched...")

            print("\n")
            
        else:
            cnt-=1
            if cnt>=1:
                
                print("Your letter is not matched")
                print("you have",cnt,"lives left")
            print("\n")
            if cnt<1:
                print("BOOOOOOM!  You are exhausted your lives")

def choice():
    user=input("Enter yes if you want to continue playing else no \n")
    
    
    if user=="yes":
        game()
    
    if user=="no":
        pass


if __name__ == "__main__":
    
    game()

    choice()

                



        



        



