
l = int(input())
n = int(input())
plate = {}
for i in range(n):
    r = input().split()
    if r[0] not in plate:
        plate[r[0]] = {}
    plate[r[0]][int(r[1])] = int(r[2])

ticket = []
for car in plate:
    x0, t0 = -1, 0
    for camera in sorted(plate[car].keys()) :
        if x0 < 0:
            x0, t0 = camera, plate[car][camera]
        else:
            x1, t1 = camera, plate[car][camera]
            dx, dt = x1 - x0, t1 - t0
            if dx * 3600 > dt * l:
                ticket.append(car + " " + str(camera))
            x0, t0 = x1, t1

if len(ticket) == 0:
    print("OK")
else:
    for incident in ticket:
        print(incident)
