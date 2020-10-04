import re

# https://regex101.com

### grep:
    ## -i:
        # To search for a string regardless of casing add the -i flag in the grep command.
        # Example:
            # grep -i python /usr/share/dict/words
    
### Regular Expressions (regex):
    ## . (wildcard):
        # . is a wildcard that matches any character.
        
        
    ## ^ (circumflex) and $ (dollar sign):
        # ^ indicates start of a line.
        # $ indicates end of a line.
        # Example:
            # grep ^fruit /usr/share/dict/words
            # grep cat$ /usr/share/dict/words1
            
            
    ## r (raw string):
        # result = re.search(r'aza', 'plaza')
        # Raw strings tells the Python interpreter that it shouldn't try to interpret any special characters, and instead, should just pass the string to the function as is.
        
        
    ## re.IGNORECASE:
        # result = re.search(r'p.ng', 'Pangaea', re.IGNORECASE)
        # print(result)
            # <re.Match object; span=(0, 4), match='Pang'>
           
           
    ## [] (Square brackets):
        # print(re.search(r"[Pp]ython", "Python"))
            # <re.Match object; span=(0, 6), match='Python'>
            
        # print(re.search(r"[a-z]way", "The end of the highway"))
            # <re.Match object; span=(18, 22), match='hway'>
        
        # print(re.search(r"[a-z]way", "What a way to go"))
            # None
            
        # print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
            # <re.Match object; span=(0, 6), match='cloudy'>
        # print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))
            # <re.Match object; span=(0, 6), match='cloud9'>
           
            
    ## [^] (Square brackets with circumflex inside):
        # Matching characters that aren't in the group.
        
        # print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
            # <re.Match object; span=(4, 5), match=' '>
            
        # print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
            # <re.Match object; span=(30, 31), match='.'>
            

    ## | (Pipe):
        # Either/Or.
        
        # print(re.search(r"cat|dog", "I like cats."))
            # <re.Match object; span=(7, 10), match='cat'>
            
        # print(re.search(r"cat|dog", "I like both dogs and cats."))
            # <re.Match object; span=(12, 15), match='dog'>


    ## re.findall():
        # A regex method that finds all occurences.
        
        # print(re.findall(r"cat|dog", "I like both dogs and cats and dogs."))
            # ['dog', 'cat', 'dog']
            

    ## * (Asterisk):
        # Zero or more times.
        
        # print(re.search(r"A*B*C*", "AAACC"))
            # <re.Match object; span=(0, 5), match='AAACC'>

        # print(re.search(r"Py.*n", "Pygmalion"))
            # <re.Match object; span=(0, 9), match='Pygmalion'>
            
        # Example of a greedy behaviour:
        # print(re.search(r"Py.*n", "Python Programming"))
            # <re.Match object; span=(0, 17), match='Python Programmin'>
            
        # Less greedy example:
        # print(re.search(r"Py[a-z]*n", "Python Programming"))
            # <re.Match object; span=(0, 6), match='Python'>


    ## + (Plus):
        # 1 or more
        
        # print(re.search(r"o+l+", "goldfish"))
            # <re.Match object; span=(1, 3), match='ol'>
            
        # print(re.search(r"o+l+", "wooly"))
            # <re.Match object; span=(1, 4), match='ool'>
            
        # print(re.search(r"o+l+", "boil"))
            # None
            

    ## ? (Question mark):
        # 0 or 1
        
        # print(re.search(r"p?each", "To each their own"))
            # <re.Match object; span=(3, 7), match='each'>
            
        # print(re.search(r"p?each", "I like peaches"))
            # <re.Match object; span=(7, 12), match='peach'>


    ## \ (Back slash) Escape character:
        # Escapes a special character.
        # Turns special characters into regular character.
        
        # print(re.search(r".com", "welcome"))
            # <re.Match object; span=(2, 6), match='lcom'>
            
        # print(re.search(r"\.com", "welcome"))
            # None
            
        # print(re.search(r"\.com", "mydomain.com"))
            # <re.Match object; span=(8, 12), match='.com'>
            

    ## \w
        # Matches any alphanumeric character.
        # It matches letters, numbers and underscores.
        
        # print(re.search(r"\w*", "This is an example"))
            # <re.Match object; span=(0, 4), match='This'>
            
        # print(re.search(r"\w*", "And_this_is_another"))
            # <re.Match object; span=(0, 19), match='And_this_is_another'>


    ## \d
        # Matches digits
        

    ## \s
        # Matches white space characters
        
        
    ## () Capturing groups:
        # result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
        # print(result)
            # <re.Match object; span=(0, 13), match='Lovelace, Ada'>
        # result.groups()
        # print(result.groups())
            # ('Lovelace', 'Ada')
        # print(result[0])
            # Lovelace, Ada
        # print(result[1])
            # Lovelace
        # print(result[2])
            # Ada

def rearrange_name1():
    def rearrange_name(name):
        result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
        if result is None:
            return name
        return "{} {}".format(result[2], result[1])
    print(rearrange_name("Lovelace, Ada"))
        # Ada Lovelace
    print(rearrange_name("Ritchie, Dennis"))
        # Dennis Ritchie
    print(rearrange_name("Hopper, Grace M."))
# rearrange_name1()

    ## \b (boundary) and {} Repition qualifiers:
        # print(re.findall(r"[a-zA-Z]{5}", "A scary ghost appeared"))
            # ['scary', 'ghost', 'appea']
        # print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))
            # ['scary', 'ghost']
        # print(re.findall(r"\w{5,10}", "I really like strawberries"))
            # ['really', 'strawberri']
        # print(re.findall(r"\w{5,}", "I really like strawberries"))
            # ['really', 'strawberries']
        # print(re.search(r"s\w{,20}", "I really like strawberries"))
            # <re.Match object; span=(14, 26), match='strawberries'>
            
def extract_pid1():
    def extract_pid(log_line):
        ## Process ID (PID):
        regex = r"\[(\d+)\]"
        result = re.search(regex, log_line)
        if result is None:
            return ""
        return result[1]
    print(extract_pid("99 elephants in a [cage]"))
        # 
# extract_pid1()

    ## re.split():
        # print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))
            # ['One sentence', ' Another one', ' And the last one', '']
            
        # print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))
            # ['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']
            
    
    ## re.sub(): replacing characters:
        # print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts@my.example.com"))
            # Received an email for [REDACTED]
            
    ## Change the order of the capturing groups:
        # /2 and /1 refers to the 2nd and 1st capturing groups.
        # print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))
            # Ada Lovelace
            
    ## Regex backreference:
        # https://www.regular-expressions.info/backref.html
        # The \1 refers to the first captured group. It's like a copy paste
        # <([A-Z][A-Z0-9]*)\b[^>]*>.*?</\1>