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
money = 1000000
# 50 euro per asic, 50 euro per integration
costPerAsic = 50 + 50
n_dev = money/costPerAsic
print("How many units can be operated in parallel with the available budget? : ", n_dev)

keyLength = [40, 56, 64, 80, 112, 128]  # bit

print("How long does average key search time take? :")

for length in keyLength:
    print("------------------------------- \n")
    print("Search time at a key length of " + str(length) + " bit \n")

    maxTries = float(2 ** length)
    avgTries = float(maxTries / 2)

        maxSeconds = maxTries / float(speed_dev)
        avgSeconds = avgTries / float(speed_dev)
        minSeconds = float(1 / float(speed_dev))

    print("Minimum: \n    1 try.")
    print("    " + '{:30f}'.format(minSeconds) + " (a very small fraction of a second) \n")

    print("Average: \n    " + '{:.2f}'.format(avgTries) + " tries")
    print("in  " + '{:.5f}'.format(avgSeconds) + " seconds.")
    print("in  " + '{:.2f}'.format(sec_to_min(avgSeconds)) + " minutes.")
    print("in  " + '{:.2f}'.format(sec_to_hour(avgSeconds)) + " hours.")
    print("in  " + '{:.2f}'.format(sec_to_day(avgSeconds)) + " days.")
    print("in  " + '{:.2f}'.format(sec_to_years(avgSeconds)) + " years.")
    print("in  2^" + '{:.2f}'.format(math.log(sec_to_years(avgSeconds), 2)) + " years.")

    print("Maximum: \n    " + '{:.0f}'.format(maxTries) + " tries")
    print("in  " + '{:.5f}'.format(maxSeconds) + " seconds.")
    print("in  " + '{:.2f}'.format(sec_to_min(maxSeconds)) + " minutes.")
    print("in  " + '{:.2f}'.format(sec_to_hour(maxSeconds)) + " hours.")
    print("in  " + '{:.2f}'.format(sec_to_day(maxSeconds)) + " days.")
    print("in  " + '{:.2f}'.format(sec_to_years(maxSeconds)) + " years.")
    print("in  2^" + '{:.2f}'.format(math.log(sec_to_years(maxSeconds), 2)) + " years.")

    print("------------------------------- \n")
    print("Moore with 1 000 000 000 budget")
    # Das mooresche Gesetz besagt,
    # dass sich die Komplexitaet integrierter Schaltkreise mit minimalen Komponentenkosten
    # regelmaessig verdoppelt;
    # je nach Quelle werden 12 bis 24 Monate als Zeitraum genannt.
    # meistens 18 Monate

    # N(t): power after years
    # N0:   start power
    # t:    years
    # N(t) = N0 * 2^t
    # t= ln(  N(t) / N0  )  /  ln(2)

    # http://www.mathe-paradies.de/mathe/gleichungsloeser/index.htm
    # A = B * 2^X

    futureMoney = 1000000000

    # 1 Mrd / (50 + 50)
    maxAsics = float(futureMoney / costPerAsic)

    keysPerDay = speed_dev * maxAsics * float(60 * 60 * 24)

    # unit: keys per second
    days = avgTries / keysPerDay  # 24h

    print("days=" + str(days))
    print("keysPerDay=" + str(keysPerDay))

    years = 0

    asictmp = speed_dev
    while days > 1:
        years = years + 1.5
        asictmp = asictmp * 2
        keysPerDay = asictmp * maxAsics * float(60 * 60 * 24)
        days = avgTries / keysPerDay

    print("years=" + str(years))

    futureMoney = 1000000000

    # 1 Mrd / (50 + 50)
    futureMaxAsics = float(futureMoney / costPerAsic)

    # unit: keys per second
    requieredKeysPerSecond = maxTries / float(60 * 60 * 24)  # 24h

    # N(t) = N0 * 2^t
    requieredASICs = requieredKeysPerSecond / futureMaxAsics

    # t= ln(  N(t) / N0  )  /  ln(2)
    requieredYears = math.log(requieredASICs / speed_dev) / math.log(2)

    if requieredYears <= 0:
        print("Already exists")
    else:
        print("In " + str(format(requieredYears, '.2f')) +
              " years according to Moore's Law can be built a machine, that can hack a " + str(length) +
              " key in 24 hours.")
    print("##########################################")

print("======================================================================")
print("How expensive is an attack with the complexity 2^64 and 2^80 measured by the current bitcoin mining rate")
"""Hash Rate is the speed at which a compute is completing an operation in the Bitcoin code. """
current_rate = 89 * 10**18  # exahash

complexity = [64, 80]
# formula: time = (sec/60)/60)/24
# time = 1 day ===>
# 1 = (2^64 * current_rate) / (speed_dev * num_dev)
# speed_dev * num_dev = 2^64 * current_rate
# num_dev = (2^64 * current_rate) / speed_dev
for c in complexity:
    comp = (2**64 * current_rate) / speed_dev
    print("Only with one AISC for complexity", c)
    print("in  " + '{:.2f}'.format(sec_to_day(comp)) + " days.")
    print("in  " + '{:.2f}'.format(sec_to_years(comp)) + " years.")
    print("in  2^" + '{:.2f}'.format(math.log(sec_to_years(comp), 2)) + " years.")

    num_asic = (2**64 * current_rate) / speed_dev
    money = num_asic * costPerAsic
    print("To hack within 24 hours for complexity", c)
    print("amount of ASICs: 2^ {:.2f}".format(math.log(sec_to_years(num_asic), 2)))
    print("Money: {:.2f} €".format((sec_to_years(money))))
    print("Money: 2^{:.2f} €".format(math.log(sec_to_years(money), 2)))


"""
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

"""