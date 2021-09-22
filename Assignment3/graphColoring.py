import pulp as p 
  
Lp_prob = p.LpProblem('Problem', p.LpMinimize)    
  

numberOfVertex,  numberOfEdges= input().split()
variable = []
constrains= []
lpMax =  p.LpVariable("lpMax", lowBound = 0)   

for i in range(int(numberOfVertex)):
    temp = "x" + str(i)
    variable.append(p.LpVariable(temp, lowBound = 0))

for i in range(int(numberOfEdges)):
    temp = "constrains" + str(i) + str(0)
    temp1 = "constrains" + str(i) + str(1)
    temp2 = []
    temp2.append(p.LpVariable(temp, cat='Binary'))
    temp2.append(p.LpVariable(temp1, cat='Binary'))
    constrains.append(temp2)

Lp_prob +=  lpMax

# Constraints: 

for i in range(int(numberOfVertex)):
    Lp_prob += lpMax >= variable[i]

for i in range(int(numberOfEdges)):
    temp1, temp2 = input().split()
    Lp_prob += variable[int(temp1)] - variable[int(temp2)]-( int(numberOfVertex) * (1 - constrains[i][0])) <= -1
    Lp_prob += variable[int(temp2)] - variable[int(temp1)] - ( int(numberOfVertex) * (1 - constrains[i][1])) <= -1
    Lp_prob += constrains[i][0] + constrains[i][1] >= 1

status = Lp_prob.solve()   # Solver 

print(p.LpStatus[Lp_prob.status])
print(" the chromatic number of a given graph is :")
print(p.value(Lp_prob.objective) + 1)