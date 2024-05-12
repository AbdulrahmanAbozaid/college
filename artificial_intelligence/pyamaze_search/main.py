from bfs import BFS
from dfs import DFS
from astar import astar
from pyamaze import maze, agent, COLOR

m = maze(15, 25)
# m.CreateMaze(theme=COLOR.light, loopPercent=20, saveMaze=True)
m.CreateMaze(theme=COLOR.light, loopPercent=20, loadMaze="maze--2024-03-30--08-56-20.csv")
a = agent(m, filled=True, footprints=True, color=COLOR.blue)
b = agent(m, footprints=True, color=COLOR.red)

x = agent(m, filled=True, footprints=True, color=COLOR.black)
y = agent(m, footprints=True, color=COLOR.yellow)

i = agent(m, filled=True, footprints=True, color=COLOR.cyan)
j = agent(m, footprints=True, color=COLOR.green)

paths = DFS(m)
m.tracePath({a:paths[0]}, kill=True, delay=60)
m.tracePath({b:paths[1]}, delay=50)

paths = BFS(m)

m.tracePath({x:paths[0]}, kill=True, delay=10)
m.tracePath({y:paths[1]}, delay=50)

paths = astar(m)

m.tracePath({i:paths[0]}, kill=True, delay=60)
m.tracePath({j:paths[1]}, delay=50)

m.run()