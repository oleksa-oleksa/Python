"""Swedish Fish Incorporated is the largest Swedish company delivering fish by mail order.
They are now trying to get into the lucrative Danish market by selling one year Salmon subscriptions.
The marketing department have done a pilot study and tried the following marketing method:

A: Sending a mail with a colorful brochure that invites people to sign up for a one year salmon subscription.

The marketing department sent out 16 mails of type A.
Six Danes that received a mail signed up for one year of salmon
and marketing now wants to know, how good is method A?"""

# Import libraries
import pandas as pd
import numpy as np

# Number of random draws from the prior
n_draws = 10000

# Here you sample n_draws draws from the prior into a pandas Series (to have convenient
# methods available for histograms and descriptive statistics, e.g. median)
prior = pd.Series(...)
print(prior)
prior.hist()
