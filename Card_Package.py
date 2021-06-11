class Card (object):
    def __init__(self, name = "Name", description = "Description"):
        "Abstract class of a card initialization"
        self.mName = name
        self.mDescription = description

class Opportunity (Card):
    def __init__(self, name, description, cost = 0, cashFlow = 0):
        "Initialization of an opportunity"
        Card.__init__(self, name, description)
        self.mCost = cost
        self.mCashFlow = cashFlow


class Doodads (Card):
    def __init__(self, description = "Description", toPay = 0):
        "Initialisation of a doodad"
        Card.__init__(self, description)
        self.mToPay = toPay

    def display(self):
        "Display the doodads to the player"
        print("DOODADS")
        print(self.mDescription)
        print("To pay : {} Fcfa".format(self.mToPay))
    
    def get_toPay(self):
        return self.mToPay


class Market (Card):
    def __init__(self, name, description, opportunityTarget, gain = 0):
        "Initialization of a market"
        Card.__init__(self, name, description)
        self.mGain = gain
        self.mOpportunityTarget = opportunityTarget

    def display(self):
        "Display the market to the player"
        print("MARKET : {}".format(self.mName))
        print(self.mDescription)
        print("Investment/Fund target : {}".format(self.get_opportunityTarget()))
        print("Gain : {} Fcfa".format(self.get_gain()))

    def get_gain(self):
        return self.mGain

    def get_opportunityTarget(self):
        return self.mOpportunityTarget.get_name()


#=======================================================================================================#
description1, topay1 = "perte d'un pari sportif" , 500
doodad1 = Doodads(description1, topay1)

description2, topay2 = " relloocker la maison", 200
doodad2 = Doodads(description = description2, toPay = topay2)

description3, topay3 = "refaire garde robe", 100
doodad3 = Doodads(description = description3, toPay = topay3)

description4, topay4 = "depense inutile", 2000
doodad4 = Doodads(description = description4, toPay = topay4)  

description5, topay5 = "agression", 700
doodad5 = Doodads(description = description5, toPay = topay5)

description6, topay6 = "deux semaines de maladie", 7000
doodad6 = Doodads(description = description6, toPay = topay6)

description7, topay7 = " accident de circulation", 400
doodad7 = Doodads(description = description7, toPay = topay7)

description8, topay8 = "cambriolage perte de bijoux de valeur", 800
doodad8 = Doodads(description = description8, toPay = topay8)

description9, topay9 = "organisation de la fete d'aniversaire", 250
doodad9 = Doodads(description = description9, toPay = topay9)
#-----------------------------------------------------------------------------------------
