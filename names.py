names = [“Evi”, “Madeleine”, “Dan”, “Kelsey”, “Cayden”, “Hayley”, Darian”]

print(names.sort())


optchoice = int(input("1. Check a name\n2. Replace a name \n3. Add a name"))
if optchoice < 3:
    if optchoice == 1:
        check_name = input("Enter a name").lower()
        check_name[0] = check_name[0].upper()
        if (check_name in names):
            print("name accepted")
        else:
            print("name not accepted")
    else if optchoice == 2:
        change = input("Enter a postion or name to replace")
        replacewith = input("Name")
        replacewith = replacewith.lower()
        replacewith[0] = replacewith[0].upper()
        try:
            change = int(change)
            names[change] = replacewith
        except:
            try:
                names[names.index(change)] = replacewith
                print("Change successful \n{}".format(names))
            except:
                print("name not in list\n {}".format(names))
    else:
        names.append(replacewith)
    print("List is \n{}".format(names))
else:
    print("invalid choice")