import re

def StringChallenge(sen):
    # Code goes here
    # User input
    original_input = sen
    # Remove special characters
    sen = re.sub(r'[^a-zA-Z0-9\s]', '', sen)
    # Split string into words
    words = sen.split()
    # Find the longest word
    longest_word = max(words, key=len)
    # Concatenate with ChallengeToken
    final_output = longest_word + "yotai139vdbf"
    # Replace every third character with 'X'
    final_output = ''.join(char if (i + 1) % 3 != 0 else 'X' for i, char in enumerate(final_output))
    # Output format
    output_format = "Input: {}\nOutput: {}\nFinal Output: {}".format(original_input, longest_word, final_output)
    return output_format

# Keep this function call here
print(StringChallenge(input()))