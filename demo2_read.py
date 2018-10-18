import csv

def read_csv_demo1():
    with open('classroom.csv', 'r', encoding='utf-8') as fp:
        # reader是一个迭代器
        reader = csv.reader(fp)
        # 不想要标题，next()
        next(reader)
        for x in reader:
            name = x[0]
            height = x[-1]
            print({'name': name, 'height': height})


def read_csv_demo2():
    with open('classroom.csv', 'r',encoding='utf-8') as fp:
        reader = csv.DictReader(fp)
        for x in reader:
            value = {'name':x['username'],'height':x['height']}
            print(value)

if __name__ == '__main__':
    read_csv_demo2()