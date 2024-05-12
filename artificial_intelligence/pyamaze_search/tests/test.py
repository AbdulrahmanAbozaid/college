from pyamaze import maze, COLOR, agent

m = maze(10, 10)
m.CreateMaze(theme=COLOR.light)
a = agent(m, shape='square', filled=True, footprints=True, color=COLOR.red)
# a.position = (a.x-2, a.y-3)
# a.position = (a.x-2, a.y-3)
# a.position = (a.x-2, a.y-3)

# print(m.maze_map)
# print(m.path)
# m.markCells = [(5, 5), (1, 1), (1, 3), (2, 3)]
# m.tracePath({a: m.path}, delay=100, kill=False, showMarked=True)

# m.enableArrowKey(a)
# m.enableWASD(a)
m.run()