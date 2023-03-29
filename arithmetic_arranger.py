def arithmetic_arranger(problems, result=False):
  if len(problems) > 5:
    return "Error: Too many problems."
  first = list()
  operator = list()
  second = list()
  for i in problems:
    i = i.split()
    first.append(i[0])
    operator.append(i[1])
    second.append(i[2])
  if "*" in operator or "/" in operator:
    return "Error: Operator must be '+' or '-'."
  for numero in first:
    if not numero.isdigit():
      return "Error: Numbers must only contain digits."
  for numero in second:
    if not numero.isdigit():
      return "Error: Numbers must only contain digits."
  for numero in first:
    if len(numero) > 4:
      return "Error: Numbers cannot be more than four digits."
  for numero in second:
    if len(numero) > 4:
      return "Error: Numbers cannot be more than four digits."
  arranged_problems = list()
  operazione = list()
  #controllo del risultato
  op = 0
  num1 = 0
  num2 = 0
  for i in range(len(problems)):
    num1 = int(first[i])
    num2 = int(second[i])
    if "+" in operator[i]:
      op = num1 + num2
      operazione.append(op)
    if "-" in operator[i]:
      op = num1 - num2
      operazione.append(op)


#----------------------------------------
  primo = ""
  sign = ""
  secondo = ""
  risultato = ""
  high = ""
  bottom = ""
  bottom1 = ""
  linea = ""
  totale = ""
  for indice in range(len(problems)):
    primo = first[indice]
    sign = operator[indice]
    secondo = second[indice]
    if result is True:
      risultato = str(operazione[indice])
    lunghezza = max(len(primo), len(secondo)) + 2
    high += primo.rjust(lunghezza) + (4 * " ")
    bottom = sign + secondo.rjust(lunghezza - 1)
    bottom1 = bottom1 + bottom + (4 * " ")
    linea += len(bottom) * "-"+ (4*" ")
    totale += risultato.rjust(lunghezza) + (4*" ")
  print(high)
  print(bottom1)
  print(linea)
  print(totale)
  #return arranged_problems
