class Lightbulb:
    def __init__(self):
        self.state = "off"

    def change_state(self):
        # self.state = "on"
        if self.state == "off":
            self.state = "on"
            print(f"Turning the light {self.state}")
        elif self.state == "on":
            self.state = "off"
            print(f"Turning the light {self.state}")
