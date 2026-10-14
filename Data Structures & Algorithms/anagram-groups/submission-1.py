class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        store = {}

        for i,v in enumerate(strs):
            newv = ''.join(sorted(v))
            if newv in store:
                store[newv].append(v)
                print(store[newv])
            else:
                store[newv] = []
                store[newv].append(v)
        result = []

        for values in store.values():
            result.append(values)
            print(values)

        return result