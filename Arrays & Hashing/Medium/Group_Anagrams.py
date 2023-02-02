class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:
            word_form = ''.join(sorted(word))
            if word_form in dictionary.keys():
                dictionary[word_form].append(word)
            else:
                dictionary[word_form] = [word]
        
        return(list(dictionary.values()))
