c = [["HTML","Java"],["Java","Python"],["Python","HTML"]]
r = [0,1,1]

def tournamentWinner(competitions, results):
    # Write your code here.
	a = {}
	for i in range(len(competitions)):
		if results[i] == 0:
			if competitions[i][1] in a:
				a[competitions[i][1]] += 3
			else:
				a[competitions[i][1]] = 3
		if results[i] == 1:
			if competitions[i][0] in a:
				a[competitions[i][0]] += 3
			else:
				a[competitions[i][0]] = 3
	keymax = max(a,key = a.get)
	return keymax


print(tournamentWinner(c,r))