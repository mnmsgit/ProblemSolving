class Solution(object):
    def trap(self, height):        
        # list for trapped water
        water = [0 for i in range(len(height))]
        # save height info into dictionary
        height_dict = {}
        for i,h in enumerate(height):
            for j in range(h+1):
                if j in height_dict:
                    height_dict[j].append(i)
                else:
                    height_dict[j] = [i]
        for key in height_dict:
            height_dict[key].sort()
        # calculate trapped water + original height
        max_height = max(height)
        for h in range(max_height+1):
            if h in height_dict:
                if len(height_dict[h]) == 1:
                    water[height_dict[h][0]] = h
                elif len(height_dict[h]) > 1:
                    for i in range(height_dict[h][0],height_dict[h][-1]+1):
                        water[i] = h
        print(water)
        return sum(water) - sum(height)
