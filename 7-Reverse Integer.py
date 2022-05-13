class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            negative = True
            x = x * -1
        as_lst = str(x)
        as_lst = ''.join(reversed(as_lst))
        if len(as_lst) < 10:
            if negative:
                return -1 * int(as_lst)
            else:
                return int(as_lst)
        if len(as_lst) > 10:
            return 0
        int_max = [2,1,4,7,4,8,3,6,4,7]
        for i in range(len(as_lst) - 1):
            if int(as_lst[i]) < int(int_max[i]):
                if negative:
                    return -1 * int(as_lst)
                else:
                    return int(as_lst)
            if int(as_lst[i]) > int(int_max[i]):
                return 0
        if negative and int(as_lst[-1]) < 9:
            return -1 * int(as_lst)
        if not negative and int(as_lst[-1]) < 8:
            return int(as_lst)
        return 0
        
        
