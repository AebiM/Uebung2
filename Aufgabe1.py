class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y , self.z - other.z)

    def __add__ (self, other):
        return Vector3(self.x + other.x, self.y + other.y , self.z + other.z)
    

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x * other, self.y * other, self.z * other)
        
        else:
            return Vector3(self.x * other.x, self.y * other.y , self.z * other.z)

    def __rmul__ (self, other):  
        if type(other) == int or type(other) == float:
            return Vector3(self.x * other, self.y * other, self.z * other)
        
        else:
            return Vector3(self.x * other.x, self.y * other.y , self.z * other.z)
        
    def dot(a,b):
        return a.x * b.x + a.y * b.y + a.z * b.z
    
    def cross(a,b):
        return Vector3(a.y * b.z - a.z * b.y,
                       a.z * b.x - a.x * b.z,
                       a.x * b.y - a.y * b.x)
    
    def normalize(a):
        mag = (a.x**2 + a.y**2 + a.z**2)**0.5
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector3(a.x / mag, a.y / mag, a.z / mag)


a = Vector3(3,4,2) 
b = Vector3(2,1,0) 
c = 3 * b      # Komponentenweise Multiplikation print(c) 

s = a.normalize()
print(s)