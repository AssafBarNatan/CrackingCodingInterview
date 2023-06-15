#This document contains implementations of the exercises in 
#chapter 1 of cracking the coding interview

from collections import Counter
import numpy as np
import re


def is_unique(s):
    '''
    Takes in a string s, and returns true if s contains all unique 
    characters. Can you do this witout using other data structures?
    '''
    if not s:
        return True

    chars = {}

    for char in s:
        if char in chars.keys():
            return False
        else:
            chars[char] = 1
    return True

def is_unique(s):
    '''
    see above: no additional data structures
    '''
    if not s:
        return True
    for char1 in s:
        for char2 in s:
            if char1 == char2:
                return False
    return True


def check_permutations(s1, s2):
    '''
    Checks if s1 is a permutation of s2
    '''
    if not len(s1) == len(s2):
        return False
    d1 = {}
    for ch in s1:
        if ch in d1:
            d1[ch] += 1
        else:
            d1[ch] = 1
    for ch in s2:
        if ch in d1:
            d1[ch] -=1
            if d1[ch] == 0:
                del d1[ch]
        else:
            return False
    if d1:
        return False
    else:
        return True

def URLify(s):
    '''
    Replaces all whitespaces with %20 (from the example, 
    I think that they also want us to get rid of 
    trailing whitespaces, but I'm not gonna do that.
    '''
    out = ""
    for ch in s:
        if ch == " ":
            out.append("%20")
        else:
            out.append(ch)
    return out



def palindrome_permutation(s):
    '''
    Checks if a string s is a permutation of a palindrome
    Followup: use the collectons -> counter package

    Implementation number 1:
    d = {}
    for ch in s:
        if ch in d:
            d[ch] -= 1
        else:
            d[ch] = 1

    if sum(d.values()) > 1:
        return False
    return True
    '''

    c = Counter(list(s))
    if sum([val % 2 for val in c.values()]) > 1:
        return False
    return True

#testcases = ["","lllo","llo","abraca"]
#for test in testcases:
#    print(test)
#    if palindrome_permutation(test):
#        print("is a palindrome permutation")
#    else:
#        print("is not a palindrome permutation")

def one_away(tup):
    '''
    Checks if s1 is "one edit" away from s2, where an edit is one 
    of: 
        1. Deleting a character
        2. Inserting a character
        3. Changing one character
    '''
    s1 = tup[0]
    s2 = tup[1]


    if len(s2) > len(s1):
        t = s1 
        s1 = s2
        s2 = t

    if len(s1) - len(s2) > 1:
        return False

    elif abs(len(s1) - len(s2)) == 0:
        change = 0
        for i in range(len(s1)):
            if not s1[i] == s2[i]:
                change +=1
                if change > 1:
                    return False
        return True

    elif len(s1) - len(s2) == 1:
        p1 = 0
        p2 = 0
        jump = 0
        while p1 < len(s1) and p2 < len(s2):
            if s1[p1] == s2[p2]:
                p1 += 1
                p2 += 1
            else:
                p1 +=1
                jump += 1
                if jump > 1:
                    return False
        return True

#testcases = [("","a"), ("aba","bab"), ("aab","abb"), ("abcd","abd"), ("abcd", "abc"), ("abcd", "cd"), ("abcd", "bcd")]
#testcases2 = [(pair[1], pair[0]) for pair in testcases]
#testcases = testcases + testcases2
#
#for test in testcases:
#    print(f'The strings: {test} are one away? {one_away(test)}')
#

def string_compression(s):
    '''
    Implement basic string compression, converting 
    an [a-z] string like aaaabbbb to 5a4b. If the 
    string compression is not compressive, return the 
    original string.
    '''
    if not s:
        return ''

    out = ''
    ch = ''
    count = 0
    for i in range(len(s)):
        if s[i] == ch:
            count +=1
        else:
            # normally this could be if count > 0, but 
            # I can improve the algorithm by removing trailing 1s
            if count > 1:
                out += str(count)+ch
            if count == 1:
                out += ch
            ch = s[i]
            count = 1
    if count:
        out += str(count) + ch
    return (out if len(out)<len(s) else s)

#testcases = ['','aaaaaaaaabbbbbbbaaaaaaaa', 'aabbaa', 'asd', 'aab','abracadabra', 'baaa', 'baaabb', 'bbaa']
#for test in testcases:
#    print(f'The string: {test} is compressed to: {string_compression(test)}')
#
def rotate_matrix(M):
    '''
    given an image represented by an NxN matrix, 
    where each pixel is represented by an int, 
    write a method to rotate the image by 90 degrees. 

    Do this in place
    '''

    def reflect_y(M):
        for i in range(int(len(M)/2)):
            for j in range(len(M[0])):
                tmp = M[i][j]
                M[i][j] = M[len(M)-i-1][j]
                M[len(M)-i-1][j] = tmp
        return M

    def transpose(M):
        for i in range(len(M)):
            for j in range(i):
                tmp = M[i][j]
                M[i][j] = M[j][i]
                M[j][i] = tmp
        return M

    return transpose(reflect_y(M))

def zero_matrix(M):
    '''
    write an algorithm such that if (i,j) = 0, 
    then the entire row i and column j are 0
    '''
    hitcols = set([])
    killrow = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 0:
                killrow = 1
                hitcols.add(j)

        if killrow:
            M[i] = [0]*len(M[0])
            killrow = 0

    for i in range(len(M)):
        for j in list(hitcols):
            M[i][j] = 0
    return M

def is_substring(s1, s2):
    '''
    returns TRUE if s1 is a contiguous substring of s2
    '''
    return bool(re.match(re.compile(s1),s2))

def string_rotation(s1, s2):
    '''
    code a method: is_substring which checks if a 
    word is a substring of another.

    Then write code to check if s2 is a rotation of s1 using only 
    one call to is_substring
    '''

    return is_substring(s1,s2+s2) and len(s1) == len(s2)
