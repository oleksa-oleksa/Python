"""
Example: Specific cancer that occurs to 1% of population P(c) = 0.01
Test for this cancer with a 90% chance is positive if you have this cancer (this is sensitivity of the test)
But the test is sometimes is positive even if you don't have a cancer C.
Let's say with another 90% chance is negative if you don't have cancer C (this is specificity of the test)

Question: the prior probability of cancer is 1%, and a sensitivity and specificity are 90%,
what's the probability that someone with a positive cancer test actually has the disease?


Bayes theorem states the following:

Posterior = Prior * Likelihood

This can also be stated as P (A | B) = (P (B | A) * P(A)) / P(B) , where P(A|B) is the probability of A given B, also called posterior.

Prior: Probability distribution representing knowledge or uncertainty of a data object prior or before observing it

Posterior: Conditional probability distribution representing what parameters are likely after observing the data object

Likelihood: The probability of falling under a specific category or class.

Prior MULT Test Evidence ==> Posterior
"""

# Prior
P_c = 0.01
P_nonC_pos = 1 - P_c
print("P_nonC_pos = ", P_nonC_pos)
# Test sensitivity
P_pos_cancer = 0.9

# Posterior cancer
P_c_pos = P_c * P_pos_cancer
# Posterior NON cancer
P_nonC_pos
