# Problem A: find_password
#==========================================
# Purpose:
#   Given an encrypted file, tries every possible four letter lowercase
#   password for that file until one works, and then returns the password.
# Input Parameter(s):
#   filename is a string representing the name of the encrypted file.
#   The file must be in the same folder as this script.
# Return Value:
#   Returns the password that successfully decrypts the given file
#==========================================

def find_password(filename):
    fp = open(filename)
    data = fp.read()
    password =''
    for a in range (97,123):
        for b in range (97,123):
            for c in range (97,123):
                for d in range (97,123):
                    password=chr(a)+chr(b)+chr(c)+chr(d)
                    if decrypt(data,password):
                        return password

##find_password('encrypted2.txt')


# Problem B: count_primes
#==========================================
# Purpose:
#   Prints out all prime numbers between low and high, inclusve, and
#   returns a count of how many there were.
# Input Parameter(s):
#   low is a positive integer 
#   high is a positive integer, which should be >= low
# Return Value:
#   Returns the number of prime numbers between low and high, inclusive
#==========================================
def prime_num(n):
    if n == 1:
        return False
    for x in range (2,int((n)**1/2)):   
        if n % x == 0:
            return False
        return True

def count_primes(low, high):
    a = 0
    if low > high:
        return 0
    for i in range (low,high+1):
        if prime_num(i):
            a += 1
            print(i,'is prime')
    return a
        
print(count_primes(1,20))


#Problem C: population
#==========================================
# Purpose:
#   Simulates the population of smallfish, middlefish, and bigfish over time
# Input Parameter(s):
#   small is an integer, the initial number of smallfish in the lake
#   middle is an integer, the initial number of middlefish in the lake
#   big is an integer, the initial number of bigfish in the lake
# Return Value:
#   Returns the number of weeks required for one of the populations to
#   fall below 10, or 100 if the populations are all still >= 10 after
#   100 weeks
#==========================================

##small_birth_rate = 0.1
##middle_death_rate = -0.05
##big_death_rate = -0.1
##
##
##
##def population(small, middle, big):
##    week_count = 0
##    for week in range (1,101):
##        small_birth = small * small_birth_rate
##        middle_death = middle * middle_death_rate
##        big_death = big * big_death_rate
##        if week <= 100 and small >= 10 and middle >=10 and big>=10:
##            week_count += 1
##            eaten_small_fish = 0.0002 * small * middle
##            eaten_middle_fish = 0.00025 * middle * big
##            produce_middle_fish = eaten_small_fish * 0.5
##            produce_big_fish = eaten_middle_fish * 0.8
##            
##            small = small - eaten_small_fish + small_birth
##            middle = middle - eaten_middle_fish + produce_middle_fish + middle_death
##            big = big + produce_big_fish + big_death
##            
##            print('week ',week,'-','small:',int(small),'middle:',int(middle),'big',int(big))
##            
##    return week_count
##
##print(population(800,600,1000))


#DO NOT EDIT ANYTHING BELOW THIS LINE
#Below are helper functions used for decrypting the text files.
#You don't have to understand how any of these work.

# decrypt
#==========================================
# Purpose:
#   Check whether the password is correct for a given encrypted
#   file, and print out the decrypted contents if it is.
# Input Parameter(s):
#   data is a string, representing the contents of an encrypted file.
#   password is a four letter lowercase string, representing the password
#   used to encrypt/decrypt the file contents.
# Return Value:
#   Returns True if the password is correct and the file contents
#   were printed.  Returns False and prints nothing otherwise.
#==========================================
def decrypt(data, password):
    data = data.split('\n')
    if encode(password) == int(data[0]):
        print(vigenere(data[1],password))
        return True
    return False

# encode
#==========================================
# Purpose:
#   Turn a password into a ~9 digit number
# Input Parameter(s):
#   key is a four letter string representing a password
# Return Value:
#   Returns a number between 0 and 547120140, using modular exponentiation
#   to make it difficult to reverse engineer the password from the number.
#==========================================
def encode(key):
    total = 0
    for ltr in key:
        total += ord(ltr)
        total *= 123
    return pow(total,2011,547120141)

# vigenere
#==========================================
# Purpose:
#   Decipher a message using the Vigenere cipher
# Input Parameter(s):
#   msg a string, representing the encrypted message
#   key is a four letter string, representing the cipher key
# Return Value:
#   Returns a string representing the deciphered text
#==========================================
def vigenere(msg,key):
    i = 0
    out_msg = ''
    for ltr in msg:
        out_msg += chr((ord(ltr)-ord(key[i]))%28 +97)
        i = (i+1)%len(key)
    return out_msg.replace('{',' ').replace('|','.')


