"""leetcode: 383. Ransom Note """

def hdx(ransomNote: str, magazine: str) -> bool:
    """ Given two strings ransomNote and magazine, returns true if
    ransomNote can be constructed by using the letters from magazine
    and false otherwise."""
    for char in ransomNote:
        if char in magazine:
            magazine = magazine.replace(char,"",1)
        else:
            return False
    return True


print(hdx("a", "b"))
print(hdx("aa", "ab"))
print(hdx("aa", "aab"))
print(hdx("aac", "abca"))
