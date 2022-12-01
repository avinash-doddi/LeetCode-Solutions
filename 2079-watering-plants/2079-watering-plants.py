class Solution:
    def wateringPlants(self, plants: List[int], cap: int) -> int:
        n = len(plants); temp = cap
        if (n == 1): return 1;
        steps = 0; init = 1
        for i in range(n):
            if (init):
                steps += 1; temp -= plants[i]; init = 0;
            else:
                if (plants[i] > temp):
                    steps += (i*2)+1; temp = cap - plants[i];
                else:
                    steps += 1; temp -= plants[i];
            print(steps, end = " ")
        return steps