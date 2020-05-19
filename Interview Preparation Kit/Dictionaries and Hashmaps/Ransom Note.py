"""Link: https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview
-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his
handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an
untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words
available in the magazine. He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note
exactly using whole words from the magazine; otherwise, print No.

For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the
right words, but there's a case mismatch. The answer is No

Sample Input 0

6 4
give me one grand today night
give one grand today

Sample Output 0

Yes
"""


def checkMagazine(magazine, note):

    """
    This Solutions has the:
        - Run Time complexity: O(N)
        - Space Complexity: O(N)
    For Run Time Complexity searching operation in dictionary is constant time so
    the loop will only go through the length of the Ransom Note so that is why it is O(N).

    """

    magazine_dict = {}  # Word count dictionary for the magazine
    note_dict = {}  # word count dictionary for the ransom note

    """ Creating key:value pair for the word and the occurrence of the word"""
    for word in magazine:
        if word in magazine_dict:
            magazine_dict[word] += 1
        else:
            magazine_dict[word] = 1

    for word in note:
        if word in note_dict:
            note_dict[word] += 1
        else:
            note_dict[word] = 1

    """ 
    Looping through each word in the ransom note to check: 
        1. if the word in available in the magazine
        2. if the count of occurrence is magazine is always greater than or equal to the count in the ransom note.
        
    """
    for pair in note_dict:
        if pair in magazine_dict:
            if note_dict[pair] <= magazine_dict[pair]:
                pass
            else:
                print('No')
                return
        else:
            print('No')
            return

    print('Yes')


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
