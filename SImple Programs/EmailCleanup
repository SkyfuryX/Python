# References:
#https://docs.python.org/3/library/imaplib.html
#https://stackoverflow.com/questions/19001266/how-to-search-specific-e-mail-using-python-imaplib-imap4-search

import imaplib
count = 0

#ensures nummber of emails to delete, restarts on incorrect input, breaks over 5 errors 
def confirmnum():
    global count    
    if count > 5:
        raise Exception('Try again later.')
    print('There are ' + str(len(id_list)) + ' emails containing "unsubscribe" that could be deleted.\nStarting with the oldest, how many do you want to delete?')
    num = input()
    if str(num).isnumeric() == False:
        print('You must enter a number.\n')
        count += 1
        confirmnum()    
    elif int(num) > len(id_list)-1:
        print('The number must be smaller than ' + str(len(id_list)) + '\n')
        count += 1
        confirmnum()
    else:
        return int(num)
        
#initiates connection
conn = imaplib.IMAP4_SSL(host = 'imap.gmail.com')
conn.login('Email', 'password') #email / app password

#Selects inbox, allows changes
conn.select(mailbox='INBOX', readonly=False) 

#finds all messages that contanin unsubscribe in the body
result, data = conn.search(None, '(BODY "Unsubscribe")') 

#splits data into results that can be viewed
id_list = data[0]
id_list = id_list.split()

#calls funtion to choose how many emails to delete
num_delete = confirmnum()
count = 0
print('Working...')

#deletes every email selected prior
for i in range(num_delete):
    conn.store(id_list[i], '+FLAGS', '\\Deleted')
    
    if round(num_delete * 0.25, 0) == i+1:
        print('25% complete...')
    elif round(num_delete * 0.5, 0) == i+1:
        print('50% complete...')
    elif round(num_delete * 0.75, 0) == i+1:
        print('75% complete...')
    elif num_delete == i+1:
        print('100% complete!')
    
#ends the connection
conn.close()
conn.logout()

