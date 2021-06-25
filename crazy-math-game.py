#START
start = input("Press ""y/Y"" to Start ""n/N"" to Quit: ")

#START PROCESS
if start == "y" or start == "Y":
    start = True
    print("""\n
      _---~~(~~-_.
    _{        )   )
  ,   ) -~~- ( ,-' )_
 (  `-,_..`., )-- '_,)
( ` _)  (  -~( -_ `,  }
(_-  _  ~_-~~~~`,  ,' )
  `~ -^(    __;-,((()))
        ~~~~ {_ -_(())
               `\  }
    welcome to math fuckin game!
          \n""")
    print("99% of people can't answer this \n")
    print("1 + 1 ?")
elif start == "n" or start == "N":
    start = False
else:
    start = False
    print('Only "y" and "n", not CAPITAL')

#IF START IS "TRUE", THE GAME WILL START!

#USER LIFE
life = 3

#GAME PROCESS
while start:
    #USER INPUT
    user = input("Enter your answer: ")
    if user == "Magelan" or user == "magelan":
        #CORRECT ANSWER
        print("Correct")
        break
    else:
        #WRONG ANSWER
        print("Wrong")
        if life == 1:
            print("Game Over")
            break
        life = life - 1
