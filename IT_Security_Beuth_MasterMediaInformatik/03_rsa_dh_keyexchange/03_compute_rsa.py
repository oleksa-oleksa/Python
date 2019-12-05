import math


"""
###############
TASK 2: 
Verschlusseln Sie die Nachricht x= 9 mit den RSA Parametern p= 5, q= 11, e= 3
Berechnen  Sie  den  zugehorigen  privaten  Schlussel  und  entschlusseln  Sie zur Uberprung die verschlusselte Nachricht
"""


message = 9
p = 5
q = 11
exp = 3

# encoding
n_private = p * q
print("Private key n = ", n_private)
# ciper = (9 ** 3) mod (5 * 11) = 729 mod 55 = 13
ciper_rsa = (message ** exp) // n_private
print("Ciper:", ciper_rsa)

# decoding
# ciper_rsa = (message ** exp) // n_private
# ciper_rsa * n_private = message ** exp
# message = log_e(ciper_rsa * n_private)
message_restored = math.log(ciper_rsa * n_private, math.exp)
print("Restored:", message_restored)

"""
###############
TASK 2: 
Verschlusseln Sie die Nachricht x= 9 mit den RSA Parametern p= 5, q= 11, e= 3
Berechnen  Sie  den  zugehorigen  privaten  Schlussel  und  entschlusseln  Sie zur Uberprung die verschlusselte Nachricht
"""