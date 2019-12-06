import math


"""
###############
TASK 1: 
Diffie-Hellmann Keyexchange
"""
p = 467
g = 2

secret_a_b = [(2, 5), (400, 134), (228, 57)]
A = 0
B = 0

for sample in secret_a_b:

    A = (g ** sample[0]) % p
    B = (g ** sample[1]) % p
    K_A = (B ** sample[0]) % p
    K_B = (A ** sample[1]) % p
    assert(K_A == K_B)
    print("Key K_A is:", K_A)
    print("Key K_B is:", K_B)

    check = (g ** (sample[0] * sample[1])) % p
    print("Share key check:", check)





"""
###############
TASK 2: 
Verschlusseln Sie die Nachricht x= 9 mit den RSA Parametern p= 5, q= 11, e= 3
Berechnen  Sie  den  zugehorigen  privaten  Schlussel  und  entschlusseln  Sie zur Uberprung die verschlusselte Nachricht
"""


def modinv(e, phi):
    d_old = 0; r_old = phi
    d_new = 1; r_new = e
    while r_new > 0:
        a = r_old // r_new
        (d_old, d_new) = (d_new, d_old - a * d_new)
        (r_old, r_new) = (r_new, r_old - a * r_new)
    return d_old % phi if r_old == 1 else None


print("Task 2: ")
message = 9
p = 5
q = 11
rsa_exp = 3
print("Original message: ", message)

n = p * q
psi_n = (p - 1) * (q - 1)

r = math.gcd(rsa_exp, psi_n)
print("gcd = ", r)

secret_exp = modinv(rsa_exp, psi_n)
print("n = ", n)
print("psi_n = ", psi_n)
print("secret_exp = ", secret_exp)


# encoding
# ciper = (9 ** 3) mod (5 * 11) = 729 mod 55 = 13
ciper_rsa = (message ** rsa_exp) % n
print("ENCODED Ciper:", ciper_rsa)

# decoding

message_restored = (ciper_rsa ** secret_exp) % n
print("Restored:", message_restored)

"""
###############
TASK 3: 
p= 41 und q= 17.
Welche der Zahlen e1= 32 und e2= 39 ist als  offentlicher RSA Exponent geeignet?
Berechnen Sie den privaten Exponenten mit Hilfe  Erweiterten Euklidischen Algorithmus.
"""

p = 41
q = 17
rsa_exp1 = 32
rsa_exp2 = 39

n = p * q
psi_n = (p - 1) * (q - 1)

# In other words, given 𝑒 and 𝜑, we wish to find an integer solution (𝑑,𝑘) to the linear equation
# d*e + k*psi = r

print("Task 3: ")
r1 = math.gcd(rsa_exp1, psi_n)
print("gcd exp1 = ", r1)

r2 = math.gcd(rsa_exp2, psi_n)
print("gcd exp1 = ", r2)
