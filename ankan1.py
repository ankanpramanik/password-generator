import random as ran

n=int(input("Enter the length of your password (max 16 char): "))


if n<=16:
  alphaupper1=chr(ran.randint(65,90))
  alphaupper2=chr(ran.randint(65,90))
  alphaupper3=chr(ran.randint(65,90))
  alphaupper4=chr(ran.randint(65,90))
  alphalower1=chr(ran.randint(97,122))
  alphalower2=chr(ran.randint(97,122))
  alphalower3=chr(ran.randint(97,122))
  alphalower4=chr(ran.randint(97,122))
  num1=chr(ran.randint(48,57))
  num2=chr(ran.randint(48,57))
  num3=chr(ran.randint(48,57))
  num4=chr(ran.randint(48,57))
  splchar1=chr(ran.randint(33,47))
  splchar2=chr(ran.randint(33,47))
  splchar3=chr(ran.randint(33,47))
  splchar4=chr(ran.randint(33,47))

  def shuffle(string):
    tempList = list(string)
    ran.shuffle(tempList)
    return ''.join(tempList)

# adding comments for better readability
#creating password according to  the following combination
  password=alphaupper1+alphaupper2+alphalower2+alphalower1+num1+num2+splchar1+splchar2+alphaupper3+alphaupper4+alphalower3+alphalower4+num3+num4+splchar3+splchar4

#shuffling the password in random order and then cutting out the first n char 
  
  password=shuffle(password)
  pw=password[:n]

#Adding feature so that no password starts with any special character 

  if chr(33)<=pw[0]<=chr(47):
    while chr(33)<=pw[0]<=chr(47):
        pw=shuffle(pw)
        continue
  print("Your suggested password is:",pw)
 
  
  if len(pw)<8:
    print("Strenth: Weak")
  elif len(pw)==8:
    print("Strenth: Moderate")
  elif len(pw)>8:
    print("Strenth: Strong")

else:
  print("Wrong input")

