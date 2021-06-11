import Professions

class Big_Opportunity(object):
  def __init__(self, description = "Description", cost = 0, cashFlow = 0):
    "Initialisation of a big opportunity"
    self.mDescription = description
    self.mCost = cost
    self.mCashFlow = cashFlow

  def display(self):
    "Display the opportunity to the player"
    print("BIG DEALS")
    print(self.mDescription)
    print("Cost : {} Fcfa".format(self.mCost))
    print("Cash Flow : {} Fcfa".format(self.mCashFlow))
    print("Can be sell #entre {} or more".format(self.mCost))


class Small_Opportunity(object):
  def __init__(self, description = "Description", cost = 0, cashFlow = 0):
    "Initialisation of a small opportunity"
    self.mDescription = description
    self.mCost = cost
    self.mCashFlow = cashFlow

  def display(self):
    "Display the opportunity to the player"
    print("SMALL DEALS")
    print(self.mDescription)
    print("Cost : {} Fcfa".format(self.mCost))
    print("Cash Flow : {} Fcfa".format(self.mCashFlow))
    print("Can be resell between {} or more".format(self.mCost))


class Doodads(object):
  def __init__(self, description = "Description", toPay = 0):
    "Initialisation of a doodad"
    self.mDescription = description
    self.mToPay = toPay

  def display(self):
    "Display the doodads to the player"
    print("DOODADS")
    print(self.mDescription)
    print("To pay : {} Fcfa".format(self.mToPay))


class Market(object):
  def __init__(self, description = "Description", gain = 0):
    "Initialisation of a market"
    self.mDescription = description
    self.mGain = gain

  def display(self):
    "Display the market to the player"
    print("MARKET")
    print(self.mDescription)
    print("Gain : {} Fcfa".format(self.mGain))
    

class Profession(object):
  def __init__(self, name = "Name_profession", salary = 0, savings = 0, monthExpenses = []):
    "Initialisation of a profession"
    self.mName = name
    self.mSalary = salary
    self.mSavings = savings
    self.mMonthExpenses = monthExpenses

  def get_Name(self):
    return self.mName

  def get_Salary(self):
    return self.mSalary

  def get_Savings(self):
    return self.mSavings
  
  def set_MonthExpenses(self, tupl = (name = "Name of expense", sumExpense = 0)):
    self.mMonthExpenses.append(tupl)

  def get_MonthExpenses(self):
    return self.mMonthExpenses

  def get_Sum_MonthExpenses(self):
    summ = 0
    for tupl in self.mMonthExpenses:
      summ = summ + tupl[1]
    return summ
    

class Player(object):
  def __init__(self):
    "Representation of a player in the game"
    self.mPseudo = "Pseudo of the player"
    self.mProfession = provide_profession() # Récupère une profession dans une liste de profession et l'attribu au joueur
    self.mSalary = self.mProfession.get_Salary()
    self.mCashFlow = 0
    self.mDepenses = self.mProfession.get_Sum_MonthExpenses()  # Représente la somme totale des dépenses mensuelles
    self.mCash = self.mSalary + self.mCashFlow - self.mDepenses + self.mProfession.get_Savings()
    self.mChildNumber = 0
    self.mMonthExpensesList = self.mProfession.get_MonthExpenses()
    self.mInvestmentList = [] # Has the player's investments
    self.mPropertyList = [] # Has the player's property

