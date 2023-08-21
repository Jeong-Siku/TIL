def solution(myString, pat): 
    idx = myString[::-1].index(pat[::-1])
    return myString[:-idx]  if idx else myString