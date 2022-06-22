##Lillian Puckett and Kezia Boyce
#Mad libs quest
num = int(input("Choose a number from 1-4: "))

while num == 1:
  print(" A story of a person who goes on vacation to a faraway place.")
  ans1= str(input("Would you like to write this story?:\n (Yes)(No)"))
  if str(ans1)==("yes"):
   import part1
   num=[]  
  elif str(ans1)==("no"):
    num = int(input("Choose a number from 1-4:"))
  else:
    ans1 = input("Enter yes or no:")
  



while num == 2:
  print("A summary of your favorite book.")
  ans1= str(input("Would you like to write this story?:\n (Yes)(No)"))
  if str(ans1)==("yes"):
    import part2
    num = []
  elif str(ans1)==("no"):
    num = int(input("Choose a number from 1-4:"))
  else: 
    ans1= input("Enter yes or no:")



while num == 3:
  print("A person goes to the zoo and talks to one of the animals. ")
  ans1= str(input("Would you like to write this story?:\n (Yes)(No)"))
  if str(ans1)==("yes"):
    import part3
    num=[]
  elif str(ans1)==("no"):
    num = int(input("Choose a number from 1-4:"))
  else:
    ans1= input("Enter yes or no:")

while num == 4:
  print("A review about a well known tourist destination ")
  ans1= str(input("Would you like to write this story?:\n (Yes)(No)"))
  if str(ans1)==("yes"):
    import part4
    num=[]
  elif str(ans1)==("no"):
    num = int(input("Choose a number from 1-4:"))
  else:
    ans1= input("Enter yes or no:")
  