class Car(object):
    num_of_doors = 4

    def __init__(self, name='General', model='GM', car_type='saloon', speed=0):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.speed = speed
        self.num_of_wheels = 4

        if name == "Porshe" or name == "Koenigsegg":
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
        if self.car_type == "trailer":
            self.num_of_wheels = 8
        self.speed = 0

    def is_saloon(self):
        """Checks if the type of car is saloon or trailer"""
        if self.car_type is not 'trailer':
            return True

        return False

    def drive(self, speed):
        """Check the type of car and returns its speed
        :param speed:
        """
        if self.car_type is 'trailer':
            self.speed = 77
        else:
            self.speed = 10 ** speed
        return self