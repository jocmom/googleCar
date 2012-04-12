colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print (p[i])


#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

p =[[0.05, 0.05, 0.05, 0.05, 0.05], 
    [0.05, 0.05, 0.05, 0.05, 0.05], 
    [0.05, 0.05, 0.05, 0.05, 0.05],     
    [0.05, 0.05, 0.05, 0.05, 0.05]]

sensor_wrong = 1 - sensor_right
p_stay = 1 - p_move

def sense(p, Z):
    q = []    
    # prior
    for r in range(len(p)):
        tmp = []
        for c in range(len(p[r])):
            hit = (Z == colors[r][c])
            tmp.append(p[r][c] * (hit * sensor_right + (1-hit) * sensor_wrong) )
        q.append(tmp)
    # normalize
    s = 0
    for r in range(len(q)):
        s += sum(q[r])
    for r in range(len(q)):
        for c in range(len(q[r])):        
            q[r][c] = q[r][c]/s
    return q
 
 
def move(p, U):
    q = []
    for r in range(len(p)):
        tmp = []
        for c in range(len(p[r])):
            s = p_stay * p[r][c]
            s += p_move * (p[(r-U[0])%len(p)][(c-U[1])%len(p[r])])
            tmp.append(s)
        q.append(tmp)
    return q
    
        
for i in range(len(measurements)):
    p = move(p, motions[i])
    p = sense(p, measurements[i])


#Your probability array must be printed 
#with the following code.

show(p)




