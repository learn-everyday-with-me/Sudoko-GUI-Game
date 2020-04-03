from tkinter import *
from tkinter import PhotoImage
root = Tk()
root.title("Sudoko")
root.iconbitmap("bitmap.ico")
win_gif = PhotoImage(file = "tenor.gif")
win_image = Label(root,image = win_gif)

matrix=[  [3,0,6,5,0,8,4,0,0],
          [5,2,0,0,0,0,0,0,0],
          [0,8,7,0,0,0,0,3,1],
          [0,0,3,0,1,0,0,8,0],
          [9,0,0,8,6,3,0,0,5],
          [0,5,0,0,9,0,6,0,0],
          [1,3,0,0,0,0,2,5,0],
          [0,0,0,0,0,0,0,7,4],
          [0,0,5,2,0,6,3,0,0]
     ]
matrix1=matrix
def Submitted():
    if (
            int(row0column0.get()) == matrix1[0][0] and
            int(row0column1.get()) == matrix1[0][1] and
            int(row0column2.get()) == matrix1[0][2] and
            int(row0column3.get()) == matrix1[0][3] and
            int(row0column4.get()) == matrix1[0][4] and
            int(row0column5.get()) == matrix1[0][5] and
            int(row0column6.get()) == matrix1[0][6] and
            int(row0column7.get()) == matrix1[0][7] and
            int(row0column8.get()) == matrix1[0][8] and
            int(row1column0.get()) == matrix1[1][0] and
            int(row1column1.get()) == matrix1[1][1] and
            int(row1column2.get()) == matrix1[1][2] and
            int(row1column3.get()) == matrix1[1][3] and
            int(row1column4.get()) == matrix1[1][4] and
            int(row1column5.get()) == matrix1[1][5] and
            int(row1column6.get()) == matrix1[1][6] and
            int(row1column7.get()) == matrix1[1][7] and
            int(row1column8.get()) == matrix1[1][8] and
            int(row2column0.get()) == matrix1[2][0] and
            int(row2column1.get()) == matrix1[2][1] and
            int(row2column2.get()) == matrix1[2][2] and
            int(row2column3.get()) == matrix1[2][3] and
            int(row2column4.get()) == matrix1[2][4] and
            int(row2column5.get()) == matrix1[2][5] and
            int(row2column6.get()) == matrix1[2][6] and
            int(row2column7.get()) == matrix1[2][7] and
            int(row2column8.get()) == matrix1[2][8] and
            int(row3column0.get()) == matrix1[3][0] and
            int(row3column1.get()) == matrix1[3][1] and
            int(row3column2.get()) == matrix1[3][2] and
            int(row3column3.get()) == matrix1[3][3] and
            int(row3column4.get()) == matrix1[3][4] and
            int(row3column5.get()) == matrix1[3][5] and
            int(row3column6.get()) == matrix1[3][6] and
            int(row3column7.get()) == matrix1[3][7] and
            int(row3column8.get()) == matrix1[3][8] and
            int(row4column0.get()) == matrix1[4][0] and
            int(row4column1.get()) == matrix1[4][1] and
            int(row4column2.get()) == matrix1[4][2] and
            int(row4column3.get()) == matrix1[4][3] and
            int(row4column4.get()) == matrix1[4][4] and
            int(row4column5.get()) == matrix1[4][5] and
            int(row4column6.get()) == matrix1[4][6] and
            int(row4column7.get()) == matrix1[4][7] and
            int(row4column8.get()) == matrix1[4][8] and
            int(row5column0.get()) == matrix1[5][0] and
            int(row5column1.get()) == matrix1[5][1] and
            int(row5column2.get()) == matrix1[5][2] and
            int(row5column3.get()) == matrix1[5][3] and
            int(row5column4.get()) == matrix1[5][4] and
            int(row5column5.get()) == matrix1[5][5] and
            int(row5column6.get()) == matrix1[5][6] and
            int(row5column7.get()) == matrix1[5][7] and
            int(row5column8.get()) == matrix1[5][8] and
            int(row6column0.get()) == matrix1[6][0] and
            int(row6column1.get()) == matrix1[6][1] and
            int(row6column2.get()) == matrix1[6][2] and
            int(row6column3.get()) == matrix1[6][3] and
            int(row6column4.get()) == matrix1[6][4] and
            int(row6column5.get()) == matrix1[6][5] and
            int(row6column6.get()) == matrix1[6][6] and
            int(row6column7.get()) == matrix1[6][7] and
            int(row6column8.get()) == matrix1[6][8] and
            int(row7column0.get()) == matrix1[7][0] and
            int(row7column1.get()) == matrix1[7][1] and
            int(row7column2.get()) == matrix1[7][2] and
            int(row7column3.get()) == matrix1[7][3] and
            int(row7column4.get()) == matrix1[7][4] and
            int(row7column5.get()) == matrix1[7][5] and
            int(row7column6.get()) == matrix1[7][6] and
            int(row7column7.get()) == matrix1[7][7] and
            int(row7column8.get()) == matrix1[7][8] and
            int(row8column0.get()) == matrix1[8][0] and
            int(row8column1.get()) == matrix1[8][1] and
            int(row8column2.get()) == matrix1[8][2] and
            int(row8column3.get()) == matrix1[8][3] and
            int(row8column4.get()) == matrix1[8][4] and
            int(row8column5.get()) == matrix1[8][5] and
            int(row8column6.get()) == matrix1[8][6] and
            int(row8column7.get()) == matrix1[8][7] and
            int(row8column8.get()) == matrix1[8][8]
    ):
        print("Completed")
        win_image.grid(row=10,column=0,columnspan=9)
    else:
        print("Wrong")
        win_image.grid(row=10, column=0,columnspan=9)


row0column0 = Entry(root,width=5)
row0column0.grid(row=0,column=0)
row0column0.insert(0,matrix[0][0])
row0column1 = Entry(root,width=5)
row0column1.grid(row=0,column=1)
row0column1.insert(0,matrix[0][1])
row0column2 = Entry(root,width=5)
row0column2.grid(row=0,column=2)
row0column2.insert(0,matrix[0][2])
row0column3 = Entry(root,width=5)
row0column3.grid(row=0,column=3)
row0column3.insert(0,matrix[0][3])
row0column4 = Entry(root,width=5)
row0column4.grid(row=0,column=4)
row0column4.insert(0,matrix[0][4])
row0column5 = Entry(root,width=5)
row0column5.grid(row=0,column=5)
row0column5.insert(0,matrix[0][5])
row0column6 = Entry(root,width=5)
row0column6.grid(row=0,column=6)
row0column6.insert(0,matrix[0][6])
row0column7 = Entry(root,width=5)
row0column7.grid(row=0,column=7)
row0column7.insert(0,matrix[0][7])
row0column8 = Entry(root,width=5)
row0column8.grid(row=0,column=8)
row0column8.insert(0,matrix[0][8])


row1column0 = Entry(root,width=5)
row1column0.grid(row=1,column=0)
row1column0.insert(0,matrix[1][0])
row1column1 = Entry(root,width=5)
row1column1.grid(row=1,column=1)
row1column1.insert(0,matrix[1][1])
row1column2 = Entry(root,width=5)
row1column2.grid(row=1,column=2)
row1column2.insert(0,matrix[1][2])
row1column3 = Entry(root,width=5)
row1column3.grid(row=1,column=3)
row1column3.insert(0,matrix[1][3])
row1column4 = Entry(root,width=5)
row1column4.grid(row=1,column=4)
row1column4.insert(0,matrix[1][4])
row1column5 = Entry(root,width=5)
row1column5.grid(row=1,column=5)
row1column5.insert(0,matrix[1][5])
row1column6 = Entry(root,width=5)
row1column6.grid(row=1,column=6)
row1column6.insert(0,matrix[1][6])
row1column7 = Entry(root,width=5)
row1column7.grid(row=1,column=7)
row1column7.insert(0,matrix[1][7])
row1column8 = Entry(root,width=5)
row1column8.grid(row=1,column=8)
row1column8.insert(0,matrix[1][8])

row2column0 = Entry(root,width=5)
row2column0.grid(row=2,column=0)
row2column0.insert(0,matrix[2][0])
row2column1 = Entry(root,width=5)
row2column1.grid(row=2,column=1)
row2column1.insert(0,matrix[2][1])
row2column2 = Entry(root,width=5)
row2column2.grid(row=2,column=2)
row2column2.insert(0,matrix[2][2])
row2column3 = Entry(root,width=5)
row2column3.grid(row=2,column=3)
row2column3.insert(0,matrix[2][3])
row2column4 = Entry(root,width=5)
row2column4.grid(row=2,column=4)
row2column4.insert(0,matrix[2][4])
row2column5 = Entry(root,width=5)
row2column5.grid(row=2,column=5)
row2column5.insert(0,matrix[2][5])
row2column6 = Entry(root,width=5)
row2column6.grid(row=2,column=6)
row2column6.insert(0,matrix[2][6])
row2column7 = Entry(root,width=5)
row2column7.grid(row=2,column=7)
row2column7.insert(0,matrix[2][7])
row2column8 = Entry(root,width=5)
row2column8.grid(row=2,column=8)
row2column8.insert(0,matrix[2][8])


row3column0 = Entry(root,width=5)
row3column0.grid(row=3,column=0)
row3column0.insert(0,matrix[3][0])
row3column1 = Entry(root,width=5)
row3column1.grid(row=3,column=1)
row3column1.insert(0,matrix[3][1])
row3column2 = Entry(root,width=5)
row3column2.grid(row=3,column=2)
row3column2.insert(0,matrix[3][2])
row3column3 = Entry(root,width=5)
row3column3.grid(row=3,column=3)
row3column3.insert(0,matrix[3][3])
row3column4 = Entry(root,width=5)
row3column4.grid(row=3,column=4)
row3column4.insert(0,matrix[3][4])
row3column5 = Entry(root,width=5)
row3column5.grid(row=3,column=5)
row3column5.insert(0,matrix[3][5])
row3column6 = Entry(root,width=5)
row3column6.grid(row=3,column=6)
row3column6.insert(0,matrix[3][6])
row3column7 = Entry(root,width=5)
row3column7.grid(row=3,column=7)
row3column7.insert(0,matrix[3][7])
row3column8 = Entry(root,width=5)
row3column8.grid(row=3,column=8)
row3column8.insert(0,matrix[3][8])


row4column0 = Entry(root,width=5)
row4column0.grid(row=4,column=0)
row4column0.insert(0,matrix[4][0])
row4column1 = Entry(root,width=5)
row4column1.grid(row=4,column=1)
row4column1.insert(0,matrix[4][1])
row4column2 = Entry(root,width=5)
row4column2.grid(row=4,column=2)
row4column2.insert(0,matrix[4][2])
row4column3 = Entry(root,width=5)
row4column3.grid(row=4,column=3)
row4column3.insert(0,matrix[4][3])
row4column4 = Entry(root,width=5)
row4column4.grid(row=4,column=4)
row4column4.insert(0,matrix[4][4])
row4column5 = Entry(root,width=5)
row4column5.grid(row=4,column=5)
row4column5.insert(0,matrix[4][5])
row4column6 = Entry(root,width=5)
row4column6.grid(row=4,column=6)
row4column6.insert(0,matrix[4][6])
row4column7 = Entry(root,width=5)
row4column7.grid(row=4,column=7)
row4column7.insert(0,matrix[4][7])
row4column8 = Entry(root,width=5)
row4column8.grid(row=4,column=8)
row4column8.insert(0,matrix[4][8])


row5column0 = Entry(root,width=5)
row5column0.grid(row=5,column=0)
row5column0.insert(0,matrix[5][0])
row5column1 = Entry(root,width=5)
row5column1.grid(row=5,column=1)
row5column1.insert(0,matrix[5][1])
row5column2 = Entry(root,width=5)
row5column2.grid(row=5,column=2)
row5column2.insert(0,matrix[5][2])
row5column3 = Entry(root,width=5)
row5column3.grid(row=5,column=3)
row5column3.insert(0,matrix[5][3])
row5column4 = Entry(root,width=5)
row5column4.grid(row=5,column=4)
row5column4.insert(0,matrix[5][4])
row5column5 = Entry(root,width=5)
row5column5.grid(row=5,column=5)
row5column5.insert(0,matrix[5][5])
row5column6 = Entry(root,width=5)
row5column6.grid(row=5,column=6)
row5column6.insert(0,matrix[5][6])
row5column7 = Entry(root,width=5)
row5column7.grid(row=5,column=7)
row5column7.insert(0,matrix[5][7])
row5column8 = Entry(root,width=5)
row5column8.grid(row=5,column=8)
row5column8.insert(0,matrix[5][8])

row6column0 = Entry(root,width=5)
row6column0.grid(row=6,column=0)
row6column0.insert(0,matrix[6][0])
row6column1 = Entry(root,width=5)
row6column1.grid(row=6,column=1)
row6column1.insert(0,matrix[6][1])
row6column2 = Entry(root,width=5)
row6column2.grid(row=6,column=2)
row6column2.insert(0,matrix[6][2])
row6column3 = Entry(root,width=5)
row6column3.grid(row=6,column=3)
row6column3.insert(0,matrix[6][3])
row6column4 = Entry(root,width=5)
row6column4.grid(row=6,column=4)
row6column4.insert(0,matrix[6][4])
row6column5 = Entry(root,width=5)
row6column5.grid(row=6,column=5)
row6column5.insert(0,matrix[6][5])
row6column6 = Entry(root,width=5)
row6column6.grid(row=6,column=6)
row6column6.insert(0,matrix[6][6])
row6column7 = Entry(root,width=5)
row6column7.grid(row=6,column=7)
row6column7.insert(0,matrix[6][7])
row6column8 = Entry(root,width=5)
row6column8.grid(row=6,column=8)
row6column8.insert(0,matrix[6][8])


row7column0 = Entry(root,width=5)
row7column0.grid(row=7,column=0)
row7column0.insert(0,matrix[7][0])
row7column1 = Entry(root,width=5)
row7column1.grid(row=7,column=1)
row7column1.insert(0,matrix[7][1])
row7column2 = Entry(root,width=5)
row7column2.grid(row=7,column=2)
row7column2.insert(0,matrix[7][2])
row7column3 = Entry(root,width=5)
row7column3.grid(row=7,column=3)
row7column3.insert(0,matrix[7][3])
row7column4 = Entry(root,width=5)
row7column4.grid(row=7,column=4)
row7column4.insert(0,matrix[7][4])
row7column5 = Entry(root,width=5)
row7column5.grid(row=7,column=5)
row7column5.insert(0,matrix[7][5])
row7column6 = Entry(root,width=5)
row7column6.grid(row=7,column=6)
row7column6.insert(0,matrix[7][6])
row7column7 = Entry(root,width=5)
row7column7.grid(row=7,column=7)
row7column7.insert(0,matrix[7][7])
row7column8 = Entry(root,width=5)
row7column8.grid(row=7,column=8)
row7column8.insert(0,matrix[7][8])


row8column0 = Entry(root,width=5)
row8column0.grid(row=8,column=0)
row8column0.insert(0,matrix[8][0])
row8column1 = Entry(root,width=5)
row8column1.grid(row=8,column=1)
row8column1.insert(0,matrix[8][1])
row8column2 = Entry(root,width=5)
row8column2.grid(row=8,column=2)
row8column2.insert(0,matrix[8][2])
row8column3 = Entry(root,width=5)
row8column3.grid(row=8,column=3)
row8column3.insert(0,matrix[8][3])
row8column4 = Entry(root,width=5)
row8column4.grid(row=8,column=4)
row8column4.insert(0,matrix[8][4])
row8column5 = Entry(root,width=5)
row8column5.grid(row=8,column=5)
row8column5.insert(0,matrix[8][5])
row8column6 = Entry(root,width=5)
row8column6.grid(row=8,column=6)
row8column6.insert(0,matrix[8][6])
row8column7 = Entry(root,width=5)
row8column7.grid(row=8,column=7)
row8column7.insert(0,matrix[8][7])
row8column8 = Entry(root,width=5)
row8column8.grid(row=8,column=8)
row8column8.insert(0,matrix[8][8])
Submit = Button(root,text = "Submit",command = Submitted)
Submit.grid(row=9,column=0,columnspan=9)
def check(number,row,column,matrix1):
    for i in range(0,len(matrix1[row])):
        if(matrix1[row][i] == number and i != column):
            return False
    for i in range(0,len(matrix1)):
        if(matrix1[i][column] == number and i != row):
            return False
    for i in range(0 + row - (row % 3),3 + row - (row % 3)):
        for j in range(0 + column - (column % 3), 3 + column - (column % 3)):
            if(matrix1[i][j] == number and i != row and j != column):
                return False
    return True
def show_case_matrix(matrix1):
    for i in range(0,len(matrix1)):
        for j in range(0,len(matrix1[0])):
            print(matrix1[i][j]," ",end="")
            if(j%3 == 2):
                print("|"," ",end="")
        if(i%3 == 2):
            print("\n","-"*(11*len(matrix[0])//3),end="",sep="")
        print()
def empty_check(matrix1):
    global l
    for i in range(0,len(matrix1)):
        for j in range(0,len(matrix1[0])):
            if(matrix1[i][j] == 0):
                l = [i,j]
                return True
    return False
l = [0,0]
def sudoko_solver(matrix1):
    if(not empty_check(matrix1)):
        return True
    row,column = l[0],l[1]
    for _ in range(1,10):
        if(check(_,row,column,matrix1)):
            matrix1[row][column] = _
            if(sudoko_solver(matrix1)):
                return True
            matrix1[row][column]=0
    return False
if(sudoko_solver(matrix1)):
    show_case_matrix(matrix1)
else:
    print("No solution")
root.mainloop()
