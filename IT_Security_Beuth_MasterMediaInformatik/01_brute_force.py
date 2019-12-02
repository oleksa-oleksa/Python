import math
"""
ASIC 2^44 keys pro second
cost: 50€ (buy) + 50€(maintain)
budget: 1 million euro
"""


def sec_to_min(sec):
    return sec/60


def sec_to_hour(sec):
    return (sec/60)/60


def sec_to_day(sec):
    return ((sec/60)/60)/24


def sec_to_years(sec):
    return (((sec/60)/60)/24)/365

speed_dev = 2**44
n_dev = 1000000/100

bit_40 = 2**40 / speed_dev
print("40 bit time in seconds: ", bit_40)

bit_56 = 2**56 / speed_dev
print("56 bit time in seconds: {:.2f}, minutes: {:.2f}, hours: {:.2f}".format(bit_56, sec_to_min(bit_56), sec_to_hour(bit_56)))

bit_64 = 2**64 / speed_dev
print("64 bit time in seconds: {:.2f}, minutes: {:.2f}, hours: {:.2f}".format(bit_64, sec_to_min(bit_64), sec_to_hour(bit_64)))

bit_80 = 2**80 / speed_dev
print("80 bit time in seconds: {:.2f}, minutes: {:.2f}, hours: {:.2f}, days: {:.2f}, years: {:.2f}".format(bit_80,
      sec_to_min(bit_80), sec_to_hour(bit_80), sec_to_day(bit_80), sec_to_years(bit_80)))

bit_112 = 2**112 / speed_dev
print("112 bit time in seconds: {:.2f}, minutes: {:.2f}, hours: {:.2f}, days: {:.2f}, years: {:.2f}".format(bit_112,
      sec_to_min(bit_112), sec_to_hour(bit_112), sec_to_day(bit_112), sec_to_years(bit_112)))
print("112 bit needs 2^{:.2f} years".format(math.log(sec_to_years(bit_112), 2)))

bit_128 = 2**128 / speed_dev
print("128 bit time in seconds: {:.2f}, minutes: {:.2f}, hours: {:.2f}, days: {:.2f}, years: {:.2f}".format(bit_128,
      sec_to_min(bit_128), sec_to_hour(bit_128), sec_to_day(bit_128), sec_to_years(bit_128)))
print("128 bit needs 2^{:.2f} years".format(math.log(sec_to_years(bit_128), 2)))
