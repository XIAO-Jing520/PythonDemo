import sqlite3
cx = sqlite3.connect("./test.db")
cu = cx.cursor()
# cu.execute(
#   'create table token2name (imgtoken  CHAR(32) primary key,name  varchar(10)); ')
#cu.execute(
#   "insert into token2name values('61a2e1b2bb3d8c75e60859dfd43ef599', '刘德华')")
#cx.commit()

cu.execute("select name from token2name")
print(cu.fetchall())
