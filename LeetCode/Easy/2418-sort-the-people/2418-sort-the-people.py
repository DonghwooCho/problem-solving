class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = []
        for i, v in enumerate(names):
            people.append((v, heights[i]))
        people.sort(key = lambda x: x[1], reverse = True)

        return [person[0] for person in people]