from colorama import Fore, Style
curAmount = 30000
additionalAmount = 10000
amountDeposited = 10000
numYears = 41
amountDepositedInflationAdjusted = 10000
print("""Assuming you invest 10k/year (annual contribution going up 6% per year which is 3.22% average annual inflation + a bit more to cover your career promotions) and your total investment going up 7%/year to match stock market""")
print(f"Contribution adjusted for inflation at age 19: {Fore.GREEN}${10000:,}{Style.RESET_ALL}. Total savings adjusted for inflation: {Fore.GREEN}$30,000{Style.RESET_ALL}")

for period in range(numYears):
    curAmount                        += additionalAmount
    curAmount                        *= 1.07
    amountDeposited                  += additionalAmount
    additionalAmount                 *= 1.06
    amountDepositedInflationAdjusted += additionalAmount / (1.032)**period
    if period % 3 == 0: print(f"Contribution adjusted for inflation at age {period+20}: {Fore.GREEN}${int(additionalAmount / (1.032)**period):,}{Style.RESET_ALL}. Total savings adjusted for inflation: {Fore.GREEN}${int(curAmount / (1.032)**period):,}{Style.RESET_ALL}.")# Assuming we are saving 20% of pre-tax pay we are making {Fore.GREEN}${int(additionalAmount / (1.032)**period)*5:,}{Style.RESET_ALL}")

PV = curAmount / (1.032)**numYears
print("")
print(f"                                    Amount deposited: {Fore.GREEN}${amountDeposited:,.2f}{Style.RESET_ALL}")
print(f"                              Balance after {numYears-1} years: {Fore.GREEN}${curAmount:,.2f}{Style.RESET_ALL}")
print(f"     Purchasing power deposited (inflation adjusted): {Fore.GREEN}${amountDepositedInflationAdjusted:,.2f}{Style.RESET_ALL}")
print(f"Purchasing power after {numYears-1} years (inflation adjusted): {Fore.GREEN}${PV:,.2f}{Style.RESET_ALL}")
print(f"   Annual pension (4% of total) (inflation adjusted): {Fore.GREEN}${PV*0.04:,.2f}{Style.RESET_ALL}")
