class Vehicles:
    def __init__(self,engine):
        print("Inside vehicles constructor")
        self.engine=engine
class Car(Vehicles):
    def __init__(self,engine,max_speed):
        super().__init__(engine)
        print("Inside car constructor")
        self.max_speed=max_speed
class Electric_Car(Car):
    def __init__(self,engine,max_speed,km_range):
        super().__init__(engine,max_speed)
        print("Inside Elctric Car constructor")
        self.km_range=km_range
ev=Electric_Car("1500cc",240,750)
print(f"Engine={ev.engine} max speed={ev.max_speed} range={ev.km_range}")
