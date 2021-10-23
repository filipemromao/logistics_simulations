class Distribuition_Center:
    def __init__(self, cd_id, lst_mat, wrhse_cap, reception_cap):
        self.dict_mat = self.__createItemDict(lst_mat)
        self.wrse_cap = wrhse_cap
        self.reception_cap = reception_cap
        self.id = cd_id

    def __createItemDict(self, lst_obj_mat):
        material_dict = {item.id: item for item in lst_obj_mat}
        return material_dict

    def getTotalInventory(self):
        item_values = [item.returnAmount() for item in self.dict_mat.values()]
        wrhseTotalInventory = sum(item_values)
        return wrhseTotalInventory
    
    def returnItemInventory(self, id_item):
        return self.dict_mat[id_item].returnAmount()
    
    def pullItemInventory(self, id_item, item_amount):
        if self.dict_mat.get(id_item):
            self.dict_mat[id_item].pullAmount(item_amount)
        else:
            return 'item {} not found'.format(id_item)
    
    def getItemInventory(self, id_item, item_amount):
        if self.dict_mat.get(id_item):
            self.dict_mat[id_item].getAmount(item_amount)
        else:
            return 'item {} not found'.format(id_item)