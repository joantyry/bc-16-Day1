
class Car(object):
    def __init__(self, car_name='General', car_model='GM',
                 car_type='saloon', doors = 4 ,wheels = 4 ):
        self.car_name = car_name
        self.car_model = car_model
        self.doors = doors
        self.car_type = car_type
        self.wheels = wheels
        self.speed = 0

    @property
    def name(self):
        return self.car_name

    @property
    def model(self):
        return self.car_model

    @property
    def num_of_doors(self):
        if self.car_name in ['Koenigsegg', 'Porshe']:
            self.doors = 2
           
        return self.doors

    @property
    def num_of_wheels(self):
        if self.car_type == 'trailer':
            self.wheels = 8
            
        return self.wheels

    def is_saloon(self):
        if self.car_type == 'saloon':
            return True
        return False

    @property
    def num_of_wheels(self):
        if self.car_type == 'trailer':
            self.wheels = 8
            
        return self.wheels

    @property
    def type(self):
        return self.car_type

    def drive(self,  drive_number):
        if self.car_type == 'trailer':
            if drive_number in range(1, 8):
                self.speed = 11 * drive_number
                
            return self
        else:
            if drive_number in range(1, 4):
                self.speed = 997 + drive_number
                
            return self

def main():
    man = Car('MAN', 'Truck', 'trailer')
    moving_man = man.drive(7)
    moving_man_instance = isinstance(moving_man, Car)
    moving_man_type = type(moving_man) is Car
    print(moving_man_instance, moving_man_type, moving_man.speed, man.speed)

    man = Car('Mercedes', 'SLR500')
    parked_speed = man.speed
    moving_speed = man.drive(3).speed

    print(parked_speed, moving_speed)

    honda = Car('Honda')
    print(type(honda) is Car)

    man = Car('MAN', 'Truck', 'trailer')
    koenigsegg = Car('Koenigsegg', 'Agera R')
    print(man.num_of_wheels, koenigsegg.num_of_wheels)

    opel = Car('Opel', 'Omega 3')
    porshe = Car('Porshe', '911 Turbo')
    print(opel.num_of_doors,porshe.num_of_doors,Car('Koenigsegg', 'Agera R').num_of_doors)

    toyota = Car('Toyota', 'Corolla')
    print(toyota.name, toyota.model)    