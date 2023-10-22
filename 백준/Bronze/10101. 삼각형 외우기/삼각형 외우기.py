tri= []
for i in range(3):
    tri.append(input())
sum_tri = sum(list(map(int,tri)))
if len(set(tri)) == 1 and sum_tri == 180:
    a = "Equilateral"
elif len(set(tri)) == 2 and sum_tri == 180:
    a = "Isosceles"
elif len(set(tri)) == 3 and sum_tri == 180:
    a = "Scalene"
else:
    a = "Error"
print(a)