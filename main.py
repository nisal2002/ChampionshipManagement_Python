
ADD = "ADDING DRIVER DETAILS"
DDD = "DELETING"
UDD = "UPDATING DRIVER DETAILS"
VCT = "VIEWING THE RALLY CROSS STANDINGS TABLE"
SRR = "SIMULATING A RANDOM RACE"
VRL = "VIEWING RACE TABLE SORTED ACCORDING TO THE DATE"
STF = "SAVE THE CURRENT DATA TO A TEXT FILE"
RFF = "LOAD DATA FROM THE SAVED TEXT FILE"
ESC = "EXIT THE PROGRAM"

class EmptyError(Exception):
    pass

def function_add():
    print("\t---|", ADD, "|---")
    while True:
        try:
            name = input("Name: ")
            name = name.lower()
            if name == "":
                raise EmptyError("Can't be empty.")
            else:
                break
        except EmptyError as error:
            print(error)
    while True:
        try:
            age = int(input("Age: "))
            age = str(age)
            break
        except ValueError:
            print("Only numbers can be input & Can't be empty.")
    while True:
        try:
            team = input("Team: ")
            team = team.lower()
            if team == "":
                raise EmptyError("Can't be empty.")
            else:
                break
        except EmptyError as error:
            print(error)
    while True:
        try:
            car = input("Car: ")
            car = car.lower()
            if car == "":
                raise EmptyError("Can't be empty.")
            else:
                break
        except EmptyError as error:
            print(error)
    while True:
        try:
            current_points = int(input("Current Points: "))
            current_points = str(current_points)
            break
        except ValueError:
            print("Only numbers can be input & Can't be empty.")
    print("\nDo you want to save the current data to file? Type STF")  # asking save data
    choice = input("Enter Choice: ")
    choice = choice.upper()
    if choice == "STF":
        with open("details.txt", "a") as fa:  # open and save into details.txt
            fa.write("\n")
            fa.write(name)
            fa.write(",")
            fa.write(age)
            fa.write(",")
            fa.write(team)
            fa.write(",")
            fa.write(car)
            fa.write(",")
            fa.write(current_points)
        fa.close()
        print("Entered data saved.")
    else:
        print("Entered data cleared.")

def function_ddd():
    print("Do you want to load the current data from file? Type RFF")
    choice = input("Enter Choice: ")
    choice = choice.upper()
    if choice == "RFF":
        with open("details.txt", "r") as fr:  # getting details from details.txt
            print("\n||||||||||||||||||||||||||||||")
            split=fr.read().split()
            for part in split:
                print(part)
            print("||||||||||||||||||||||||||||||\n")
        fr.close()
        print("\t---|", DDD, "|---")
        name = input("Enter name: ")
        name = name.lower()
        with open("details.txt") as f:  # deleting part
            for number, line in enumerate(f, 1):
                if name in line:
                    with open("details.txt", "r") as fr:
                        lines = fr.readlines()
                        point = 1
                        with open("details.txt", 'w') as fw:
                            for line in lines:
                                if point != number:
                                    fw.write(line)
                                point += 1
        f.close()
        print("Deleted.")
    else:
        print("Returned to functions")

def function_udd():
    print("Do you want to load the current data from file? Type RFF")
    choice = input("Enter Choice: ")
    choice = choice.upper()
    if choice == "RFF":
        with open("details.txt", "r") as fr:  # getting details from details.txt
            print("\n||||||||||||||||||||||||||||||")
            split = fr.read().split()
            for part in split:
                print(part)
            print("||||||||||||||||||||||||||||||\n")
        fr.close()
        print("\t---|", UDD, "|---")
        name = input("Enter name: ")
        name = name.lower()
        print("['Name,Age,Team,Car,Current Points']")
        with open("details.txt", "r") as fr:
            for line in fr.readlines():
                if name in line:
                    print(line.split())
                    index = input("Enter index for change: ")
                    ch_index = input("Enter new index: ")
                    new = line.replace(index, ch_index)  # ch_index : 'changed index'
                    record = new.split()
                    print(record)
        print("\nDo you want to save the current data to file? Type STF")
        choice_1 = input("Enter Choice: ")
        choice_1 = choice_1.upper()
        if choice_1 == "STF":
            with open("details.txt", "a") as fa:  # appending details to details.txt
                for items in record:
                    fa.write("\n")
                    fa.write(items)

            with open("details.txt") as f:  # delete part : before update record
                for number, line in enumerate(f, 1):
                    if name in line:
                        with open("details.txt", "r") as fr:
                            lines = fr.readlines()
                            point = 1
                            with open("details.txt", "w") as fw:
                                for line in lines:
                                    if point != number:
                                        fw.write(line)
                                    point += 1
            print("Entered data saved.")
        else:
            print("Entered data cleared.")
    else:
        print("Returned to functions")

def function_vct():
    print("\t---|", VCT, "|---")
    with open("details.txt", "r") as fr:
        read = fr.readline().replace("\n", "")
        while read:
            field = read.split(",")  # reversing record
            field.reverse()
            points = field[0]
            name = field[4]
            age = field[3]
            team = field[2]
            car = field[1]
            with open("sort.txt", "a") as fa:  # appending name to sort.txt
                fa.write("Current Points: ")
                fa.write(points)
                fa.write(", Name: ")
                fa.write(name)
                fa.write(", Age: ")
                fa.write(age)
                fa.write(", Team: ")
                fa.write(team)
                fa.write(", Car: ")
                fa.write(car)
                fa.write("\n")
            fa.close()
            read = fr.readline().replace("\n", "")
    fr.close()

    record = list()
    with open("sort.txt", "r") as fr:                  # sort part
        for line in fr:
            record.append(line)

    for x in range(len(record)):
        for y in range(x + 1, len(record)):

            if record[x] < record[y]:
                record[x], record[y] = record[y], record[x]

    i = 0
    j = 1
    while i < len(record):
        print("Place", j, "-", record[i], end="")
        i += 1
        j += 1
    fr.close()
    with open("sort.txt","w") as fw:  # clearing sort.txt
        fw.close()

def function_srr():
    print("\t---|", SRR, "|---")
    with open("details.txt", "r") as fr:
        read = fr.readline().replace("\n", "")
        while read:
            field = read.split(",")
            name = field[0]
            with open("sort.txt", "a") as fa:
                fa.write(name)
                fa.write("\n")
            fa.close()
            read = fr.readline().replace("\n", "")
    fr.close()

    import random

    year = [2020, 2021, 2022, 2023, 2024, 2024, 2025]
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    location = ["Nyirad", "Holjes", "Montalegre", "Barcelona", "Riga", "Norway"]

    rdm_year = random.choice(year)
    rdm_month = random.choice(month)
    rdm_location = random.choice(location)
    if rdm_month == 2:                          # randomly select year,month,date
        if rdm_year == 2020 or 2024:
            rdm_date = random.randint(1, 29)
        else:
            rdm_date = random.randint(1, 28)
    elif rdm_month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        rdm_date = random.randint(1, 31)
    else:
        rdm_date = random.randint(1, 30)

    rdm_date = str(rdm_date)
    rdm_month = str(rdm_month)
    rdm_year = str(rdm_year)

    lines_1 = open('sort.txt').read().split()
    random1 = random.choice(lines_1)
    with open("sort.txt") as f:
        for number1, line in enumerate(f, 1):
            if random1 in line:
                with open("sort.txt", "r") as fr:
                    lines = fr.readlines()
                    point = 1
                    with open("sort.txt", 'w') as fw:
                        for lin1 in lines:
                            if point != number1:
                                fw.write(lin1)
                            point += 1
                    fw.close()
                fr.close()
    fw.close()
    with open("details.txt", "r") as fr:
        for line in fr.readlines():
            if random1 in line:
                my_lst = line.split(",")
                index = my_lst[4]
                index = int(index)
                ch_index = index + 10      # adding +10 to 1st driver
                index = str(index)         # ch_index : changed index
                ch_index = str(ch_index)
                new = line.replace(index, ch_index)
                record = new.split()
                print("|||||||||| WINNER", random1, "(+10 Points) ||||||||||")
                print("Place 1 -", record,"\n")
    fr.close()
    with open("details.txt", "a") as fa:
        for items in record:
            fa.write("\n")
            fa.write(items)
    fa.close()

    with open("details.txt") as f:
        for number1, line in enumerate(f, 1):
            if random1 in line:
                with open("details.txt", "r") as fr:
                    lines = fr.readlines()
                    point = 1
                    with open("details.txt", "w") as fw:
                        for line in lines:
                            if point != number1:
                                fw.write(line)
                            point += 1
                    fw.close()
                fr.close()
    f.close()
    with open("race.txt", "a") as fa:
        fa.write("\n")
        fa.write(rdm_year)
        fa.write("/")
        fa.write(rdm_month)
        fa.write("/")
        fa.write(rdm_date)
        fa.write(" - ")
        fa.write(rdm_location)
        fa.write(" - ")
        record = str(record)
        fa.write(record)
        fa.write(" Place(1)")
    fa.close()

    lines_2 = open('sort.txt').read().split()
    random2 = random.choice(lines_2)
    with open("sort.txt") as f:
        for number2, line in enumerate(f, 1):
            if random2 in line:
                with open("sort.txt", "r") as fr:
                    lines = fr.readlines()
                    point = 1
                    with open("sort.txt", 'w') as fw:
                        for lin2 in lines:
                            if point != number2:
                                fw.write(lin2)
                            point += 1
                    fw.close()
                fr.close()
    fw.close()
    with open("details.txt", "r") as fr:
        for line in fr.readlines():
            if random2 in line:
                my_lst = line.split(",")
                index = my_lst[4]
                index = int(index)
                ch_index = index + 7        # adding +7 to 2nd driver
                index = str(index)
                ch_index = str(ch_index)
                new = line.replace(index, ch_index)
                record = new.split()
                print("|||||||||| 1ST RUNNERS-UP", random2, "(+7 Points) ||||||||||")
                print("Place 2 -", record, "\n")
    fr.close()
    with open("details.txt", "a") as fa:
        for items in record:
            fa.write("\n")
            fa.write(items)
    fa.close()

    with open("details.txt") as f:
        for number2, line in enumerate(f, 1):
            if random2 in line:
                with open("details.txt", "r") as fr:
                    lines = fr.readlines()
                    point = 1
                    with open("details.txt", "w") as fw:
                        for line in lines:
                            if point != number2:
                                fw.write(line)
                            point += 1
                    fw.close()
                fr.close()
    f.close()
    with open("race.txt", "a") as fa:
        fa.write("\n")
        fa.write(rdm_year)
        fa.write("/")
        fa.write(rdm_month)
        fa.write("/")
        fa.write(rdm_date)
        fa.write(" - ")
        fa.write(rdm_location)
        fa.write(" - ")
        record = str(record)
        fa.write(record)
        fa.write(" Place(2)")
    fa.close()

    lines_3 = open('sort.txt').read().split()
    random3 = random.choice(lines_3)
    with open("sort.txt") as f:
        for number1, line in enumerate(f, 1):
            if random3 in line:
                with open("sort.txt", "r") as fr:
                    lines = fr.readlines()
                    point = 1
                    with open("sort.txt", 'w') as fw:
                        for lin3 in lines:
                            if point != number1:
                                fw.write(lin3)
                            point += 1
                    fw.close()
                fr.close()
    fw.close()
    with open("details.txt", "r") as fr:
        for line in fr.readlines():
            if random3 in line:
                my_lst = line.split(",")
                index = my_lst[4]
                index = int(index)
                ch_index = index + 5    # adding +5 to 3rd driver
                index = str(index)
                ch_index = str(ch_index)
                new = line.replace(index, ch_index)
                record = new.split()
                print("||||||||||| 2ND RUNNERS-UP", random3, "(+5 Points) |||||||||")
                print("Place 3 -", record, "\n")
    fr.close()
    with open("details.txt", "a") as fa:
        for items in record:
            fa.write("\n")
            fa.write(items)
    fa.close()

    with open("details.txt") as f:
        for number1, line in enumerate(f, 1):
            if random3 in line:
                with open("details.txt", "r") as fr:
                    lines = fr.readlines()
                    point = 1
                    with open("details.txt", "w") as fw:
                        for line in lines:
                            if point != number1:
                                fw.write(line)
                            point += 1
                    fw.close()
                fr.close()
    f.close()
    with open("race.txt", "a") as fa:
        fa.write("\n")
        fa.write(rdm_year)
        fa.write("/")
        fa.write(rdm_month)
        fa.write("/")
        fa.write(rdm_date)
        fa.write(" - ")
        fa.write(rdm_location)
        fa.write(" - ")
        record = str(record)
        fa.write(record)
        fa.write(" Place(3)")
    fa.close()
    print("||||||||||||||||||||||| OTHER PLAYERS |||||||||||||||||||||")

    with open("sort.txt", 'r') as fp:
        count = len(fp.readlines())
    fp.close()
    i = 0
    j = 4
    while i != count:
        with open("sort.txt", 'r') as fp:
            new_line = fp.read().split()
            name = random.choice(new_line)
            with open("details.txt", "r") as fr:
                for line in fr.readlines():
                    if name in line:
                        split = line.split()
                        print("Place", j, "-", split)
                        with open("race.txt", "a") as fa:
                            fa.write("\n")
                            fa.write(rdm_year)
                            fa.write("/")
                            fa.write(rdm_month)
                            fa.write("/")
                            fa.write(rdm_date)
                            fa.write(" - ")
                            fa.write(rdm_location)
                            fa.write(" - ")
                            split = str(split)
                            fa.write(split)
                            fa.write(" Place(")
                            j = str(j)
                            fa.write(j)
                            fa.write(")")

                        fa.close()
                        j=int(j)
                        i += 1
                        j += 1

            with open("sort.txt") as f:
                for number, line in enumerate(f, 1):
                    if name in line:
                        with open("sort.txt", "r") as fr:
                            lines = fr.readlines()
                            point = 1
                            with open("sort.txt", 'w') as fw:
                                for line in lines:
                                    if point != number:
                                        fw.write(line)
                                    point += 1
    with open("race.txt", "a") as fa:
        fa.write("\n")
    fa.close()

def function_vrl():
    with open("race.txt", "r") as fr:
        read = fr.read()
    fr.close()
    with open("sort.txt","a") as fa:
        fa.write(read)
    fa.close()
    record = list()
    with open("sort.txt", "r") as fr:                  # sort part
        for line in fr:
            record.append(line)

    for x in range(len(record)):
        for y in range(x + 1, len(record)):

            if record[x] < record[y]:
                record[x], record[y] = record[y], record[x]

    i = 0
    while i < len(record):
        print(record[i], end="")
        i += 1
    fr.close()
    with open("sort.txt","w") as fw:  # clearing sort.txt
        fw.close()





print("-| WORLD RALLY CROSS CHAMPIONSHIP |-\n")
print("         CONSOLE MENU")
print("         ------------")
print("Type :-\n"
    "\tADD for Adding Driver Details\n"
    "\tDDD for Deleting\n"
    "\tUDD for Updating Driver Details\n"
    "\tVCT for Viewing The Rally Cross Standings Table\n"
    "\tSRR for Simulating A Random Race\n"
    "\tVRL for Viewing Race Table Sorted According To The Date\n\n"
    "\tSTF to Save The Current Data To A Text File\n"
    "\tRFF to Load Data From The Saved Text File\n"
    "\tESC to Exit The Program")

while True:
    print("\n~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~")
    function = input("Enter Function: ")
    function = function.upper()

    if function == "ADD":
        function_add()
    elif function == "DDD":
        function_ddd()
    elif function == "UDD":
        function_udd()
    elif function == "VCT":
        function_vct()
    elif function == "SRR":
        function_srr()
    elif function == "VRL":
        function_vrl()
    elif function == "ESC":
        print(ESC)
        break
    else:
        print("Invalid Function")