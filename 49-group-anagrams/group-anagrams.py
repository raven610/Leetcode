class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1 = defaultdict(list)
        for s in strs:
            l = [0]*26
            for i in s:
                l[ord(i)-ord('a')] += 1
            d1[tuple(l)].append(s) 
        return [i for i in d1.values()]