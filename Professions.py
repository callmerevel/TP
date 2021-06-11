from random import choice

class Profession (object):
  def __init__(self, name = "Name_profession", salary = 0, savings = 0, liabilities = [], monthExpenses = []):
    "Initialisation of a profession"
    self.mName = name
    self.mSalary = salary
    self.mSavings = savings
    self.mLiabilities = liabilities     # Représente toutes les dettes du Joueur
    self.mMonthExpenses = monthExpenses     # Représente les dettes du joueur reparties par mois

  def get_name(self):
    return self.mName

  def get_salary(self):
    return self.mSalary

  def get_savings(self):
    return self.mSavings
    
  def set_liability(self, tupl = ("Name of liability", 0)):
    self.mLiabilities.append(tupl)
    
  def get_liabilities(self):
    return self.mLiabilities

  def set_monthExpenses(self, tupl = ("Name of expense", 0)):
    self.mMonthExpenses.append(tupl)

  def get_monthExpenses(self):
    return self.mMonthExpenses

  def get_sum_monthExpenses(self):
    summ = 0
    monthExpenses = self.get_monthExpenses()
    for tupl in monthExpenses:
      summ = summ + tupl[1]
    return summ

#=================================================================================================================
#1
name1, salary1, savings1 = "Programmer", 350000, 25000
liabilities1 = [
  ("Home Mortgage", 1500000),
  ("Car Loans", 1000000),
  ("Credit Card", 400000)
]
monthExpenses1 = [
  ("Taxes", 30000),
  ("Home Mortgage Payment", 25000),
  ("Car Loans Payment", 20000),
  ("Credit Card Payment", 10000),
  ("Other Expenses", 80000),
  ("Child(s) Expenses", 0)
]
profession1 = Profession(name1, salary1, savings1, liabilities1, monthExpenses1)

#2 (A compléter en suivant la démarche précédente)



# Ajouter chaque profession créée dans la liste 
list_of_Profession = [profession1]

# Ne pas toucher !!!!!!!
def provide_profession():
  "Fonction that returns a profession"
  return choice(list_of_Profession)