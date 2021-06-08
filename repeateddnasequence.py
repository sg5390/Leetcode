 def findRepeatedDnaSequences(self, s: str) -> List[str]:
        allsubs = set()
        result = set()
        for i in range(len(s)-10+1):
            sub = s[i:i+10]
            if sub in allsubs:
                result.add(sub)
            allsubs.add(sub)
        return result
