# Problem 76: Count vowels in a string using recursion

def count_vowels(s, index=0):
    if index == len(s):
        return 0
    
    vowels = "aeiouAEIOU"
    count = 1 if s[index] in vowels else 0
    
    return count + count_vowels(s, index + 1)

string = input("Enter a string: ")

vowel_count = count_vowels(string)
print(f"Number of vowels in '{string}': {vowel_count}")
