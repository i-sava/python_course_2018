#!/usr/bin/env python3
# -*- coding: cp1251 -*-

#pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
from datetime import date



dict_room = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set()}




dict_room_2 = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set()}


room = {
       '207', '229', '230', '231', '232',  '234',
       '301', '303', '305', '306', '307', '307a', '307�', '309', '310',
       '313', '316', '318',  '320', '322', '324', '325',
       '402', '403', '404',  
        }

dict_room_free = {1: room, 2: room, 3: room, 4: room, 5: room, 6: room, 7: room}

groups = {'��-11(�)','��-12(�)', '��-6', '���-1', '��(�)(�)11', '��-2', '��(�)-2', '��(�)-5�',
          '���-42', '���-41', '�(��)-11', '��-4', '��-21', '���-32', '�(�)-41', '���-41',
          '��(�)-11', '���-41', '��-5', '�� �- 31', '�� �- 31','�� �- 41',  '���-5�', '��(�)(�)11', '�-3',
          '��-3', '�(��)-21', '�-4', '���-21', '��(�)-1', '���(�)(�)6', '��-11', '��-52�',
          '���(�)(�)6', '���-1', '���-2', '���-3', '��(�)-1', '��-2', '��-1', '�(����)-1', '��(�)-5�.', '��-51',
          '���-31', '�(����)-2', '��-52�', '�-52�', '��(�)-2', '��(�)(�)21', '�-2', '���(�)(�)-',
          'ϲ-3', '�(�)-31', '���-42', '��(�)-21', '���-32', '��(�)-11', '��(�)(�)21', '�-51',
          '��-12(�)', '���(�)(�)5', '��-1', '���-22', '��-51�', '��-22', '�-1', '���-31',
          '���-2', '��(�)-3', '��(�)-3',
          '��-1', '��-2', '��-31', '��-32', '���-1', '���-2', 
	  '���-1', '���-2',
	  '��� -1', '���-1', '���-2',
	  '� -2', '� - 41', '� - 42',
          '���-1', '���-1', '���(�)-1', '���(�)-1',
          '�� -2', '���(�)-2', '��� (�)-2',
          'ϲ-4', '�-4',  '��(I)-1', '�-3',
          '�-3',
          '��(�)-11', '��(�)-12', '��-21(�)', '��-22(�)', '�� �- 31', '�� �- 32', '�� �- 41'
          }


sdate = input("������ ���� � ������ [18.10.2017] = ")

if sdate == '':
      today = date.today()  
      sdate = today.strftime("%d.%m.%y")
      edate = today.strftime("%d.%m.%y")
else:
      edate = sdate

group = '���-2'

url = "http://asu.pnu.edu.ua/cgi-bin/timetable.cgi"
headers = {'Content-Type': 'text/html; charset=windows-1251'}

data = {'group': group.encode('cp1251'), 'sdate': sdate, 'edate': edate}


r = requests.post(url, headers=headers, data = data )

print(r)
r.encoding = 'cp1251'
#print(r.text)
#print(r.content)

soup = BeautifulSoup(r.text, "html.parser")

#tab = soup.find('table', class_='table table-bordered table-striped')
rows = soup.find_all('tr')

#print(rows[1])

for row in rows:
    cols = row.find_all('td')
    #print(cols[2].text.split()[0], cols[2].text.split()[1],)
    
    if cols[2].text:
        number_line = int(cols[0].text)
        line_list = cols[2].text.split()
        elem_room = str(cols[2].text.split()[0])
        
        #room.discard(elem_room)
        
        #print(number_line, elem_room, cols[2].text)
        dict_room[number_line].add(elem_room)
   

#print(dict_room)



 

##for tag in soup.find_all(True):
##    print(tag.name)

#input()



#flag = int(input("�������� ������� ��������� [���=1, �=0] ?"))
flag = 0
#print("For date = ", edate, 'flag=', flag)      



for group in groups:
      #print(groups, end=' ')
      r = requests.post(url, headers=headers, data = {'group': group.encode('cp1251'), 'sdate': sdate,
                                                      'edate': edate, 'n': '700'})
      r.encoding = 'cp1251'

      soup = BeautifulSoup(r.text, "html.parser")
      #tab = soup.find('table', class_='table table-bordered table-striped')
      rows = soup.find_all('tr')
       
       

            
      if rows:
            #rows = table.find_all('tr')
            #rows = table
            for row in rows:
                  cols = row.find_all('td')
                  if cols[0]:
                        index = int(rows.index(row))
                        number_line = index + 1
                        #number_line = int(cols[0].text.split()[0])
                        #print(number_line, cols[2].text)

                      
                        if cols[2].text:
                              elem_room = cols[2].text.split()[0] 
                              elem_room_2 = elem_room +'('+ cols[2].text.split()[1]+')'  
                        else:
                              elem_room = ''
    
                                  
                        
                        if elem_room:                                                     
                              #room.add(elem_room)
                              dict_room[number_line].add(elem_room)
                              dict_room_2[number_line].add(elem_room_2)
                              #print(number_line,"-->" ,elem_room)
   


for k in range(1,7):
    print("|{}| \n  {}".format(k, ', \n  '.join(sorted(dict_room_2[k]))))
    f = dict_room_free[k].difference(dict_room[k])
    #print(f)
    print("|{} | ���� : {}|".format(k, ',  '.join(sorted(f))))
    print("")
   




