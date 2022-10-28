

class Clock():
    def __init__(self, time:str) -> None:
        self.hours = None
        self.minutes = None
        self.set_time(time)

    def set_time(self, time:str) -> tuple:
        time = time.split(":")
        self.hours = int(time[0]) % 12
        self.minutes = int(time[1]) % 60

    def angle_hh(self) -> float:
        return (360 / 12) * self.hours + (360 / (12*60)) * self.minutes

    def angle_mm(self) -> float:
        return (360 / 60) * self.minutes

    def angle(self) -> float:
        return abs(self.angle_hh() - self.angle_mm())


time = "12:30"
clock = Clock(time)

print(clock.angle())