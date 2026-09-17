pan = input("Enter PAN number: ")

if len(pan) != 10:
    print("Invalid PAN number")
else:
    valid = True

    for i in range(5):
        if not ('A' <= pan[i] <= 'Z'):
            valid = False

    for i in range(5, 9):
        if not ('0' <= pan[i] <= '9'):
            valid = False

    if not ('A' <= pan[9] <= 'Z'):
        valid = False

    if valid:
        print("Valid PAN number")
    else:
        print("Invalid PAN number")