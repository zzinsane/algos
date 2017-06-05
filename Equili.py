
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
	# write your code in Python 2.7
	total = sum(A)

	current = 0
	result = []
	for idx,ele in enumerate(A):
		if total - ele - current == current:
			result.append(idx)
		current += ele

	return result[0] if len(result) > 0 else -1

print solution([-1, 3, -4, 5, 1, -6, 2, 1])
print solution([-1])
print solution([])
