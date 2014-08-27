file = '057-KillerSudokuCages.txt'
symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ#+='

n = 3

grid = ['0' for i in range(n*n) for j in range(n*n)]

with open(file) as f:
	i = 0
	for line in f:
		for num in line.split()[1:]:
			grid[int(num)] = symbols[i]
		i += 1
		
for i in range(n*n*n*n):
	print grid[i],
	if (i+1) % (n*n) == 0:
		print