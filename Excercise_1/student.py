#Sajal Baral, Asim Siddique, Shawn Kiruba, Kevin Avila, Shail Patel
class student:
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa

    def report_gpa(self):
        return (f"{self.name} has a GPA of {self.gpa}")
