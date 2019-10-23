from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def valid(word1, word2):
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff +=1
            return diff == 1
        
        def nextWord(word, wordList):
            res = []
            for w in wordList:
                if valid(word, w):
                    res.append(w)
            return res
        
        if not beginWord or not endWord or endWord not in wordList or not wordList:
            return 0
        
        d = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '.' + word[i+1:]
                d[key].append(word)
        
        visited = set()
        visited.add(beginWord)
        queue = [(beginWord,1)]
        while queue:
            curr, level = queue.pop(0)
            for i in range(len(curr)):
                key = curr[:i] + '.' + curr[i+1:]
                for word in d[key]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        queue.append((word, level + 1))
                        visited.add(word)
        return 0
