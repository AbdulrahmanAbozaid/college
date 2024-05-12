"""Implementing A* on a maze"""
from pyamaze import maze, agent, COLOR
from util import PriorityQueue

def mdis(p):
	return (p[0] - 1) + (p[1] - 1)

def astar(m):
	"""A* traversal"""
	start = (m.rows, m.cols)
	queue = PriorityQueue()
	visited = [start]
	src_path = []
	goal_path = {}
	queue.push(start, mdis(start))

	while not queue.isEmpty():
		curr = queue.pop()
		src_path.append(curr)

		if curr == (1, 1):
			break

		for d in "ESNW":
			if m.maze_map[curr][d] == True:
				if d == 'E':
					ch = (curr[0], curr[1] + 1)
				elif d == 'W':
					ch = (curr[0], curr[1] - 1)
				elif d == 'S':
					ch = (curr[0] + 1, curr[1])
				elif d == 'N':
					ch = (curr[0] - 1, curr[1])
				# print(ch)
				if ch in visited:
					continue
				visited.append(ch)
				queue.push(ch, mdis(ch))
				goal_path[ch] = curr
	real_path = {}
	cell = (1, 1)
	while cell != start:
		real_path[goal_path[cell]] = cell
		cell = goal_path[cell]
	return src_path, real_path


if __name__ == '__main__':
	m = maze(15, 15)
	m.CreateMaze(theme=COLOR.light, loopPercent=10, saveMaze=True)
	a = agent(m, filled=True, footprints=True, color=COLOR.yellow)
	b = agent(m, footprints=True, color=COLOR.red)

	paths = astar(m)
	m.tracePath({a:paths[0]}, kill=True, delay=60)
	m.tracePath({b:paths[1]}, delay=50)

	m.run()
