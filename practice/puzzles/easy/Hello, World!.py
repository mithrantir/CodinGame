import sys
import math


def from_geo_to_radians(lat, lon):
    lat_deg = float(lat[1:3]) + float(lat[3:5])/60 + float(lat[5:])/3600
    lat_r = lat_deg * math.pi/180
    if lat[0] == 'S': lat_r *= -1
    lon_deg = float(lon[1:4]) + float(lon[4:6])/60 + float(lon[6:])/3600
    lon_r = lon_deg * math.pi/180
    if lon[0] == 'W': lon_r *= -1
    return [lat_r, lon_r]


def distance(loc1, loc2):
    dphi = (loc1[0] -  loc2[0])/2
    dlambda = (loc1[1] -  loc2[1])/2
    a = math.sin(dphi)**2
    a += math.cos(loc1[0]) * math.cos(loc2[0]) * math.sin(dlambda)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    dist = int(math.floor(6371 * c + 0.5))
    return dist


n = int(input())  # number of capitals
m = int(input())  # number of geolocations for which to find the closest capital

positionOf, capitalOf, messageOf = {}, [], {}
for i in range(n):
    cd = input().split()
    capitalOf.append(cd[0])
    positionOf[cd[0]] = from_geo_to_radians(cd[1], cd[2])
for i in range(n):
    messageOf[capitalOf[i]] = input()
for i in range(m):
    geoloc = input().split()
    location = from_geo_to_radians(geoloc[0], geoloc[1])
    near_capitals, min_dist = [], 45000
    for j in range(n):
        d = distance(location, positionOf[capitalOf[j]])
        if d == min_dist:
            near_capitals.append(capitalOf[j])
        elif d < min_dist:
            near_capitals = [capitalOf[j]]
            min_dist = d

    nclose, ans = len(near_capitals), ""
    for i in range(nclose-1):
        ans += messageOf[near_capitals[i]] + " "
    ans += messageOf[near_capitals[nclose-1]]
    print(ans)
