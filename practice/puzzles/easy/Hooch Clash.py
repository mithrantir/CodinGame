import sys
import math

orb_size_min, orb_size_max = [int(i) for i in input().split()]
glow1, glow2 = [int(i) for i in input().split()]

king_vol = glow1**3 + glow2**3
spark1, spark2, spark_dif = glow1, glow2, glow2-glow1

for orb1 in range(orb_size_min, orb_size_max):
    for orb2 in range(orb1, orb_size_max):
        volume = orb1**3 + orb2**3
        if volume == king_vol:
            if spark1 == glow1 or orb2 - orb1 > spark_dif:
                spark1, spark2, spark_dif = orb1, orb2, orb2-orb1
                break
        elif volume > king_vol:
            break

if spark1 == glow1:
    print('VALID')
else:
    print('{} {}'.format(spark1, spark2))
