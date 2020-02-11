#------------------------
# Game: Tic Tac Toe
# Author: Raghav Srivaths
# Standard: XI-B
#------------------------

#import sound module for playing sound
#--
import winsound

#--
#Function name: dash
#Input argument: n
#Purpose: Print a string of n dashes in a single line
#--
def dash (n):
    for i in range (1,n):
        print("_",end="") 

#--
#Function name: 	vbarhspace(n)
#Input argument: 	n
#Purpose: 		Print 1 vertical bar followed by (n-1) horizontal spaces in a single line
#--
def vbarhspace(n):
    print ("|",end="")
    for i in range (2,n):
        print(" ",end="")

#--
#Function name: 	drawrowmid(n)
#Input argument: 	n
#Purpose: 		Print a regular middle row for our grid and go to next line
#			|14 spaces|14spaces|14spaces|
#			One extra space needed after second and third vbarhspace for aligning properly
#--		
def drawrowmid(n):
     for i in range (1,n):
         vbarhspace(15); vbarhspace(15);print(" ", end="");vbarhspace(15);print(" ", end="");print("|")

#--
#Function name: 	drawrowtop_bottom()
#Input argument: 	None
#Purpose: 		Print top or bottom rows for our grid, and go to next line
#			15 dashes 1 space 15 dashes 1 space 15 dashes 1 space
#--
def drawrowtop_bottom():
    dash(15); print(" ", end=""); dash (15);print(" ", end=""); dash (15);print(" ", end=""); 
    print()

#--
#Function name: 	vbarhspacefill(n,a)
#Input arguments: 	n -	width of a box	
#			a -	character to be printed
#Purpose: 		Print a row as follows
#			1. One vertical bar
#			2. ~ Half the width with space
#			3. Character to  be printed
#			4. ~ Half the width with space
#--
def vbarhspacefill(n,a):
    print ("|",end="")
    for i in range (2,(n-1)//2):
        print(" ",end="")
    print(a,end="")
    for i in range ((n+1)//2,n):
        print(" ",end="")

#--
#Function name: 	drawrowmidfill(n,a,b,c)
#Input arguments: 	n - 	Height of the box
#			a - 	label of the first box
#			b -	label of the second box
#			c -	label of the third box
#Purpose: 		Print three boxes next to each other as follows
#			Each box must print the label provided in the input arguments
#			1. Print first half of all three boxes 
#			2. Print row containing label
#			3. Print second half of all three boxes 
#--        
def drawrowmidfill(n,a,b,c):
    for i in range (1,n//2):
        vbarhspace(15); vbarhspace(15);print(" ", end="");vbarhspace(15);print(" ", end="");print("|")    
    vbarhspacefill(15,a); vbarhspacefill(15,b);print(" ", end="");vbarhspacefill(15,c);print(" ", end="");print("|")
    for i in range (n//2+2,n):
        vbarhspace(15); vbarhspace(15);print(" ", end="");vbarhspace(15);print(" ", end="");print("|")

#--
#Function name: 	drawgrid()
#Input argument: 	None
#Purpose: 		Print nine boxes 
#			In each box, print the character stored in position array pos
#			pos will be 1,2 ... 9 to start with, when no player has played
#			pos will hold the player's choices as the game proceeds
#--
def drawgrid():
    drawrowtop_bottom()
    drawrowmidfill(10,pos[1],pos[2],pos[3])
    drawrowtop_bottom()

    drawrowtop_bottom()
    drawrowmidfill(10,pos[4],pos[5],pos[6])
    drawrowtop_bottom()

    drawrowtop_bottom()
    drawrowmidfill(10,pos[7],pos[8],pos[9])
    drawrowtop_bottom()

#--
#  Define the position array pos with initial values
#  We need only 9 positions for 9 grid boxes, but since array indices start with 0
#  we can define an array of 10 elements. The zeroth element is a dummy, never used
#	
# 	pos will be 0,1,2 ... 9 to start with, when no player has played
#	pos[0] will be 0 always since it is never used 
# 	pos[1]..pos[9] will hold the player's choices for the 9 boxes 
#	as the game proceeds
#--
pos = ["0","1","2","3","4","5","6","7","8","9"]

#--
#Function name: 	formation(arr)
#Input argument: 	arr
#Purpose: 		Check if the input array has a winning formation
#			A winning formation is 3 rows with same label
#			or 3 columns with same label
#			or the 2 crosses with same label
#Output:		Return 1 if winning formation exists or 0
#			if no winning formation
#--
def formation(arr):
    if (arr[1]==arr[2]==arr[3]): 
        return 1
    if (arr[4]==arr[5]==arr[6]): 
        return 1
    if (arr[7]==arr[8]==arr[9]): 
        return 1
    if (arr[1]==arr[4]==arr[7]): 
        return 1
    if (arr[2]==arr[5]==arr[8]): 
        return 1
    if (arr[3]==arr[6]==arr[9]): 
        return 1
    if (arr[1]==arr[5]==arr[9]): 
        return 1
    if (arr[3]==arr[5]==arr[7]): 
        return 1
    return 0

#------------------------------------------------------------
#------------------------------------------------------------
#Start of main program
#------------------------------------------------------------
#------------------------------------------------------------

#------------------------------------------------------------
#Print initial  blank tictac toe grid to see how it looks!
#This has nine boxes
#------------------------------------------------------------

#--
#Printing the first three boxes 
#--
drawrowtop_bottom()
drawrowmid(10)
drawrowtop_bottom()

#--
#Printing the middle three boxes 
#--
drawrowtop_bottom()
drawrowmid(10)
drawrowtop_bottom()

#--
#Printing the last three boxes
#--
drawrowtop_bottom()
drawrowmid(10)
drawrowtop_bottom()


#------------------------------------------------------------
#Print grid now with positions printed
#This has nine boxes with numbers 1,2...9 printed in each box
#------------------------------------------------------------
drawgrid()

#------------------------------------------------------------
#Now we start playing
#There are 9 attempts possible between the two players
#	PLAYER 1's label is 0
# 	PLAYER 2's label is X
#
# Each time a player selects his position, we do the following -
# 1. Replace position location in the position array pos with  appropriate label (0 or X)
# 2. Update and display the grid to show the label in the selected position
# 3. Check if he has won using the function formation
#	If won, we are done!! 
#------------------------------------------------------------
for i in range(1,9):
    #Get PLAYER 1 position
    print ("PLAYER 1:  Enter POSITION")
    p1=int(input())
    pos[p1]="O"
    drawgrid()
    if formation(pos)==1:
        print ("PLAYER 1 WON")
        winsound.PlaySound("winsound.wav",winsound.SND_ASYNC)
        break
    
    #Get PLAYER 2 position
    print ("PLAYER 2:  Enter POSITION")
    p2=int(input())
    pos[p2]="X"
    drawgrid()
    if formation(pos)==1:
        print ("PLAYER 2 WON")
        winsound.PlaySound("winsound.wav",winsound.SND_ASYNC)
        break

#------------------------------------------------------------
# THE END
#------------------------------------------------------------
