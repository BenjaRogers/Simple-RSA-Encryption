#############################
# Simple RSA encoder/decoder
# Benjamin S. Rogers
# 4/23/2021
##############################

import random
from time import sleep
MIN = 100
MAX = 500

dic = {   70:'What is up?',
        71:'You are fast!',
        72:'All your trinkets belong to us.',
        73:'Someone on our team thinks someone on your team are in the same class.',
        74:'You are the weakest link.',
        75:'Encryption is fun;',
        76:'Spring is my favorite season',
        77:'Enjoy your morning beverage',
        78:'I am an early riser',
        79:'I am not an early riser',
        80:'Wake Tech is my school',
        81:'CSC 120 Computing Fundamentals',
        82:'Best wishes to you'
}
# Function to check whether num is prime
def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# create prime numbers p & q 
def get_p_q():
    p = random.randrange(MIN, MAX)
    q = random.randrange(MIN, MAX)

    while check_prime(p) == False:
        p = random.randrange(MIN, MAX)

    while check_prime(q) == False:
        q = random.randrange(MIN, MAX)

    return p, q

# e must be relatively prime with var nn
def create_public_key(nn):
    e = random.randrange(2, nn)
    rel_prime = euclid_gcd(e, nn)
    
    #if euclid_gc() returns 1 than the 2 numbers are relatively prime
    while rel_prime != 1:
        e = random.randrange(2, nn)
        rel_prime = euclid_gcd(e, nn)
    return e

# e * d - 1 = nn * k 
def create_private_key(e, nn):
    k = 1
    d = 1
    while d < nn:
        while nn * k <= d * e:
            if ((d * e) -1) / (nn * k) == 1:
                return d, k
            k += 1
        d += 1
    
# euclids formula to find if numbers a & are relatively prime
def euclid_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def encrypt_message(e, n, m):
    enc_message = (m ** e) % n
    return enc_message

def decrypt_message(d, n, m):
    dec_message = (m ** d) % n
    return dec_message

def get_message(dictionary):
    message = 0
    print("70:'What is up?'\n"
        "71:'You are fast!'\n"
        "72:'All your trinkets belong to us.'\n"
        "73:'Someone on our team thinks someone on your team are in the same class.'\n"
        "74:'You are the weakest link.'\n"
        "75:'Encryption is fun;'\n"
        "76:'Spring is my favorite season'\n"
        "77:'Enjoy your morning beverage'\n"
        "78:'I am an early riser'\n"
        "79:'I am not an early riser'\n"
        "80:'Wake Tech is my school'\n"
        "81:'CSC 120 Computing Fundamentals'\n"
        "82:'Best wishes to you'\n"
    )
    message = int(input("Refering to the list above please enter an integer between 70-82 to send the given message: "))
    print(f"The message you want to send is {message} - {dictionary[message]}")
    return message

def main():
    print("Generating Keys >>>")
        # generate random prime numbers and make sure they are different
    p, q = get_p_q()
    while p == q:
        get_p_q()
    sleep(1)
    print(".")

    # Calculate n and nn
    n = p * q
    nn = (p-1)*(q-1)
    sleep(1)
    print(".")

    # generate public and private keys and make sure they are different
    e = create_public_key(nn)
    d, k = create_private_key(e, nn)
    while e == d:
        e = create_public_key(nn)
        d, k = create_private_key(e, nn)
    sleep(1)
    print(".")

    message = get_message(dic)

    print("Encoding Message >>>")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    enc = encrypt_message(e,n,message)
    dec = decrypt_message(d, n, enc)

    print("Your encoded message is", enc)
    
    print("Decoding Message >>>")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    print(f"Your Decoded message is {dec} - {dic[dec]}")
    

main()