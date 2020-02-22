## Jianyuan Gan
## gan00008

#Part 1: get_data_list
#==========================================
# Purpose:
#   Extract the data from a CSV file as a list of rows
# Input Parameter(s):
#   fname is a string representing the name of a file
# Return Value:
#   Returns a list of every line in that file (a list of strings)
#   OR returns -1 if the file does not exist
#==========================================
def get_data_list(fname):
    try:
        with open(fname,'r')as fo:
            line = fo.readlines()
        return line 
    except:
        return -1

print(get_data_list('grades1'))


#Part 2: hw8_index
#==========================================
# Purpose:
#   Determine which column stores the grades for hw8
# Input Parameter(s):
#   row1_str is a string containing the first row of data 
#   (the column titles) in the CSV file
# Return Value:
#   Returns the index of the column labelled 'hw8 Grade' (an integer)
#   OR returns -1 if there is no column labelled 'hw8 Grade'
#==========================================
def hw8_index(row1_str):
    li = row1_str.split(',')
    for i in li:
        if i == 'hw8 Grade':
            return li.index(i)
    return -1
##print(hw8_index("hw1 Grade,hw2 Grade,hw3 Grade,hw4 Grade,hw5 Grade,hw6 Grade,hw7 Grade,hw8 Grade,hw9 Grade\n"))

#Part 3: alter_grade
#==========================================
# Purpose:
#   Change the hw8 grade in your row string to '40'
# Input Parameter(s):
#   row_str is a string containing any row of data from the CSV file
#   idx is an index for the column you want to alter
# Return Value:
#   Returns a string identical to row_str, except with the column
#   at the given index changed to '40'
#==========================================
def alter_grade(row_str,idx):
    li = row_str.split(',')
    li[idx] = '40'
    return ','.join(li)



#Part 4: haxx
#==========================================
# Purpose:
#   Alters a gradebook CSV file so that your score on hw8 is '40'
# Input Parameter(s):
#   fname is the file name of the gradebook file
# Return Value:
#   Returns False if the file isn't open
#   Returns False if the file doesn't contain a 'hw8 Grade' column
#   Otherwise, returns True
#==========================================
def haxx(fname):
    read_rows = get_data_list(fname)
    if read_rows == -1:
        return False

    hw8_column_index = hw8_index(read_rows[0])
    if hw8_column_index == -1:
        return False

    with open(fname,'w') as file:
        for i in range(len(read_rows)):
            if "Jianyuan Gan" in read_rows[i]:
                read_rows[i] = alter_grade(read_rows[i], hw8_column_index)
            file.write(read_rows[i])
    return True

    #Hints:
    #   Use get_data_list to read in the rows from the file
    #   Use hw8_index to determine which column you need to change
    #   Write back each row unchanged, unless it contains your
    #   full name, exactly as it appears on Canvas
    #   If it does contain your name, use alter_grade to create an
    #   altered row string to write to the file instead
    #   Be sure to close the file



