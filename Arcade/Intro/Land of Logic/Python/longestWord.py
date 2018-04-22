def longestWord(text):
    return sorted(re.sub(r'[^A-Za-z ]', ' ', text).split(' '), key=len)[-1]