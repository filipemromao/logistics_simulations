class Truck:
    def __init__(self, env,truck_id, item_id, load_capacity, transit_time):
        self.env = env
        self.id = truck_id
        self.item_id = item_id
        self.load_capacity = load_capacity
        self.transit_time = transit_time
