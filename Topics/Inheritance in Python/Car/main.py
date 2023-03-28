class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color


class Tesla(Car):
    pass


tesla_car = Tesla('SpaceX', 'Black')
