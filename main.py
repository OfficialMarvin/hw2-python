# Author: Marvin Jakobs mkj5388@psu.edu

def getGradePoint(letter):
  if(letter == "A"):
    return 4.0
  elif(letter == "A-"):
    return 3.67
  elif(letter == "B+"):
    return 3.33
  elif(letter == "B"):
    return 3.0
  elif(letter == "B-"):
    return 2.67
  elif(letter == "C+"):
    return 2.33
  elif(letter == "C"):
    return 2
  elif(letter == "D"):
    return 1.0
  else:
    return 0.0

def run():
  gp1 = getGradePoint(input("Enter your course 1 letter grade: "))
  c1 = float(input("Enter your course 1 credit: "))
  print("Grade point for course 1 is: "+ str(float(gp1)))
  gp2 = getGradePoint(input("Enter your course 2 letter grade: "))
  c2 = float(input("Enter your course 2 credit: "))
  print("Grade point for course 2 is: "+ str(float(gp2)))
  gp3 = getGradePoint(input("Enter your course 3 letter grade: "))
  c3 = float(input("Enter your course 3 credit: "))
  print("Grade point for course 3 is: "+ str(float(gp3)))
  
  GPA = ((gp1*c1)+(gp2*c2)+(gp3*c3))/(c1+c2+c3)

  print("Your GPA is: " + str(GPA))
  

if __name__ == "__main__":
  run()