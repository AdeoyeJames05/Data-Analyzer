from random import randint as rnd

memReg = 'my_folder/members.txt'
exReg = 'my_folder/inactive.txt'
fee =('yes','no')


"""
def clean_file(current, old) creates a random data
"""
def clean_files(current, old):
    with open(current,'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for row_no in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for row_no in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


clean_files(memReg, exReg)


def clean_files(current_mem, ex_mem):
    """
    :param current_mem: has the data with all members
    :param ex_mem: has the data with all ex-members
    :return:
    """
    with open(current_mem,'r+') as write_file:
        with open(ex_mem,'a+') as append_file:
            write_file.seek(0)
            members = write_file.readlines()
            """
            convert the current member into a list (member), then removed the header 
            """
            header = members.pop(0)


            inactive = []
            """
            looped through the list (member) and added the inactive member in the empty list (inactive)
            """
            for member in members:
                if 'no' in member:
                    inactive.append(member)

            write_file.seek(0)


            """
            adding the inactive members in the ex_mem file
            """
            for member in members:
                if member in inactive:
                    append_file.write(member)
                else:
                    write_file.write(member)
            write_file.truncate()



memReg = 'my_folder/members.txt'
exReg = 'my_folder/inactive.txt'
clean_files(memReg, exReg)

headers = "Membership No  Date Joined  Active  \n"
with open(memReg, 'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())

with open(exReg, 'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
