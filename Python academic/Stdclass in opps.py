class student:
    def __init__(self, usn, name):
        self.usn = usn
        self.name = name
        self.marks = []
        self.total = 0
        self.percentage = 0

    def readmarks(self):
        for i in range(3):
            m = float(input("Enter mark in subject: "))
            self.marks.append(m)

    def calculate_result(self):
        self.total = sum(self.marks)
        self.percentage = self.total / 3
    
    def display(self):
        print(f'usn: {self.usn}\nname: {self.name}')
        print(f'Total Marks: {self.total}')
        print(f'Percentage: {self.percentage}%')

usn = input("Enter the usn of the student: ")
name = input("Enter name: ")
s = student(usn, name)
s.readmarks()
s.calculate_result()
s.display()
