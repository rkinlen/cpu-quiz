import time


print('''

 _____ ______ _   _       _____ _   _ _____ ______
/  __ \| ___ \ | | |     |  _  | | | |_   _|___  /
| /  \/| |_/ / | | |     | | | | | | | | |    / / 
| |    |  __/| | | |     | | | | | | | | |   / /  
| \__/\| |   | |_| |     \ \/' / |_| |_| |_./ /___
 \____/\_|    \___/       \_/\_\\___/ \___/\_____/
                                                  
                                                  
''')


q1 = input('''
Where is the Program Counter Located?   
1: The Control Unit
2: The ALU
:  ''')

if q1 == "1":
    print("Correct")
    
elif q1 == "2":
    print("Wrong")

time.sleep(1.5)

q2 = input('''
What dose the MAR:   
1: hold the adress of the current instruction
2: performs logical,shift and arithmetic operations 
:  ''')

if q2 == "1":
    print("Correct")
    
elif q2 == "2":
    print("Wrong")


q3 = input('''
What dose the MDR:   
1: acts as a buffer and holds data that is copied from RAM
2: holds the actual data that is being stored in RAM
:  ''')

if q3 == "1":
    print("Correct")
    
elif q3 == "2":
    print("Wrong")


q4 = input('''
What would be necessary if the Accumlator wasn't there:   
1: you would have to overclock the computer therefore installing better cooling
2: write the result of each calculation to main memory.
:  ''')

if q4 == "1":
    print("Correct, Trick Question")
    
elif q4 == "2":
    print("Correct, Trick Question")