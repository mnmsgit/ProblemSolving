class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        letters = dict()
        for task in tasks:
            if task in letters:
                letters[task] += 1
            else:
                letters[task] = 1
        
        arr = []
        for letter in letters.values():
            arr.append(letter)
        arr.sort(reverse=True)
        tick = 0
        len_arr = len(arr)
        remaining = [-1 for i in range(len_arr)]
        flag = True
        ans = []
        while flag:
            idle = False
            max_index = -1
            max_value = 0
            for i in range(len_arr):
                if remaining[i] < 0 and arr[i] >max_value:
                    max_index = i 
                    max_value = arr[i]
            if max_index >=0:
                arr[max_index] -= 1
                remaining[max_index] = n
                tick +=1
                idle =False
                ans.append(max_index)
            else:
                tick +=1
                ans.append(-1)
            flag = False
            for i in range(len_arr):
                remaining[i] -=1
                if arr[i] > 0:
                    flag =True
        # print(ans)

        return tick
