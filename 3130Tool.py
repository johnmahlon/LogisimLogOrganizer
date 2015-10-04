def organize_log_files():
    file_from = raw_input("Please enter filename: ")

    list_of_lines = []

    with open(file_from) as f:
        header = f.readline()
        for line in f:
            list_of_lines.append(line)

    set_of_lines = set(list_of_lines)   # converts to a set which deletes duplicates
    my_list = sorted(set_of_lines)     # sort

    print "Understand the file you type in will be truncated."
    file_to = raw_input("Please enter new filename to write to: ")

    target = open(file_to, 'w')

    target.write(header)
    for line in my_list:
        target.write(line)


def binary_conversion(b):
    h = hex(int(b, 2))
    d = int(b, 2)
    print "Binary: %r \nHex: %s \nDecimal: %d\n" % (b, h, d)


def hex_conversion(h):
    d = int(h, 16)
    b = bin(d)
    print "Binary: %r \nHex: %s \nDecimal: %d\n" % (b, h, d)


def decimal_conversion(d):
    # d gets assigned int(d) so it can be converted
    d = int(d)
    h = hex(d)
    b = bin(d)
    print "Binary: %r \nHex: %s \nDecimal: %d\n" % (b, h, d)


def print_menu():
    print "\n"
    print "CSCI 3130 Lab Tool"
    print "!!! Currently numbers are unsigned !!!"
    print "\n"
    print "Menu:"
    print "1: Organize Log File"
    print "2: Binary Conversion"
    print "3: Hex Conversion"
    print "4: Decimal Conversion"
    print "Type '0' to exit"
    user_choice = raw_input("Please choose an option: ")

    if user_choice == '1':
        organize_log_files()
        print_menu()

    elif user_choice == '2':
        n = raw_input("Enter binary number: ")
        binary_conversion(n)
        print_menu()

    elif user_choice == '3':
        n = raw_input("Enter hex number: ")
        hex_conversion(n)
        print_menu()

    elif user_choice == '4':
        n = raw_input("Enter decimal(base 10) number: ")
        decimal_conversion(n)
        print_menu()

    elif user_choice == '0':
        pass

print_menu()