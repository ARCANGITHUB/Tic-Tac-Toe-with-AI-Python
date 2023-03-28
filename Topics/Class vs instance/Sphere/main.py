class Sphere:
    pi_number = 3.1415

    def __init__(self, r):
        self.r = r
        self.volume = (4/3) * Sphere.pi_number * (self.r ** 3)
        # print(self.volume)


# Sphere(1)
