class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionnary = {}
        for word in strs:
            word_form = ''.join(sorted(word))
            if word_form in dictionnary.keys():
                dictionnary[word_form].append(word)
            else:
                dictionnary[word_form] = [word]
        
        return(list(dictionnary.values()))
