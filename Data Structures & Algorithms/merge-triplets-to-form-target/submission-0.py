class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        possible_triplets = []
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                possible_triplets.append(triplet)
        
        if possible_triplets == []: return False

        a, b, c = False, False, False
        for triplet in possible_triplets:
            if triplet[0] == target[0]:
                a = True
            
            if triplet[1] == target[1]:
                b = True
            
            if triplet[2] == target[2]:
                c = True
        return a and b and c

        
"""
2, 5, 6     1, 4, 4     5, 7, 5


"""