from task import work

a = work()

a.set_point(10)
a.set_real_time(10)
a.set_virtual_time(10)
print(10)
b = a.point
print(a.caliculate_point_per_time())
print(a.differnt_realtime_from_virtual_time())