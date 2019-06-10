# 使用PyMySQL操作mysql数据库

from datetime import date, datetime, timedelta
import pymysql.cursors

# 连接配置信息
config = {
    'host': '192.168.1.106',
    'port': 3306,
    'user': 'root',
    'password': 'qweqwe123',
    'db': 'test',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}
# 创建连接
connection = pymysql.connect(**config)

# 获取明天的时间
tomorrow = datetime.now().date() + timedelta(days=1)

# 执行sql语句
try:
    with connection.cursor() as cursor:
        # 执行sql语句，插入记录
        sql = 'INSERT INTO student1 (id, name, sex, birth, department, address) VALUES (%s, %s, %s, %s, %s, %s)'
        cursor.execute(sql, ('907', '李七', '女', '1990', '中文系', '东北省大连市'));
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()

finally:
    connection.close();