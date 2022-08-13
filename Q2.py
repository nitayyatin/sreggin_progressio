T = int(input("No, of test cases?\n"))
for n in range(1,T+1):
  List = input("2 Heights?\n").split()
  if int(List[1]) > int(List[0]): print('B')
  else: print('A')