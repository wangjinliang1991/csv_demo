import csv

def write_csv_demo1():
    headers = ['username', 'age', 'height']
    values = [
        ('张三', 18, 180),
        ('李四', 19, 190),
        ('王五', 20, 170)
    ]

    with open('classroom.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(values)

def write_csv_demo2():
    headers = ['username', 'age', 'height']
    values = [
        {'username': '张三', 'age': 18, 'height': 180},
        {'username': '李四', 'age': 19, 'height': 170},
        {'username': '王五', 'age': 20, 'height': 190},
    ]
    with open('classroom1.csv','w', encoding='utf-8', newline='') as fp:
        writer = csv.DictWriter(fp,headers)
        # 写入表头数据的时候需要调用writerheader()方法
        writer.writeheader()
        writer.writerows(values)




if __name__ == '__main__':
    write_csv_demo2()