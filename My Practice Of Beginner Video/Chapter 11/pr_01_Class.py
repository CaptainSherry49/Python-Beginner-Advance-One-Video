class C_2D_Vector:
    Vector_Chapter =  4
    Book = "Physics"

class C_3D_Vector(C_2D_Vector):

    def __init__(self,Book,Vector_Chapter):
        self.Book = Book
        self.Vector_Chapter = Vector_Chapter
        
V1 = C_2D_Vector
V2 = C_3D_Vector

print(f"The Book name is {V2.Book}")
print(f"The Chapter name is {V2.Vector_Chapter}")