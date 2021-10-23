import random
import simpy
import itertools

TANK_TRUCK_TIME = 3
THRESHOLD = 27
FUEL_TANK_SIZE = 50
RANGE_INT = [50, 500]
SIM_TIME = 30
T_INTER = [30, 50]

thor.santaclara.com.br\52449

def customers_store(name, env, sku_ctner):
    """A car arrives at the gas station for refueling.

    It requests one of the gas station's fuel pumps and tries to get the
    desired amount of gas from it. If the stations reservoir is
    depleted, the car has to wait for the tank truck to arrive.

    """  

    customer_purchase = random.randint(*RANGE_INT)
    yield sku_ctner.get(customer_purchase)


    # The "actual" refueling process takes some time
    yield env.timeout(1)
    print('Day %s. Sales amout: %.1f. Stock level: %d' % (env.now, customer_purchase))


def load_truck(env, sku_ctner):
    """Arrives at the gas station after a certain delay and refuels it."""
    yield env.timeout(TANK_TRUCK_TIME)
    print('Tank truck arriving at time %d' % env.now)
    ammount = sku_ctner.capacity - sku_ctner.level
    print('Tank truck refuelling %.1f liters.' % ammount)
    yield sku_ctner.put(ammount)

def warehouse_control(env, sku_ctner):
    """Periodically check the level of the *sku_ctner* and call the tank
    truck if the level falls below a threshold."""
    while True:
        if sku_ctner.level / sku_ctner.capacity * 100 < THRESHOLD:
            # We need to call the tank truck now!
            print('Calling tank truck at %d' % env.now)
            # Wait for the tank truck to arrive and refuel the station
            yield env.process(load_truck(env, sku_ctner))

        yield env.timeout(15)  # Check every 10 seconds

def car_generator(env, dc_space):
    """Generate new cars that arrive at the gas station."""
    for i in itertools.count():
        yield env.timeout(1)
        env.process(customers_store('Customer %d' % i, env, dc_space))


env = simpy.Environment()
gas_station = simpy.Resource(env, 2)
dc_space = simpy.Container(env, 120000, init=30000)
env.process(warehouse_control(env, dc_space))
env.process(car_generator(env, dc_space))

# Execute!
env.run(until=SIM_TIME)