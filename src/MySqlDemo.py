import pymysql


# 连接数据库测试
def connect_db():
    # 打开数据库连接  localhost ; 数据库用户名 数据库密码 数据库名称（自建已建）
    db = pymysql.connect("127.0.0.1", "root", "1234", "db_i_t_push_test")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    print("Database version : %s " % data)
    # 关闭数据库连接
    db.close()


# 创建一个表
def creat_tb():
    # 链接数据库
    db = pymysql.connect("localhost", "root", "1234", "db_i_t_push_test")
    # 获得游标
    cursor = db.cursor()
    # 使用excute()方法执行SQL ,如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    # 使用欲处理语句 创建表
    creatTB = """CREATE TABLE EMPLOYEE (ID INT  auto_increment primary key,FIRST_NAME CHAR(20) NOT NULL  ,LAST_NAME CHAR(20),AGE INT ,SEX CHAR(1) ,INCOME FLOAT )"""
    cursor.execute(creatTB)


# 插入一条数据
def insertData():
    # 连接数据库
    db = pymysql.connect("127.0.0.1", "root", "1234", "db_i_t_push_test")
    # 获得游标
    cursor = db.cursor()

    # 方式一、 SQL语句插入
    # insert = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) VALUES ('xiao','mi',10,'W',200000)"""
    # sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
    #          LAST_NAME, AGE, SEX, INCOME)
    #          VALUES ('小米', 'Mohan', 20, 'M', 2000)"""

    # 方式二、SQL 插入语句
    sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('%s', '%s',  %s,  '%s',  %s)" % (
        'Mac', 'Mohan', 20, 'M', 2019)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


# 查询所有
def queryAll():
    # 连接数据库
    db = pymysql.connect("127.0.0.1", "root", "1234", "db_i_t_push_test")
    # 获得游标
    cursor = db.cursor()

    sql = """SELECT * FROM EMPLOYEE WHERE INCOME > 1000"""

    try:
        # 执行SQL语句
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            id = row[0]
            fname = row[1]
            lname = row[2]
            age = row[3]
            sex = row[4]
            income = row[5]
            print("id = %s ,fname=%s ,lname=%s ,age=%s ,sex=%s ,income=%s " % (id, fname, lname, age, sex, income))
    except:
        db.rollback()
    db.close()


# 更新数据
def update():
    # 连接数据库
    db = pymysql.connect("127.0.0.1", "root", "1234", "db_i_t_push_test")
    # 获得游标
    cursor = db.cursor()
    sql = "UPDATE EMPLOYEE SET AGE =25 WHERE SEX = '%s'" % ('M')
    # sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


# 删除数据
def delete():
    db = pymysql.connect("127.0.0.1", "root", "1234", "db_i_t_push_test")
    cursor = db.cursor()

    sql = "DELETE FROM EMPLOYEE WHERE AGE >'%s'" % 20

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


# 测试链接数据库
# connect_db()
# 创建一个表
# creat_tb()
# 插入一条数据
# insertData()
# 查询所有数据
# queryAll()
# 更新数据
# update()
# 删除数据
delete()
