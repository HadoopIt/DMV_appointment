# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 11:27:10 2014

@author: HadoopIt
"""

from bs4 import BeautifulSoup
import os
import requests
import datetime

output_folder = os.getcwd() # set the folder in which you want to place the output file
test_in_days = 10           # looking for behind-the-wheel driving test within the next 'test_in_days' days
first_name = ''             # Your first name in CAPITAL letter
last_name = ''              # Your last name in CAPITAL letter
dl_number = ''              # Your driving permit number
tel_area = ''               # 3 digits: (650)xxx-xxxx
tel_prefix = ''             # 3 digits: (xxx)123-xxxx
tel_suffix = ''             # 4 digits: (xxx)xxx-4567
birth_month = ''            # e.g. 05
birth_day = ''              # e.g. 06
birth_year = ''             # e.g. 1990

# appointment for behind-the-wheel test
test_url = 'https://www.dmv.ca.gov/wasapp/foa/findDriveTest.do'
# appointment for office visit
#test_url = 'https://www.dmv.ca.gov/wasapp/foa/findOfficeVisit.do'

# for complete DMV office list, please go to the below address, and view page source in your browser
# https://www.dmv.ca.gov/foa/clear.do?goTo=driveTest&localeName=en
OFFICES = {
    'REDWOOD': '548',
    'SAN MATEO': '593',
    'SANTA CLARA': '632',
}

def main():
    post_info = dict()
    try:
        for oname, oid in OFFICES.iteritems():
            post_info['numberItems'] = '1'
            post_info['resetCheckFields'] = 'true'   
            post_info['requestedTask'] = 'DT'
            post_info['officeId'] = oid
            
            post_info['firstName'] = first_name     
            post_info['lastName'] = last_name       
            post_info['dlNumber'] = dl_number  
            post_info['telArea'] = tel_area        
            post_info['telPrefix'] = tel_prefix      
            post_info['telSuffix'] = tel_suffix     
            post_info['birthMonth'] = birth_month      
            post_info['birthDay'] = birth_day        
            post_info['birthYear'] = birth_year               
            
            earliest = get_earliest_appointment(post_info)
            if earliest:
                earlist_datetime = datetime.datetime.strptime(earliest, '%A, %B %d, %Y at %I:%M %p')
                triger_datetime = datetime.datetime.now() + datetime.timedelta(days=test_in_days)
                if (earlist_datetime < triger_datetime):
                    filename = "%s/DMV_%s_%s.txt" % (output_folder, oname, earlist_datetime.strftime("%Y-%m-%d"))
                    f = open(filename, 'w')
                    f.write(earliest)
                    f.close()
                    print 'The earliest appointment in %s is on %s' % (oname, earliest)
                else:
                    print 'No available test slot in %s within the next %d days.' % (oname, test_in_days)
        return 0
    except:
        return 1


def get_earliest_appointment(data):
    r = requests.post(test_url, data = data)
    soup = BeautifulSoup(r.content)
    for p in soup.find_all('p', 'alert'):
        if not p.text.startswith('The first available appointment'):
            return p.text


if __name__ == '__main__':
    main()