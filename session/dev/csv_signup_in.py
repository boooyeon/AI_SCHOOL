from google.colab import drive
drive.mount('/content/gdrive')

# %cd /content/gdrive/My\ Drive/'Colab Notebooks'/
# !ls

import csv
import os
file = '/content/gdrive/My Drive/Colab Notebooks/a.csv'

if os.path.isfile(file) == False:
  with open(file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["user_id", "user_pw"]) 

def write_id(user_id,user_pw):
  with open(file, 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([user_id, user_pw])  

def id_check(user_id):
  with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for i in csvreader:
      if (user_id == i[0]):
        print(f"{i[0]} 아이디가 중복되었습니다. 다시해주세요")
        return False
  return True

while (True):
  x = input("로그인/회원가입: ")
  if ( x == "회원가입"):
    n = False # 중복 여부
    while (n == False):
      user_id = input("아이디를 입력하세요: ")
      if(id_check(user_id) == True):
        user_pw = input("비밀번호를 입력하세요: ")
        write_id(user_id,user_pw)
        print(f"{user_id}가 정상생성되었습니다")
        n = True
    
  elif (x=="로그인"):
    user_id = input("아이디를 입력하세요: ")
    user_pw = input("비밀번호를 입력하세요: ")
    user_list = [user_id, user_pw]
    user_check = 0 
    with open(file, 'r') as csvfile:
      csvreader = csv.reader(csvfile)
      for i in csvreader:
        if (user_list == i):
          user_check = 1
          print("로그인 되었습니다.")
          break
      if user_check == 0:
          print("로그인 실패")
    csvfile.close()
  else:
    print("다시 입력하세요")

        
     
      
# while (True):
#   x = input("로그인/회원가입: ")
#   if ( x == "회원가입"):
#     n = False # 중복 여부
#     while (n == False):
#       user_id = input("아이디를 입력하세요: ")
#       with open(file, 'r') as csvfile:
#         csvreader = csv.reader(csvfile)
#         for i in csvreader:
#           if (user_id == i[0]):
#             print(f"{i[0]} 아이디가 중복되었습니다. 다시해주세요")
#           elif (user_id != i[0]):
#             n = True

#     if (n == True):
#       user_pw = input("비밀번호를 입력하세요: ")
#       write_id(user_id,user_pw)
#       print(f"{user_id}아이디 정상 생성 완료")