class people:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def show(self):
        print("Ten ban la %s, hien dang %d" %(self.name,self.age))
class student(people):
    def __init__(self,name,age,school):
        super().__init__(name,age)
        student.school=school
    def show(self):
        print("Ten ban la %s, hien dang %d, hoc tai %s" %(self.name,self.age,self.school))
I=people("Kham",20)
I.show()
I2=student("Kham",20,"phenikaa")
I2.show()
