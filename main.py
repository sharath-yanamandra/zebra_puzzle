from constraint import *
problem = Problem()

nationality = ["English", "Spanish", "Ukrainian", "Norwegian", "Japanese"] #inserting all contries
pet = ["dog", "snails", "fox", "zebra", "horse"] #inserting animals
cigarette = ["Old Gold", "Kools", "Chesterfields", "Lucky Strike", "Parliaments"] #inserting cigarette they smoke
colour = ["red", "green", "yellow", "blue", "ivory"] #specifing the colour of the house
beverage = ["coffee", "milk", "orange juice", "water", "tea"] #beverage they drink

criteria = nationality + pet + cigarette + colour + beverage
problem.addVariables(criteria,[1,2,3,4,5]) #adding variable to the criteria in the specified order

problem.addConstraint(AllDifferentConstraint(), nationality) #Adding a new constraint specifing all are different values in it
problem.addConstraint(AllDifferentConstraint(), pet)
problem.addConstraint(AllDifferentConstraint(), cigarette)
problem.addConstraint(AllDifferentConstraint(), colour)
problem.addConstraint(AllDifferentConstraint(), beverage)

problem.addConstraint(lambda e, r: e == r, ["English","red"]) #anonymous function by clues given
problem.addConstraint(lambda s, d: s == d, ("Spanish","dog"))
problem.addConstraint(lambda c, g: c == g, ("coffee","green"))
problem.addConstraint(lambda u, t: u == t, ("Ukrainian","tea"))
problem.addConstraint(lambda g, i: g-i == 1, ("green","ivory"))
problem.addConstraint(lambda o, s: o == s, ("Old Gold","snails"))
problem.addConstraint(lambda k, y: k == y, ("Kools","yellow"))
problem.addConstraint(InSetConstraint([3]), ["milk"]) #clearly mentioned "in house 3 drinks milk"
problem.addConstraint(InSetConstraint([1]), ["Norwegian"]) #mentioned "norwegian lives in house 1"
problem.addConstraint(lambda c, f: abs(c-f) == 1, ("Chesterfields","fox")) #absolute value of a person(c) lives next to house having fox(f)
problem.addConstraint(lambda k, h: abs(k-h) == 1, ("Kools","horse")) #absolute value of k lives
problem.addConstraint(lambda l, o: l == o, ["Lucky Strike","orange juice"])
problem.addConstraint(lambda j, p: j == p, ["Japanese","Parliaments"])
problem.addConstraint(lambda k, h: abs(k-h) == 1, ("Norwegian","blue")) #similar to rule 6. i.e lives next to is same as immediately right.

solution = problem.getSolutions()[0]

for i in range(1,6):
    for x in solution:
        if solution[x] == i:
            print (str(i), x)