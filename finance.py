goal_salary = YOUR GOAL SALARY
gross = GROSS SALARY
starting = CURRENT INVESTMENTS
saving_percent = .25
tax= .35
_401k = 0.03

savings_req = goal_salary / 0.04

def calc_bal(income, balance):
    balance += income
    balance *= 1.08
    return balance

inc = saving_percent * (1-tax) * gross + (_401k*2 * (1-tax) * gross)

bal = starting
years = 0
print("Assuming 7.5% average salary increase per year")

inc = saving_percent * (1-tax) * gross + (_401k*2 * (1-tax) * gross)
years = 0
bal = starting
while bal < savings_req:
    bal = calc_bal(inc, bal)
    inc *= 1.075
    years += 1
    print("Year: ", years, "balance:", '${:,.2f}'.format(bal))
print("Investing "+ str(100*saving_percent)+"% at the annual S&P return rate of 8%, yields ", '${:,.2f}'.format(bal), " at", years + 23, "years old")
