
def max_sub_str(sublist):
    maximal = 0
    for i in sublist:
        if i:
            maximal += 1
        else:
            maximal = 0
    return maximal


class Solution(object):

    def matrix_stop(self, matrix, upp_left, low_right):
        if low_right[0] - upp_left[0] <=1:
            sublist = matrix[upp_left[0]][upp_left[1]:low_right[1] + 1]

            return  max_sub_str(sublist)

        if low_right[1] - upp_left[1] <=1:
            sublist = [matrix[ll][upp_left[1]] for ll in range(upp_left[0], low_right[0] + 1)]

            return  max_sub_str(sublist)

        return None

    def maximalRectangleWrapper(self, matrix, upp_left, low_right):
        stop = self.matrix_stop(matrix, upp_left, low_right)
        if stop:
            return stop

        fx_1_low = (low_right[0] - 1, low_right[1])
        fx_1 = self.matrix_stop(matrix, upp_left, fx_1_low)
        fy_1_low = (low_right[0], low_right[1] -1)
        fy_1 = self.matrix_stop(matrix, upp_left, fy_1_low)

        if fx_1_low



    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if len(matrix)  == 1 :
            pass
        fxy = self.maximalRectangle(self, m)
