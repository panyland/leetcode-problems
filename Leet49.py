# Group list of strings by anagrams 
def groupAnagrams(strs):
    anagram_map = {}
    result = []
    for s in strs:
        ssorted = "".join(sorted(s))     
        if ssorted in anagram_map.keys():
            anagram_map[ssorted].append(s)
        else: 
            anagram_map[ssorted] = []
            anagram_map[ssorted].append(s)
    result = anagram_map.values()
    return result 


input = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(input))

