# Medium
# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)             
        for word in strs:
            sortedWord ="".join(sorted(word)) 
            hashmap[sortedWord].append(word)
        return list(hashmap.values())