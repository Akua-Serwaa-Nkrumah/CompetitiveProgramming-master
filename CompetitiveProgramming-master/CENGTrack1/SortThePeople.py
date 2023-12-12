class Solution(object):
    def sortPeople(self, names, heights):
        heights_people = {}
        for i in range(len(heights)):
            heights_people[heights[i]] = names[i]
        
        heights = sorted(heights)
        heights.reverse()
        new_people = []
        for i in range(len(heights)):
            new_people.append(heights_people[heights[i]])
        
        return new_people