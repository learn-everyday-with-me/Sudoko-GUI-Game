from tkinter import *
import copy
root = Tk()
root.title("Modified Sudoko")
matrix =[  [3,0,6,5,0,8,4,0,0],
          [5,2,0,0,0,0,0,0,0],
          [0,8,7,0,0,0,0,3,1],
          [0,0,3,0,1,0,0,8,0],
          [9,0,0,8,6,3,0,0,5],
          [0,5,0,0,9,0,6,0,0],
          [1,3,0,0,0,0,2,5,0],
          [0,0,0,0,0,0,0,7,4],
          [0,0,5,2,0,6,3,0,0]
     ]
matrix1 = copy.deepcopy(matrix[:][:])
print(matrix)

def sudoko_check():
    if(int(row0column0["text"]) == matrix1[0][0] and
            int(row0column1["text"]) == matrix1[0][1] and
            int(row0column2["text"]) == matrix1[0][2] and
            int(row0column3["text"]) == matrix1[0][3] and
            int(row0column4["text"]) == matrix1[0][4] and
            int(row0column5["text"]) == matrix1[0][5] and
            int(row0column6["text"]) == matrix1[0][6] and
            int(row0column7["text"]) == matrix1[0][7] and
            int(row0column8["text"]) == matrix1[0][8] and
            int(row1column0["text"]) == matrix1[1][0] and
            int(row1column1["text"]) == matrix1[1][1] and
            int(row1column2["text"]) == matrix1[1][2] and
            int(row1column3["text"]) == matrix1[1][3] and
            int(row1column4["text"]) == matrix1[1][4] and
            int(row1column5["text"]) == matrix1[1][5] and
            int(row1column6["text"]) == matrix1[1][6] and
            int(row1column7["text"]) == matrix1[1][7] and
            int(row1column8["text"]) == matrix1[1][8] and
            int(row2column0["text"]) == matrix1[2][0] and
            int(row2column1["text"]) == matrix1[2][1] and
            int(row2column2["text"]) == matrix1[2][2] and
            int(row2column3["text"]) == matrix1[2][3] and
            int(row2column4["text"]) == matrix1[2][4] and
            int(row2column5["text"]) == matrix1[2][5] and
            int(row2column6["text"]) == matrix1[2][6] and
            int(row2column7["text"]) == matrix1[2][7] and
            int(row2column8["text"]) == matrix1[2][8] and
            int(row3column0["text"]) == matrix1[3][0] and
            int(row3column1["text"]) == matrix1[3][1] and
            int(row3column2["text"]) == matrix1[3][2] and
            int(row3column3["text"]) == matrix1[3][3] and
            int(row3column4["text"]) == matrix1[3][4] and
            int(row3column5["text"]) == matrix1[3][5] and
            int(row3column6["text"]) == matrix1[3][6] and
            int(row3column7["text"]) == matrix1[3][7] and
            int(row3column8["text"]) == matrix1[3][8] and
            int(row4column0["text"]) == matrix1[4][0] and
            int(row4column1["text"]) == matrix1[4][1] and
            int(row4column2["text"]) == matrix1[4][2] and
            int(row4column3["text"]) == matrix1[4][3] and
            int(row4column4["text"]) == matrix1[4][4] and
            int(row4column5["text"]) == matrix1[4][5] and
            int(row4column6["text"]) == matrix1[4][6] and
            int(row4column7["text"]) == matrix1[4][7] and
            int(row4column8["text"]) == matrix1[4][8] and
            int(row5column0["text"]) == matrix1[5][0] and
            int(row5column1["text"]) == matrix1[5][1] and
            int(row5column2["text"]) == matrix1[5][2] and
            int(row5column3["text"]) == matrix1[5][3] and
            int(row5column4["text"]) == matrix1[5][4] and
            int(row5column5["text"]) == matrix1[5][5] and
            int(row5column6["text"]) == matrix1[5][6] and
            int(row5column7["text"]) == matrix1[5][7] and
            int(row5column8["text"]) == matrix1[5][8] and
            int(row6column0["text"]) == matrix1[6][0] and
            int(row6column1["text"]) == matrix1[6][1] and
            int(row6column2["text"]) == matrix1[6][2] and
            int(row6column3["text"]) == matrix1[6][3] and
            int(row6column4["text"]) == matrix1[6][4] and
            int(row6column5["text"]) == matrix1[6][5] and
            int(row6column6["text"]) == matrix1[6][6] and
            int(row6column7["text"]) == matrix1[6][7] and
            int(row6column8["text"]) == matrix1[6][8] and
            int(row7column0["text"]) == matrix1[7][0] and
            int(row7column1["text"]) == matrix1[7][1] and
            int(row7column2["text"]) == matrix1[7][2] and
            int(row7column3["text"]) == matrix1[7][3] and
            int(row7column4["text"]) == matrix1[7][4] and
            int(row7column5["text"]) == matrix1[7][5] and
            int(row7column6["text"]) == matrix1[7][6] and
            int(row7column7["text"]) == matrix1[7][7] and
            int(row7column8["text"]) == matrix1[7][8] and
            int(row8column0["text"]) == matrix1[8][0] and
            int(row8column1["text"]) == matrix1[8][1] and
            int(row8column2["text"]) == matrix1[8][2] and
            int(row8column3["text"]) == matrix1[8][3] and
            int(row8column4["text"]) == matrix1[8][4] and
            int(row8column5["text"]) == matrix1[8][5] and
            int(row8column6["text"]) == matrix1[8][6] and
            int(row8column7["text"]) == matrix1[8][7] and
            int(row8column8["text"]) == matrix1[8][8]):
        correct_ans = Label(root,text = "Correct")
        correct_ans.grid(row=12,column=0,columnspan=11)
    else:
        wrong_ans = Label(root, text="Wrong")
        wrong_ans.grid(row=12, column=0, columnspan=11)


def update(i,j):
    number = int(eval("row" + str(i) + "column" + str(j))["text"])
    if(matrix[i][j] == 0):
        if (number < 9):
            number = number + 1
        else:
            number = 0
    eval("row" + str(i) + "column" + str(j))["text"] = str(number)
# for i in range(0, 9):
#     for j in range(0, 9):
#         a[i][j] = Button(root, text=str(matrix1[i][j]), width=5, command=update)
#         a[i][j].grid(row=i, column=j)
i,j=0,0
row0column0 = Button(root,width=5,text = str(matrix[0][0]),command =lambda: update(0,0))
row0column0.grid(row=0+i,column=0+j)
row0column1 = Button(root,width=5,text = str(matrix[0][1]),command =lambda: update(0,1))
row0column1.grid(row=0+i,column=1+j)
row0column2 = Button(root,width=5,text = str(matrix[0][2]),command =lambda: update(0,2))
row0column2.grid(row=0+i,column=2+j)
j = 1
label1 = Label(root,text="|")
label1.grid(row=0, column=3)
row0column3 = Button(root,width=5,text = str(matrix[0][3]),command =lambda: update(0,3))
row0column3.grid(row=0+i,column=3+j)
row0column4 = Button(root,width=5,text = str(matrix[0][4]),command =lambda: update(0,4))
row0column4.grid(row=0+i,column=4+j)
row0column5 = Button(root,width=5,text = str(matrix[0][5]),command =lambda: update(0,5))
row0column5.grid(row=0+i,column=5+j)
j=2
label1 = Label(root,text="|")
label1.grid(row=0, column=7)
row0column6 = Button(root,width=5,text = str(matrix[0][6]),command =lambda: update(0,6))
row0column6.grid(row=0+i,column=6+j)
row0column7 = Button(root,width=5,text = str(matrix[0][7]),command =lambda: update(0,7))
row0column7.grid(row=0+i,column=7+j)
row0column8 = Button(root,width=5,text = str(matrix[0][8]),command =lambda: update(0,8))
row0column8.grid(row=0+i,column=8+j)


j=0
row1column0 = Button(root,width=5,text = str(matrix[1][0]),command =lambda: update(1,0))
row1column0.grid(row=1+i,column=0+j)
row1column1 = Button(root,width=5,text = str(matrix[1][1]),command =lambda: update(1,1))
row1column1.grid(row=1+i,column=1+j)
row1column2 = Button(root,width=5,text = str(matrix[1][2]),command =lambda: update(1,2))
row1column2.grid(row=1+i,column=2+j)
j=1
label1 = Label(root,text="|")
label1.grid(row=1, column=3)
row1column3 = Button(root,width=5,text = str(matrix[1][3]),command =lambda: update(1,3))
row1column3.grid(row=1+i,column=3+j)
row1column4 = Button(root,width=5,text = str(matrix[1][4]),command =lambda: update(1,4))
row1column4.grid(row=1+i,column=4+j)
row1column5 = Button(root,width=5,text = str(matrix[1][5]),command =lambda: update(1,5))
row1column5.grid(row=1+i,column=5+j)
j=2
label1 = Label(root,text="|")
label1.grid(row=1, column=7)
row1column6 = Button(root,width=5,text = str(matrix[1][6]),command =lambda: update(1,6))
row1column6.grid(row=1+i,column=6+j)
row1column7 = Button(root,width=5,text = str(matrix[1][7]),command =lambda: update(1,7))
row1column7.grid(row=1+i,column=7+j)
row1column8 = Button(root,width=5,text = str(matrix[1][8]),command =lambda: update(1,8))
row1column8.grid(row=1+i,column=8+j)


j=0
row2column0 = Button(root,width=5,text = str(matrix[2][0]),command =lambda: update(2,0))
row2column0.grid(row=2+i,column=0+j)
row2column1 = Button(root,width=5,text = str(matrix[2][1]),command =lambda: update(2,1))
row2column1.grid(row=2+i,column=1+j)
row2column2 = Button(root,width=5,text = str(matrix[2][2]),command =lambda: update(2,2))
row2column2.grid(row=2+i,column=2+j)
j=1
label1 = Label(root,text="|")
label1.grid(row=2, column=3)
row2column3 = Button(root,width=5,text = str(matrix[2][3]),command =lambda: update(2,3))
row2column3.grid(row=2+i,column=3+j)
row2column4 = Button(root,width=5,text = str(matrix[2][4]),command =lambda: update(2,4))
row2column4.grid(row=2+i,column=4+j)
row2column5 = Button(root,width=5,text = str(matrix[2][5]),command =lambda: update(2,5))
row2column5.grid(row=2+i,column=5+j)
j=2
label1 = Label(root,text="|")
label1.grid(row=2, column=7)
row2column6 = Button(root,width=5,text = str(matrix[2][6]),command =lambda: update(2,6))
row2column6.grid(row=2+i,column=6+j)
row2column7 = Button(root,width=5,text = str(matrix[2][7]),command =lambda: update(2,7))
row2column7.grid(row=2+i,column=7+j)
row2column8 = Button(root,width=5,text = str(matrix[2][8]),command =lambda: update(2,8))
row2column8.grid(row=2+i,column=8+j)

j=0
label1 = Label(root,text="---------------------------------------------------------------")
label1.grid(row=3, column=0,columnspan=11)
i=1
row3column0 = Button(root,width=5,text = str(matrix[3][0]),command =lambda: update(3,0))
row3column0.grid(row=3+i,column=0+j)
row3column1 = Button(root,width=5,text = str(matrix[3][1]),command =lambda: update(3,1))
row3column1.grid(row=3+i,column=1+j)
row3column2 = Button(root,width=5,text = str(matrix[3][2]),command =lambda: update(3,2))
row3column2.grid(row=3+i,column=2+j)
j=1
label1 = Label(root,text="|")
label1.grid(row=3+i, column=3)
row3column3 = Button(root,width=5,text = str(matrix[3][3]),command =lambda: update(3,3))
row3column3.grid(row=3+i,column=3+j)
row3column4 = Button(root,width=5,text = str(matrix[3][4]),command =lambda: update(3,4))
row3column4.grid(row=3+i,column=4+j)
row3column5 = Button(root,width=5,text = str(matrix[3][5]),command =lambda: update(3,5))
row3column5.grid(row=3+i,column=5+j)
j=2
label1 = Label(root,text="|")
label1.grid(row=3+i, column=7)
row3column6 = Button(root,width=5,text = str(matrix[3][6]),command =lambda: update(3,6))
row3column6.grid(row=3+i,column=6+j)
row3column7 = Button(root,width=5,text = str(matrix[3][7]),command =lambda: update(3,7))
row3column7.grid(row=3+i,column=7+j)
row3column8 = Button(root,width=5,text = str(matrix[3][8]),command =lambda: update(3,8))
row3column8.grid(row=3+i,column=8+j)



j=0
row4column0 = Button(root,width=5,text = str(matrix[4][0]),command =lambda: update(4,0))
row4column0.grid(row=4+i,column=0+j)
row4column1 = Button(root,width=5,text = str(matrix[4][1]),command =lambda: update(4,1))
row4column1.grid(row=4+i,column=1+j)
row4column2 = Button(root,width=5,text = str(matrix[4][2]),command =lambda: update(4,2))
row4column2.grid(row=4+i,column=2+j)
j=1
label1 = Label(root,text="|")
label1.grid(row=4+i, column=3)
row4column3 = Button(root,width=5,text = str(matrix[4][3]),command =lambda: update(4,3))
row4column3.grid(row=4+i,column=3+j)
row4column4 = Button(root,width=5,text = str(matrix[4][4]),command =lambda: update(4,4))
row4column4.grid(row=4+i,column=4+j)
row4column5 = Button(root,width=5,text = str(matrix[4][5]),command =lambda: update(4,5))
row4column5.grid(row=4+i,column=5+j)
j=2
label1 = Label(root,text="|")
label1.grid(row=4+i, column=7)
row4column6 = Button(root,width=5,text = str(matrix[4][6]),command =lambda: update(4,6))
row4column6.grid(row=4+i,column=6+j)
row4column7 = Button(root,width=5,text = str(matrix[4][7]),command =lambda: update(4,7))
row4column7.grid(row=4+i,column=7+j)
row4column8 = Button(root,width=5,text = str(matrix[4][8]),command =lambda: update(4,8))
row4column8.grid(row=4+i,column=8+j)


j=0
row5column0 = Button(root,width=5,text = str(matrix[5][0]),command =lambda: update(5,0))
row5column0.grid(row=5+i,column=0+j)
row5column1 = Button(root,width=5,text = str(matrix[5][1]),command =lambda: update(5,1))
row5column1.grid(row=5+i,column=1+j)
row5column2 = Button(root,width=5,text = str(matrix[5][2]),command =lambda: update(5,2))
row5column2.grid(row=5+i,column=2+j)
j=1
label1 = Label(root,text="|")
label1.grid(row=5+i, column=3)
row5column3 = Button(root,width=5,text = str(matrix[5][3]),command =lambda: update(5,3))
row5column3.grid(row=5+i,column=3+j)
row5column4 = Button(root,width=5,text = str(matrix[5][4]),command =lambda: update(5,4))
row5column4.grid(row=5+i,column=4+j)
row5column5 = Button(root,width=5,text = str(matrix[5][5]),command =lambda: update(5,5))
row5column5.grid(row=5+i,column=5+j)
j=2
label1 = Label(root,text="|")
label1.grid(row=5+i, column=7)
row5column6 = Button(root,width=5,text = str(matrix[5][6]),command =lambda: update(5,6))
row5column6.grid(row=5+i,column=6+j)
row5column7 = Button(root,width=5,text = str(matrix[5][7]),command =lambda: update(5,7))
row5column7.grid(row=5+i,column=7+j)
row5column8 = Button(root,width=5,text = str(matrix[5][8]),command =lambda: update(5,8))
row5column8.grid(row=5+i,column=8+j)



label1 = Label(root,text="-----------------------------------------------------------------------")
label1.grid(row=7, column=0,columnspan=11)
i=2
j=0
row6column0 = Button(root,width=5,text = str(matrix[6][0]),command =lambda: update(6,0))
row6column0.grid(row=6+i,column=0+j)
row6column1 = Button(root,width=5,text = str(matrix[6][1]),command =lambda: update(6,1))
row6column1.grid(row=6+i,column=1+j)
row6column2 = Button(root,width=5,text = str(matrix[6][2]),command =lambda: update(6,2))
row6column2.grid(row=6+i,column=2+j)
j=1
label1 = Label(root,text="|")
label1.grid(row=6+i, column=3)
row6column3 = Button(root,width=5,text = str(matrix[6][3]),command =lambda: update(6,3))
row6column3.grid(row=6+i,column=3+j)
row6column4 = Button(root,width=5,text = str(matrix[6][4]),command =lambda: update(6,4))
row6column4.grid(row=6+i,column=4+j)
row6column5 = Button(root,width=5,text = str(matrix[6][5]),command =lambda: update(6,5))
row6column5.grid(row=6+i,column=5+j)
j=2
label1 = Label(root,text="|")
label1.grid(row=6+i, column=7)
row6column6 = Button(root,width=5,text = str(matrix[6][6]),command =lambda: update(6,6))
row6column6.grid(row=6+i,column=6+j)
row6column7 = Button(root,width=5,text = str(matrix[6][7]),command =lambda: update(6,7))
row6column7.grid(row=6+i,column=7+j)
row6column8 = Button(root,width=5,text = str(matrix[6][8]),command =lambda: update(6,8))
row6column8.grid(row=6+i,column=8+j)

j=0
row7column0 = Button(root,width=5,text = str(matrix[7][0]),command =lambda: update(7,0))
row7column0.grid(row=7+i,column=0+j)
row7column1 = Button(root,width=5,text = str(matrix[7][1]),command =lambda: update(7,1))
row7column1.grid(row=7+i,column=1+j)
row7column2 = Button(root,width=5,text = str(matrix[7][2]),command =lambda: update(7,2))
row7column2.grid(row=7+i,column=2+j)
j=1
label1 = Label(root,text="|")
label1.grid(row=7+i, column=3)
row7column3 = Button(root,width=5,text = str(matrix[7][3]),command =lambda: update(7,3))
row7column3.grid(row=7+i,column=3+j)
row7column4 = Button(root,width=5,text = str(matrix[7][4]),command =lambda: update(7,4))
row7column4.grid(row=7+i,column=4+j)
row7column5 = Button(root,width=5,text = str(matrix[7][5]),command =lambda: update(7,5))
row7column5.grid(row=7+i,column=5+j)
j=2
label1 = Label(root,text="|")
label1.grid(row=7+i, column=7)
row7column6 = Button(root,width=5,text = str(matrix[7][6]),command =lambda: update(7,6))
row7column6.grid(row=7+i,column=6+j)
row7column7 = Button(root,width=5,text = str(matrix[7][7]),command =lambda: update(7,7))
row7column7.grid(row=7+i,column=7+j)
row7column8 = Button(root,width=5,text = str(matrix[7][8]),command =lambda: update(7,8))
row7column8.grid(row=7+i,column=8+j)


j=0
row8column0 = Button(root,width=5,text = str(matrix[8][0]),command =lambda: update(8,0))
row8column0.grid(row=8+i,column=0+j)
row8column1 = Button(root,width=5,text = str(matrix[8][1]),command =lambda: update(8,1))
row8column1.grid(row=8+i,column=1+j)
row8column2 = Button(root,width=5,text = str(matrix[8][2]),command =lambda: update(8,2))
row8column2.grid(row=8+i,column=2+j)
j=1
label1 = Label(root,text="|")
label1.grid(row=8+i, column=3)
row8column3 = Button(root,width=5,text = str(matrix[8][3]),command =lambda: update(8,3))
row8column3.grid(row=8+i,column=3+j)
row8column4 = Button(root,width=5,text = str(matrix[8][4]),command =lambda: update(8,4))
row8column4.grid(row=8+i,column=4+j)
row8column5 = Button(root,width=5,text = str(matrix[8][5]),command =lambda: update(8,5))
row8column5.grid(row=8+i,column=5+j)
j=2
label1 = Label(root,text="|")
label1.grid(row=8+i, column=7)
row8column6 = Button(root,width=5,text = str(matrix[8][6]),command =lambda: update(8,6))
row8column6.grid(row=8+i,column=6+j)
row8column7 = Button(root,width=5,text = str(matrix[8][7]),command =lambda: update(8,7))
row8column7.grid(row=8+i,column=7+j)
row8column8 = Button(root,width=5,text = str(matrix[8][8]),command =lambda: update(8,8))
row8column8.grid(row=8+i,column=8+j)



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
            print("\n","-"*(11*len(matrix1[0])//3),end="",sep="")
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

print(matrix)
Submit = Button(root,text = "Submit",command=sudoko_check)
Submit.grid(row=11,column=0,columnspan=11)



root.mainloop() 