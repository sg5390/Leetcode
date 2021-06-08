def wordBreak(s,wordDict):
        if (s == None) and (len(s) == 0):
            return false
        setss = set()
        
        def helper(s):
        #base
            if(len(s)==0):
                return True
        
        #logic
        for i in range(0,len(s)):
            print(i)
            if s[0,i+1] in setss and helper(s[i+1]):
                return True
        return false
    
    
        for elem in wordDict:
            setss.add(elem)
            return helper(s)