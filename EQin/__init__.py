
# 配置
DBNAME = 'test'
USERNAME = 'root'
password = 'kkuu9038'
host = '127.0.0.1'
port = '3306'


import pymysql
pymysql.install_as_MySQLdb()

# 打开数据库连接
db = pymysql.connect(host,USERNAME,password,DBNAME)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据库
data = cursor.fetchone()

# 关闭数据库
db.close()