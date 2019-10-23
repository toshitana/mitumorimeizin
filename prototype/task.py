
class work():
    def __init__(self):
        self.point = None
        self.real_time = None
        self.virtual_time = None

    def set_point(self, point):
        self.point = point
        return True

    def set_real_time(self, real_time):
        self.real_time = real_time
        return True

    def set_virtual_time(self, virtual_time):
        self.virtual_time = virtual_time
        return True

    def caliculate_point_per_time(self):
        return self.real_time/self.point

    def differnt_realtime_from_virtual_time(self):
        return abs(self.real_time - self.virtual_time)