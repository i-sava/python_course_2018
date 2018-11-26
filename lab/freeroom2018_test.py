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
       '301', '303', '305', '306', '307', '307a', '307б', '309', '310',
       '313', '316', '318',  '320', '322', '324', '325',
       '402', '403', '404',  
        }

dict_room_free = {1: room, 2: room, 3: room, 4: room, 5: room, 6: room, 7: room}

groups = {'ПМ-11(к)','ПМ-12(к)', 'СМ-6', 'ІСТ-1', 'СО(М)(з)11', 'ПМ-2', 'СО(М)-2', 'СО(І)-5м',
          'ІНФ-42', 'ПМк-41', 'М(ас)-11', 'ПМ-4', 'КН-21', 'МАТ-32', 'І(з)-41', 'МАТ-41',
          'КН(з)-11', 'ІНФ-41', 'См-5', 'ПМ к- 31', 'ПМ к- 31','ПМ к- 41',  'СОМ-5м', 'СО(І)(з)11', 'С-3',
          'ПМ-3', 'М(ас)-21', 'С-4', 'ПМк-21', 'СО(І)-1', 'СОМ(І)(з)6', 'КН-11', 'КН-52м',
          'СОМ(М)(з)6', 'ІПЗ-1', 'ІПЗ-2', 'ІПЗ-3', 'СО(М)-1', 'Ст-2', 'ПМ-1', 'М(докт)-1', 'СО(І)-5м.', 'ПМ-51',
          'МАТ-31', 'М(докт)-2', 'ПМ-52м', 'М-52м', 'СО(І)-2', 'СО(І)(з)21', 'М-2', 'СОМ(М)(з)-',
          'ПІ-3', 'І(з)-31', 'МАТ-42', 'КН(з)-21', 'ІНФ-32', 'ІС(з)-11', 'СО(М)(з)21', 'М-51',
          'ПМ-12(к)', 'СОМ(І)(з)5', 'Ст-1', 'ПМк-22', 'КН-51м', 'КН-22', 'М-1', 'ІНФ-31',
          'ІСТ-2', 'СО(М)-3', 'СО(І)-3',
          'КН-1', 'КН-2', 'КН-31', 'КН-32', 'КНМ-1', 'КНМ-2', 
	  'ІСТ-1', 'ІСТ-2',
	  'ПММ -1', 'ПММ-1', 'ПММ-2',
	  'М -2', 'М - 41', 'М - 42',
          'ММа-1', 'ММк-1', 'СОМ(М)-1', 'СОМ(І)-1',
          'СМ -2', 'СОМ(М)-2', 'СОМ (І)-2',
          'ПІ-4', 'І-4',  'СО(I)-1', 'М-3',
          'С-3',
          'ПМ(к)-11', 'ПМ(к)-12', 'ПМ-21(к)', 'ПМ-22(к)', 'ПМ к- 31', 'ПМ к- 32', 'ПМ к- 41'
          }


sdate = input("Введіть дату у форматі [18.10.2017] = ")

if sdate == '':
      today = date.today()  
      sdate = today.strftime("%d.%m.%y")
      edate = today.strftime("%d.%m.%y")
else:
      edate = sdate

group = 'ПММ-2'

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



#flag = int(input("Виводити прізвище викладача [так=1, ні=0] ?"))
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
    print("|{} | вільні : {}|".format(k, ',  '.join(sorted(f))))
    print("")
   




