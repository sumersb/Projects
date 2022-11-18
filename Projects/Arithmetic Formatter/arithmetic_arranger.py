def arithmetic_arranger(problems,T=False):
  if len(problems)>5:
    return 'Error: Too many problems.'
  else:
    line1=''
    line2=''
    line3=''
    line4=''
    for i in problems:
      operation=0
      if '+' in i:
        lstProblem=i.split('+')
        operation=1
      elif '-' in i: 
        lstProblem=i.split('-')
        operation=-1
      else: return "Error: Operator must be '+' or '-'."

      try:
          firstNum=int(lstProblem[0])
          secondNum=int(lstProblem[1])
      except:
          return 'Error: Numbers must only contain digits.'
      long=max(len(str(firstNum)),len(str(secondNum)))
      if long>4:
        return 'Error: Numbers cannot be more than four digits.'
      
      line1+=" "*2+(long-len(str(firstNum)))*' '+str(firstNum)
      
      if operation==1:
        total=firstNum+secondNum
        line2+='+ '
      else: 
        line2+='- '
        total=firstNum-secondNum
      line2+=(long-len(str(secondNum)))*' '+str(secondNum)

      line3+='-'*(long+2)

      line4+=(long+2-len(str(total)))*' '+str(total)

      if i!=problems[-1]:
        line1+=' '*4
        line2+=' '*4
        line3+=' '*4
        line4+=' '*4
      
    if T==False:
      arranged_problems=line1+'\n'+line2+'\n'+line3
      
    else:
      arranged_problems=line1+'\n'+line2+'\n'+line3+'\n'+line4
      
          
    return arranged_problems