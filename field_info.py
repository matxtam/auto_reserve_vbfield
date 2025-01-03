# This piece of code is used for generate 場單文
import datetime
print("場單文產生器！☆*: .｡. o(≧U≦)o .｡.:*☆")

isQuit = False
isGenerate = False
fieldList = []
year = int(input('請輸入年分： '))
month = int(input('請輸入月份： '))
for day in range(1, 32):
  try:
    date = datetime.datetime(year, month, day)
    if(date.strftime("%w") == '1'):
      fieldList.append({
        'd': day,
        'datestr': date.strftime('%m/%d(一) '),
        '1820': [],
        '2022': []
      })
    if(date.strftime("%w") == '5'):
      fieldList.append({
        'd': day,
        'datestr': date.strftime('%m/%d(五) '),
        '1820': [],
        '2022': []
      })
  except:
    if day <= 10:
      isQuit = True
      print("場單初始化有問題")
    break
print("請輸入中籤場單資訊, 'ok' to print 場單文, 'q' to quit, 'h' to get help.")

def fieldDate(field):
  return field['datestr'][3:5]

while not(isQuit):
  info = input()
  if info=='ok':
    print("【%d月場單】" % month)
    fieldList.sort(key=fieldDate)
    for field in fieldList:
      print(field['datestr'], end='')
      if len(field["1820"]) == 0:
        print('x', end='')
      elif len(field["1820"]) == 1:
        print(field["1820"][0], end='')
      else:
        field["1820"].sort()
        print('(', end='')
        for f in field["1820"]:
          print(f, end='')
        print(')', end='')
      if len(field["2022"]) == 0:
        print('x', end='')
      elif len(field["2022"]) == 1:
        print(field["2022"][0], end='')
      else:
        field["2022"].sort()
        print('(', end='')
        for f in field["2022"]:
          print(f, end='')
        print(')', end='')
      print()

  elif info=='q':
    break
  else:
    # OF20241020037962	排球場 / 排球場 4	2024-11-11 20:00 ~ 22:00
    nothing, info = info.split("排球場 / 排球場")
    place = info[1]
    printed = False
    if str(month) != info[8:10]:
      print("Error: 請輸入%d年%d月的場單資訊！" % (year, month))
      printed = True
    for field in fieldList:
      if printed == True:
        break
      if field['datestr'][3:5] == info[11:13]: # check dd
        print(">>> %d/%s 場 " % (month, field['datestr'][3:5]), end='')
        if info[14] == '2':
          field['2022'].append(info[1])
          print(info[1] + " 下半 added!")
        else:
          field['1820'].append(info[1])
          print(info[1] + " 上半 added!")
        printed = True

    if not printed:
      date = datetime.datetime(year, month, int(info[11:13]))
      weekday = date.strftime('%w')
      datestr = date.strftime('%m/%d(一) ') if weekday=='1' else\
                date.strftime('%m/%d(二) ') if weekday=='2' else\
                date.strftime('%m/%d(三) ') if weekday=='3' else\
                date.strftime('%m/%d(四) ') if weekday=='4' else\
                date.strftime('%m/%d(五) ') if weekday=='5' else\
                date.strftime('%m/%d(六) ') if weekday=='6' else\
                date.strftime('%m/%d(日) ')
      field = {
        'datestr': datestr,
        '1820': [],
        '2022': []
      }
      print("%d/%s 場 " % (month, field['datestr'][3:5]), end='')
      if info[14] == '2':
        field['2022'].append(info[1])
        print(info[1] + " 下半 added!")
      else:
        field['1820'].append(info[1])
        print(info[1] + " 上半 added!")
      fieldList.append(field)


print("掰餔！")