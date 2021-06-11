from Card_Package import Opportunity

class Small_Deals (Opportunity):
    def __init__(self, name, description, cost, cashFlow, trading_interval = (0,1), shares_owned = 0, payDown = 0):
        "Initialization of a small deal"
        Opportunity.__init__(self, name, description, cost, cashFlow)
        self.mTradingInterval = trading_interval
        self.mSharesOwned = shares_owned
        self.mPayDown = payDown

    def display(self):
        "Display of a small deal to a player"
        print("SMALL DEALS : {}".format(self.get_name()))
        print(self.mDescription)
        print("Cost : {} Fcfa".format(self.get_cost()))
        print("Cash Flow : {} Fcfa".format(self.get_cashFlow()))
        if(self.get_payDown() == 0):
            print("Trading range : {} Fcfa to {} Fcfa".format(self.mTradingInterval[0], self.mTradingInterval[1]))
            print("Shares owned : {}\n".format(self.get_shares()))
        else:
            print("Pay Down : {} Fcfa".format(self.get_payDown()))

    def get_name(self):
        return self.mName

    def get_cost(self):
        return self.mCost

    def get_cashFlow(self):
        return self.mCashFlow
    
    def set_shares(self, numberShares):
        self.mSharesOwned = numberShares
    
    def get_shares(self):
        return self.mSharesOwned

    def get_payDown(self):
        return self.mPayDown


class Big_Deals (Opportunity):
    def __init__(self, name, description, cost, cashFlow, payDown = 0):
        "Initialization of a big deal"
        Opportunity.__init__(self, name, description, cost, cashFlow)
        self.mPayDown = payDown

    def display(self):
        "Display of a big deal to a player"
        print("BIG DEALS : {}".format(self.get_name()))
        print(self.mDescription)
        print("Cost : {} Fcfa".format(self.get_cost()))
        print("Cash Flow : {} Fcfa".format(self.get_cashFlow()))
        print("Pay Down : {} Fcfa\n".format(self.get_payDown()))

    def get_name(self):
        return self.mName

    def get_cost(self):
        return self.mCost

    def get_cashFlow(self):
        return self.mCashFlow

    def get_payDown(self):
        return self.mPayDown

#========================================================================================================#
# SMALL DEALS

# Small_Deals (nom_opportunité, description_opportunité, prix_achat, cashflow, intervalle_trading)








# BIG DEALS

# Big_Deals (nom_opportunité, description_opportunité, prix_achat)

name1 = "honstructionParthner", 
description1 = "looking for a partner to build a wing of the hospital", 
cost1 = 1250000,
cashFlow1 = 50000, 
payDown1 = 1250000,

Big_Deals1 = Big_Deals(name1, description1, cost1, cashFlow1, payDown1)
List_Of_Big_Deals = [Big_Deals1]

name2 = "houseForSale",
description2 = "transferred skilled tradesman "+
                "kept this  house in excellent condition, so " +
                "it commands top XAF rentals in older neighborhood",
cost2 = 3350000,
cashFlow2 = 20000,
payDown2 = 600000,

name3 = "carRepaire",
description3 = "Purchase of a modern car garage with a good reputation",
cost3 = 10000000,
cashFlow3 = 135000,
payDown3 = 2000000,

name4 = "intercityTransportInvestment",
description4 = "An urban transport agency needs an investor to develop its activities in more cities",
cost4 = 11000000,
cashFlow4 = 85000,
payDown4 = 2000000,

name5 = "farmInvestment",
description5 = "Production of beef, pork and chicken",
cost5 = 8000000,
cashFlow5 = 50000,
payDown5 = 1500000,

name6 = "telecomBusiness",
description6 = "buy and resell mobile phone services under license from National Telecom",
cost6 = 22000000,
cashFlow6 = 500000,
payDown6 = 8000000,


name7 = "agriculturalProduction",
description7 = "Production and export of corn and wheat",
cost7 = 90000000,
cashFlow7 = 1500000,
payDown7 = 50000000,

name8 = "",
description8 = "",
cost8 = ,
cashFlow8 = ,
payDown8 = ,

name9 = "",
description9 ="",
cost9 = ,
cashFlow9 = ,
payDown9 = ,

big_Deals9 = Big_Deals(name9, description9, cost9, cashFlow9, payDown9)
list_Of_Big_Deals = [big_Deals1, big_Deals2, big_Deals3, big_Deals4, big_Deals5, big_Deals6, big_Deals7, big_Deals8, big_Deals9]