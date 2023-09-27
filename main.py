import Module1.VectorOperations as vec

vec1 = vec.Vector(12, 9)
vec2 = vec.Vector(3, 4)

print(vec1)
print(abs(vec1))
if (vec1):
    print("true")
else:
    print("false")
print(vec1 + vec2)
print(vec2 * 3)
