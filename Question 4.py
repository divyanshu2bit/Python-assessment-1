# traffic system records speed of vehicles every 12 hours
# program reads 12 speed values and calculates the average speed

speed_list = [0] * 12

for i in range(12):
    speed_list[i] = float(input("Enter speed: "))

total = 0
for i in range(12):
    total += speed_list[i]

avg = total / 12
print("Average speed =", avg)

if avg < 40:
    print("Slow traffic")
elif avg >= 40 and avg <= 80:
    print("Moderate traffic")
else:
    print("Fast traffic")
