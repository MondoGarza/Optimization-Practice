class matrix:
    def __init__(self, row, column):
        self.rows = row
        self.columns = column
        self.matrix =  [[0 for i in range(self.columns)] for j in range(self.rows)]

    def populate_row(self, row_num):
        try:
            theInput = input("Please input values(val1,val2,valn): ")
            theInput = theInput.split(",")
            for column in range(self.columns):
                self.matrix[row_num-1][column] = int(theInput[column])
            self.printMatrix()
        except Exception as inst:
            print(inst)

    def printMatrix(self):
        for rows in range(self.rows):
            print(self.matrix[rows])
    
    def add_rows(self):
        try:
            scalar = int(input("Please input scalor: "))
            scalarRow = int(input("Please input row number to apply scalar: "))
            changeRow = int(input("Please input row number to apply addition to: "))
            if scalar:
                scalar = int(scalar)
                for i in range(len(self.matrix[scalarRow-1])):
                    scaledVal = self.matrix[scalarRow-1][i] * scalar
                    self.matrix[changeRow-1][i] = self.matrix[changeRow-1][i] + scaledVal
            else:
                for i in range(len(self.matrix[scalarRow-1])):
                    self.matrix[changeRow-1][i] = self.matrix[scalarRow-1][i] + self.matrix[changeRow-1][i]
            self.printMatrix()
        except Exception as inst:
            print(inst)
    
    def switch_rows(self):
        try:
            index1 = int(input("Row one number: ")) - 1
            index2 = int(input("Row two number: ")) - 1
            row1 = self.matrix[index1]
            row2 = self.matrix[index2]
            self.matrix[index1] = row2
            self.matrix[index2] = row1
            self.printMatrix()
        except Exception as inst:
            print(inst)
    
    def scale_row(self):
        try:
            scale_row = int(input("Specify which row to scale: "))
            scalar = int(input("Specify scalar: "))
            for i in range(len(self.matrix[scale_row-1])):
                self.matrix[scale_row-1][i] = self.matrix[scale_row-1][i] * scalar
            print(self.matrix)
        except Exception as inst:
            print(inst)
    
    def performOperation(self):
        print(""""p" - populate a row\n"a" - add two rows\n"sc" - scale a row by scalar\n"sw" - switch two rows""")
        operation = str(input("Please specify operation (p,a,sc,sw):"))
        if operation == "p":
            popRow = int(input("Please specify which row # to populate: "))
            self.populate_row(popRow)
        elif operation == "a":
            self.add_rows()
        elif operation == "sc":
            self.scale_row()
        elif operation == "sw":
            self.switch_rows()
        else:
            print("Unspecified operation")

# matrix(rows, columns)
rows = int(input("Specify number of rows in matrix: "))
columns = int(input("Specify number of columns in matrix: "))
mat1 = matrix(rows,columns)
while True:
    mat1.performOperation()
