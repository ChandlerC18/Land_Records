
URL = {'norfolk' : 'http://www.norfolkresearch.org/ALIS/WW400R.HTM?WSIQTP=SY14D&WSKYCD=T'}

address = input('Enter an address: ')
search_url = f'http://www.norfolkresearch.org/ALIS/WW400R.HTM?W9PADR={address.replace(' ', '+')}&W9ABR=*ALL&W9TOWN=WELL&W9FDTA=&W9TDTA=&WSHTNM=WW414R00&WSIQTP=SY14AP&WSKYCD=T&WSWVER=2#schTerms'
