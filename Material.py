class Material:
    def __init__(self, id, name, amount=0, trst=0, backorder=0):
        self.id = id
        self.name = name
        self.item_inventory = amount
        self.item_transit = trst
        self.item_backorder = backorder
    
    def getId(self):
        return self.id

    def getName(self):
        return self.name
    
    def returnAmount(self):
        return self.item_inventory
    
    def pullAmount(self, amount):
        if amount >= 0:
            self.item_inventory += amount
    
    def getAmount(self, amount):
        if amount >= 0:
            self.item_inventory -= amount
    
    def pullAmountTrst(self, trst):
        if trst >= 0:
            self.item_transit += trst
    
    def getAmountTrst(self, trst):
        if trst >= 0:
            self.item_transit -= trst
    
    def pullAmountBackorder(self, backorder):
        if backorder >= 0:
            self.item_backorder += backorder
    
    def getAmountBackorder(self, backorder):
        if backorder >= 0:
            self.item_backorder -= backorder