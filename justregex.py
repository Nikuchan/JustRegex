import re
# 1: re.search(pattern,string,flags)
# It searches anywhere within the string.
# Example

print("Examples of re.search")
x=re.search("c","abcdef")
print(x)

# To get the matched text
x=re.search("c","abcdef").group()
print(x)

# If you want to get the starting index
x=re.search("c","abcdef").start()
print(x)

# To get the ending index
x=re.search("c","abcdef").end()
print(x)

# re.search only seaches for the first instant
x=re.search("c","ascsadc")
print(x)

# re.search works with the newline as well
x=re.search("c","abdef\nc")
print(x)

# 2: re.match(pattern,string,flags)

# It only searches at the beginning of the string.

# Example
print("Showing examples for re.match")

x = re.match("c","abcdef")
print(x)

# When you take the boolean value of none , it returns false.

x = bool(re.match("c","abcdef"))
print(x)

# re.match does not work with the newline

x=re.match("c","abcdef\nc")
print(x)

# To print the String value use group(), default parameter is 0

x=re.match("a","abcdef").group()
print(x)

# is same as

x=re.match("a","abcdef").group(0)
print(x)

# 3: re.findall(pattern,string,flags)

# It is going to find all the instances as a list

x=re.findall("n|a","bcdefnc abcda")
print(x)
