from pyamaze import maze,agent
def BFS(m):
    start=(m.rows,m.cols)
    frontier=[start]
    explored=[start]
    bSearch=[start]
    while len(frontier)>0:
        currCell=frontier.pop(0)
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bSearch.append(childCell)
    
    return bSearch

if __name__=='__main__':
    m=maze(15,15)
    m.CreateMaze(loopPercent=10)
    bSearch=BFS(m)
    a=agent(m,shape="square",footprints=True,filled=True)
    m.tracePath({a:bSearch} , delay=50 )
    
    m.run()