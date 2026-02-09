class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        L = len(beginWord)
        patternMap = defaultdict(list)

        for word in wordList:
            for i in range(L):
                pattern = word[:i] + '*' + word[i+1:]
                patternMap[pattern].append(word)

        q = deque()
        q.append((beginWord,1))

        visited  = set()

        visited.add(beginWord)


        while q:
            curr,level = q.popleft()

            if curr == endWord:
                return level


            
            for i in range(L):
                pattern = curr[:i] + "*" + curr[i+1:]    
                for nei in patternMap[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei,level + 1))
            
                patternMap[pattern] = []


        return 0    