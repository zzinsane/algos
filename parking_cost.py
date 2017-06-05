# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

import datetime
def solution(E, L):
    # write your code in Python 2.7
	start = "20170101 " + E
	end = "20170101 " + L
	startDate = datetime.datetime.strptime(start,"%Y%m%d %H:%M")
	endDate = datetime.datetime.strptime(end,"%Y%m%d %H:%M")
	seconds = (endDate - startDate).seconds
	if seconds == 0:
		return 2
	hours = seconds / 3600
	hours = (hours + 1) if seconds % 3600 != 0 else hours

	return 2 + 3 + 4 * (hours - 1)




print solution("09:01", "15:30")
print solution("09:01", "15:01")
print solution("09:01", "10:01")
print solution("09:01", "10:02")
print solution("09:01", "09:02")
print solution("09:42", "11:42")
print solution("10:00", "13:21")
print solution("10:00", "10:00")
