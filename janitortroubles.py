s1, s2, s3, s4 = map(int, input().split())
s = (s1 + s2 + s3 + s4) / 2
area = ((s - s1) * (s - s2) * (s - s3) * (s - s4))**(1/2)

print(area)

