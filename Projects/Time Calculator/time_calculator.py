def add_time(start, duration, day=None):
  lst1=start.split()
  dayni=lst1[1]
  if dayni=='PM':
    dayni=1
  else:
    dayni=0
  t=lst1[0].split(':')
  starthour=float(t[0])
  if dayni==1:
    starthour+=12
  startmin=float(t[1])
  
  t2=duration.split(':')
  durhour=float(t2[0])
  durmin=float(t2[1])

  minty=int(startmin+durmin)
  if minty>=60:
    starthour+=(minty//60)
    minty=(minty%60)
  if minty<10:
    minty='0'+str(minty)
  
  toty=int(starthour+durhour)
  daytrack=int(toty//24)
  toty=toty%24
  
  dayni='AM'
  if toty>=12:
    dayni='PM'
    toty-=12
  if toty<1:
    toty=12
  if daytrack==0:
    daylate=''
  elif daytrack==1:
    daylate=' (next day)'
  elif daytrack>1:
    daylate=" ("+str(daytrack)+" days later)"
  if day==None:
    d=''
  if day!=None:
    Week=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    a=day.capitalize()
    b=Week.index(a)
    b+=1+daytrack
    c=b%7-1
    d=", "+Week[c]
  if daytrack==0 and day==None:
    new_time=str(toty)+':'+str(minty)+" "+dayni
  if daytrack>0 or day!=None:
    new_time=str(toty)+":"+str(minty)+" "+dayni+d+daylate
  return new_time