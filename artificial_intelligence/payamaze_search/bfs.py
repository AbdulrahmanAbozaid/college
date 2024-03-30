"""Implementing BFS on a maze"""
from turtle import color
from pyamaze import maze, agent, COLOR


def BFS(m):
	"""Breadth-first traversal"""
	start = (m.rows, m.cols)
	queue = [start]
	visited = [start]
	src_path = []
	goal_path = {}

	while len(queue)>0:
		curr = queue.pop(0)
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
				queue.append(ch)
				goal_path[ch] = curr
	real_path = {}
	cell = (1, 1)
	while cell != start:
		real_path[goal_path[cell]] = cell
		cell = goal_path[cell]
	return src_path, real_path


if __name__ == '__main__':
	m = maze(15, 15)
	m.CreateMaze(theme=COLOR.light, loopPercent=10)
	a = agent(m, filled=True, footprints=True, color=COLOR.yellow)
	b = agent(m, footprints=True, color=COLOR.red)

	paths = BFS(m)
	m.tracePath({a:paths[0]}, kill=True, delay=60)
	m.tracePath({b:paths[1]}, delay=50)

	m.run()
