def startEndLine():
    a="*"*75
    return a
def fortext(inptext):
    b="**"
    d=75-4
    c= inptext.center(d)
    return b+c+b

# b='Welcome to AIX Version 6.1!'
# c='Please see the README file in /usr/lpp/bos for information pertinent to'
# d='this release of the AIX Operating System.'
print(startEndLine())
print(fortext('Please see the README file in /usr/lpp/bos for information pertinent to'))
print(fortext('Please see the README file in /usr/lpp/bos for information pertinent to'))
print(fortext('this release of the AIX Operating System.'))
print(startEndLine())


