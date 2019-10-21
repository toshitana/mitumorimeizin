a = input()
print(a)
point = int(input('ポイント'))
real_time = int(input('実稼働時間'))
virtual_time = int(input('想定時間'))
point_per_minutes = point / real_time
point_per_minutes = round(point_per_minutes, 2)
print('ポイント当たりの時間は'+ str(point_per_minutes) + 'hです')
print('実時間との差は'+ str(abs(real_time - virtual_time)) + 'hです')

#くそみたいなコードだが、ここから