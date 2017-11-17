import string

def pw_check(password):
    if len(password) >= 24:
        ABC = dict.fromkeys(string.uppercase, True)
        abc = dict.fromkeys(string.lowercase, True)
        nums = dict.fromkeys(string.digits, True)
        sym = dict.fromkeys(string.punctuation, True)

        ABC_flag = abc_flag = nums_flag = sym_flag = True

        for char in password:
            if ABC_flag and char in ABC:
                ABC_flag = False
                print "ABC flag set"
            elif abc_flag and char in abc:
                abc_flag = False
                print "abc flag set"
            elif nums_flag and char in nums:
                nums_flag = False
                print "nums flag set"
            elif sym_flag and char in sym:
                sym_flag = False
                print "sym flag set"

        if not any((ABC_flag, abc_flag, nums_flag, sym_flag)):
            print "Valid password"
            return True

        else:
            print "Invalid password"
            return False
    else:
        return False
