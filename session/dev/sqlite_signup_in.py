import sqlite3
import os

# os.chdir(r"C:\Users\HERIUN\Downloads")
# conn = sqlite3.connect('a.db')

def connect_db():
  conn = sqlite3.connect('a.db')
  cur = conn.cursor()
  return conn,cur

def close_db(conn):
  conn.commit()
  conn.close()

def create_table_user():
  conn, cur = connect_db()
  cur.execute("""CREATE TABLE if not exists user(
                id text primary key,
                pw text)""")
  close_db(conn)

def add_user(user_id,user_pw):
  conn,cur = connect_db()
  write_sql = "INSERT INTO USER VALUES(?,?);"
  x = [user_id,user_pw]
  cur.execute(write_sql,x)
  cur.execute("SELECT * FROM USER;")
  res = cur.fetchall()
  print(res)
  close_db(conn)


def id_check(user_id):
  conn,cur = connect_db()
  cur.execute("SELECT ID FROM USER;")
  res = cur.fetchall()
  for i in res:
      if(user_id == i[0]):
        print(f"{i[0]} 아이디가 중복되었습니다. 다시해주세요")
        close_db(conn)
        return False
  close_db(conn)
  return True

def login_user(user_id,user_pw):
  conn, cur = connect_db()
  cur.execute("SELECT * FROM USER;")
  res = cur.fetchall()
  user = [user_id,user_pw]
  for i in res:
    if user[0] == i[0] and user[1] == i[1]:
      return True
  return False

def after_login(user_id):
  a = 0
  while(a==0):
    a=input("계속: 0, 로그아웃: 1 :")
    if(a == 1):
      return False
    return True

create_table_user()

while (True):
  x = input("로그인/회원가입: ")
  if ( x == "회원가입"):
    n = False # 중복 여부
    while (n == False):
      user_id = input("아이디를 입력하세요: ")
      if(id_check(user_id) == True):
        user_pw = input("비밀번호를 입력하세요: ")
        add_user(user_id,user_pw)
        print(f"{user_id}가 정상생성되었습니다")
        n = True
    
  elif (x=="로그인"):
    user_id = input("아이디를 입력하세요: ")
    user_pw = input("비밀번호를 입력하세요: ")
    if (login_user(user_id, user_pw) == True):
      print(f"{user_id}님이 로그인 하셨습니다")
      while(True):
        if(after_login(user_id)==False):
          break
    else:
      print("id 혹은 비밀번호가 일치하지 않습니다.")

  else:
    print("다시 입력하세요")
