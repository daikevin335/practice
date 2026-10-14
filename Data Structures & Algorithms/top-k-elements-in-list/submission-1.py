class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # dict to store number of time number appears 
        counts = {}
        # Index of bucket represents frequncy, bucket[1] = appear 1 time
        bucket = [[] for i in range(len(nums) + 1)]
        result = []

        # first track the counts of each number
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        # put each number into freq bucket 

        for num, count in counts.items():
            bucket[count].append(num)


        # go through bucket backwards to get top k frequent numbers

        for i in range(len(bucket) -1, -1, -1):
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result


        
