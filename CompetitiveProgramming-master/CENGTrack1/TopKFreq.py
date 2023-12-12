from heapq import *
from collections import Counter
<<<<<<< HEAD
<<<<<<< HEAD
# class Solution:
#     def topKFrequent(self, words: [str], k: int) -> [str]:
#         heap = []
#         word_count = Counter(words)

#         for key in word_count:
#             heap.append(-word_count[key])

#         heapify(heap)

#         freq = []
#         i = 0
#         while i < k:
#             mx = heappop(heap)
#             words = []
#             for j in word_count:
#                 if word_count[j] == -mx and j not in freq:
#                     words.append(j)
#             freq.extend(sorted(words))
#             i += 1
        
#         return freq[:k]

class Solution:
    def topKFrequent(self, words: [str], k: int) -> [str]:
        heap = set()
        word_count = Counter(words)

        for key in word_count:
            heap.add(-word_count[key])

        heap = list(heap)

        heapify(heap)
        
        freq = []
        i = 0
        length = len(heap)
        while i < length:
            mx = heappop(heap)
            words = []
            for j in word_count:
                if word_count[j] == -mx:
                    words.append(j)
                    
=======
=======
>>>>>>> 04920eb23532d69c41be6dca5a1496ac538cceee
class Solution:
    def topKFrequent(self, words: [str], k: int) -> [str]:
        heap = []
        word_count = Counter(words)

        for key in word_count:
            heap.append(-word_count[key])

        heapify(heap)

        freq = []
        i = 0
        while i < k:
            mx = heappop(heap)
            words = []
            for j in word_count:
                if word_count[j] == -mx and j not in freq:
                    words.append(j)
<<<<<<< HEAD
>>>>>>> 04920eb23532d69c41be6dca5a1496ac538cceee
=======
>>>>>>> 04920eb23532d69c41be6dca5a1496ac538cceee
            freq.extend(sorted(words))
            i += 1
        
        return freq[:k]

<<<<<<< HEAD
<<<<<<< HEAD
        

=======
>>>>>>> 04920eb23532d69c41be6dca5a1496ac538cceee
=======
>>>>>>> 04920eb23532d69c41be6dca5a1496ac538cceee
        