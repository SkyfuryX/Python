#! python3

import pyperclip, re

#TODO: Create regex opjects for phone numbers
phoneRegex = re.compile(r'''
(((\d\d\d)|(\(\d\d\d\)))? #area code (optional)
(\s|-)?         # first separator(optional)
\d\d\d          # first three digits
-               # separator
\d\d\d\d        #last 4 digits
(((ext(\.)?\s)|x) #extention(optional)
(\d{2,5}))?)     #extention digits(optional)
''',re.VERBOSE)

#TODO: Create regex opbjects for email address
emailRegex = re.compile(r'''
\S+ #beginning of email
@ # @ symbol
\S+ # domain and
\. # .character
\S+ # email suffix
''',re.VERBOSE)

#TODO: Get text off the clipboard
text = pyperclip.paste()

#TODO: extract the emails and phone numbers fomr the text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#for testing
#print(allPhoneNumbers)
#print(extractedEmail)

#TODO copy the extracted email.phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)


