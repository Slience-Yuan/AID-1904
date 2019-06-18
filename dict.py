import pymysql

filename = "/home/tarena/1904/dict.txt"
fd = open(filename)

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     database='dict',
                     charset='utf8')

cur = db.cursor()

for line in fd:
    if not line:
        break
    data = line.split(' ')
    word = data[0]
    means = ' '.join(data[1:]).lstrip()
    try:
        sql = "insert into words (word,means) values (%s,%s);"
        cur.execute(sql, [word, means])
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
fd.close()
cur.close()
db.close()
