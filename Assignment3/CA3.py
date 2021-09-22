import pulp as p 

Lp_prob = p.LpProblem('Problem', p.LpMinimize)    
numberOfVertex, numberOfEdges= list(map(int,input().split())) 

# define Vars

variable = []
for i in range(numberOfVertex):
    variable.append(p.LpVariable("x" + str(i), lowBound = 0))

# define constrains

constrains= []
for i in range(numberOfEdges):
    First = "constrains" + str(i) + str(0)
    Second = "constrains" + str(i) + str(1)
    constrains.append([p.LpVariable(First, cat='Binary'), p.LpVariable(Second, cat='Binary')])
lpMax =  p.LpVariable("lpMax", lowBound = 0)   
Lp_prob +=  lpMax

# Update Constraints and Variables for Problem: 

for i in range(numberOfVertex):
    Lp_prob += lpMax >= variable[i]
for i in range(numberOfEdges):
    a, b = input().split()
    Lp_prob += variable[int(a)] - variable[int(b)]-( numberOfVertex * (1 - constrains[i][0])) <= -1
    Lp_prob += variable[int(b)] - variable[int(a)] - ( numberOfVertex * (1 - constrains[i][1])) <= -1
    Lp_prob += constrains[i][0] + constrains[i][1] >= 1

# Solve

status = Lp_prob.solve()   
print(p.LpStatus[Lp_prob.status])
print("Ans: ", p.value(Lp_prob.objective) + 1)