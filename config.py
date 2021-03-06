import os
CSRF_ENABLED = False
SECRET_KEY = os.environ['SECRET-KEY']

ADS_API_KEY= os.environ['KEY']

''''from string environment variables creating a list of them
    then use that list to create a dictionary named (di)
    since i need a dictionary not string
'''
AUTHOR=os.environ['AUTHORS']
di={}
for name in (AUTHOR.split('&')):
    author=name.split(': ')
    di[author[0]]= author[1]
AUTHORS=di


FROM_EMAIL_ADDRESS= os.environ['FROM_EMAIL']
KEYWORDS=['SAAO', 'KELT', 'Infrared Survey']

''''from string environment variables making a list'''
LIBRARIAN_EMAIL_ADDRESSES=os.environ['LIBRARIANS_EMAIL']
email =LIBRARIAN_EMAIL_ADDRESSES.split('&')
LIBRARIAN_EMAIL_ADDRESSES=email
