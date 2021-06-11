from Professions import *
from random import randint
from Opportunity_Package import *

class Player (object):
    def __init__(self, pseudo = "Pseudo du joueur"):
        "Initialization of a player interface game"
        self.mPseudo = pseudo
        self.mProfession = provide_profession()
        self.mSalary = self.mProfession.get_salary()
        self.mCashFlow = 0
        self.mCash = self.mSalary - self.mProfession.get_sum_monthExpenses() + self.mProfession.get_savings()
        self.mChildNumber = 0
        self.mInvestmentList = [] # Liste des grandes opportunités
        self.mFundsList = [] # Liste des petites opportunités

    def status(self):
        print("===== PLAYER STATUS =====")
        print("Pseudo/Name : {}".format(self.mPseudo))
        print("Profession : {}".format(self.mProfession.get_name()))
        print("Salary : {} Fcfa".format(self.mSalary))
        print("CashFlow : {} Fcfa".format(self.get_cashFlow()))
        print("Number of child : {}".format(self.mChildNumber))
        print("Total Expenses : {} Fcfa".format(self.mProfession.get_sum_monthExpenses()))
        print("Cash : {} Fcfa\n".format(self.mCash))
        print("MONTH EXPENSES LIST")
        print("-------------------")
        for tupl in self.mProfession.get_monthExpenses() :
            print("- {} : {} Fcfa".format(tupl[0], tupl[1]))
        print("\nLIABILITIES")
        print("-----------")
        for tupl in self.mProfession.get_liabilities() :
            print("- {} : {} Fcfa".format(tupl[0], tupl[1]))
        print("")

    def roll_dice(self):
        print(".\n..\n...\n{} roll {}\n".format(self.mPseudo, randint(1,6)))
    
    def roll_2dice(self):
        print(".\n..\n...\n{} roll {}\n".format(self.mPseudo, randint(2,12)))
    
    def get_cashFlow(self):
        return self.mCashFlow

    def has_a_baby(self):
        if(self.mChildNumber >= 3):
            print("You alreary have 3 child, can't give you more MONSTER !!!")
        else:
            self.mChildNumber += 1
            for tupl in self.mProfession.get_monthExpenses() :
                if(tupl[0] == "Child(s) Expenses"):
                    self.mProfession.get_monthExpenses().remove(tupl)
                    break
            num = self.mChildNumber * int(self.mSalary*0.1)  # Le budget d'un enfant vaut 10% du salaire
            self.mProfession.set_monthExpenses(("Child(s) Expenses", num))
                    
    def buy_investment(self, opportunity):
        "Function for buying an investment"
        self.mInvestmentList.append(opportunity)
        self.mCashFlow += opportunity.get_cashFlow()
        self.mProfession.set_liability((opportunity.get_name(), opportunity.get_cost()-opportunity.get_payDown()))
        self.mCash -= opportunity.get_payDown()

    def buy_funds(self, opportunity):
        "Function for buying a funds"
        self.mFundsList.append(opportunity)
        self.mCashFlow += opportunity.get_cashFlow()
        self.mCash -= opportunity.get_shares()*opportunity.get_cost()

    def sell_investment(self, opportunity):
        "Function for selling an investment"
        self.mInvestmentList.remove(opportunity)
        self.mCashFlow -= opportunity.get_cashFlow()
        for tupl in self.mProfession.get_liabilities():
            if(tupl[0] == opportunity.get_name()):
                self.mProfession.get_liabilities().remove(tupl)
                break
        self.mCash += opportunity.get_payDown()  # A revoir
    
    def sell_funds(self, opportunity):
        "Function for selling a fund"
        self.mFundsList.remove(opportunity)
        self.mCashFlow -= opportunity.get_cashFlow()
        self.mCash += opportunity.get_shares()*opportunity.get_cost()

    def borrow(self, summ = 0):
        "Function used when the player borrow at the Bank"
        # Cas où il y'a un prêt déjà en cours
        for tupl in self.mProfession.get_liabilities():
            if(tupl[0] == "Loans"):
                x = True
                val = tupl[1]+summ
                self.mProfession.get_liabilities().remove(tupl)
                self.mProfession.get_liabilities().append((tupl[0], val))
                for tupl2 in self.mProfession.get_monthExpenses():
                    if(tupl2[0] == "Loans Payment"):
                        self.mProfession.get_monthExpenses().remove(tupl2)
                        self.mProfession.get_monthExpenses().append((tupl2[0], int(val*0.1)))
                        break
                break
            else:
                x = False
        # Cas où il n'y a pas de prêt en cours
        if(x == False):
            self.mProfession.get_liabilities().append(("Loans", summ))
            self.mProfession.get_monthExpenses().append(("Loans Payment", int(summ*0.1)))

    def pay_debt(self):
        "Function called when the player want to pay their debt at the Bank"
        i, x = 1, 0
        print("REPAY")
        for tupl in self.mProfession.get_liabilities():
            print("{} - {} : {} Fcfa".format(i, tupl[0], tupl[1]))
            i += 1
        while(x != 1):
            debt = input("\nWhat debt do you want to repay ? : ")
            try:
                debt = int(debt)
                if(debt > 0 or debt <= len(self.mProfession.get_liabilities())):
                    x = 1
                else:
                    print("Enter a valid choice.")
                    x = 0
            except:
                print("Refund cancelled !\n")
                break
            if(x == 1):
                for j in range(1,i+1):
                    if(debt == j):
                        val = self.mProfession.get_liabilities()[debt-1] # Sauvegarde du tuple avant suppression de la liste
                        if(self.mCash < val[1]):
                            print("Unable to pay this debt.\n")
                        else:
                            del self.mProfession.get_liabilities()[debt-1]
                            for tupl in self.mProfession.get_monthExpenses():
                                if(tupl[0] == val[0]+" Payment"):
                                    self.mProfession.get_monthExpenses().remove(tupl)
                                    break
                            print("Debt paid !\n")
                        break

            
#class Party (object):



#===== Main test =======#

player = Player("Edghi")
player.status()
player.pay_debt()
player.status()