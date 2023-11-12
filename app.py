class Teacher:

    def __init__(self, teacherId : int, teacherName : str) -> None: # Method / Constructor (__Init__)

        self.name : str = teacherName; # Attribute

        self.teacherId : int  = teacherId;

        self.organizationName: str = "PIAIC";

    def quarter(self, quarter : int ) -> None: # Method

        print(f"This Is Quarter {quarter}");
    
    def teaching(self, subject : str ) -> None:

        print(f"{self.name} Is Teaching {subject}...!");

obj1 : Teacher = Teacher(1, "Sir Zia Khan");

obj2 : Teacher = Teacher(2, "Sir Qasim");

print(f"Name: {obj1.name}, ID: {obj1.teacherId} & Organiztion: {obj1.organizationName} \n");

print(f"Name: {obj2.name}, ID: {obj2.teacherId} & Organiztion: {obj2.organizationName} \n");

obj1.teaching("BlockChain")

obj2.teaching("Generative AI")