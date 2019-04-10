'''You are given two classes, Person and Student, where Person is the base class and Student is the derived class.
Completed code for Person and a declaration for Student are provided for you in the editor.
Observe that Student inherits all the properties of Person.
Complete the Student class by writing the following:
A Student class constructor, which has parameters:
A string, firstName.
A string, lastName.
An integer, id.
An integer array (or vector) of test scores.
A char calculate() method that calculates a Student object's average and returns the grade character representative of
their calculated average:
'''


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, id, scores):
        Person.__init__(self, firstName, lastName, id)
        self.scores = scores

    def calculate(self):
        self.calculate_by_score(self.average_score())

    def calculate_by_score(self, average_score):
        if average_score < 40:
            return 'T'
        elif average_score < 55:
            return 'D'
        elif average_score < 70:
            return 'P'
        elif average_score < 80:
            return 'A'
        elif average_score < 90:
            return 'E'
        elif average_score <= 100:
            return 'O'

    def average_score(self):
        sum_scores = 0
        for score in self.scores:
            sum_scores = sum_scores + score
        return sum_scores / len(self.scores)

    @staticmethod
    def print_student(student):
        print("Grade: ", student.calculate())


class UnivStudent(Student):

    def __init__(self, firstName, lastName, id, scores):
        super().__init__(firstName, lastName, id, scores)

    def calculate(self):
        average_score = self.average_score()

        if average_score < 100:
            return 'XXX'
        else:
            return super().calculate_by_score(average_score=average_score)




line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
p = Person(firstName, lastName, idNum)
s.calculate()
s.printPerson()

Student.print_student(s)


persons = [p, s]

s.printPerson()



