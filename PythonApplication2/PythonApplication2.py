# -*- coding: cp1251 -*-

import pickle
from flask import Flask,request,jsonify
app = Flask(__name__)
cars = []
books = []
# ��������� ���� � �������
try:
    with open('cars.data', 'rb') as filehandle: 
        cars = pickle.load(filehandle)
except:
    with open('cars.data', 'wb') as filehandle:
        pickle.dump(' ', filehandle)


# ��������� ���� � �������
try:
    with open('books.data', 'rb') as filehandle: 
        books = pickle.load(filehandle)
except:
    with open('books.data', 'wb') as filehandle:
        pickle.dump(' ', filehandle)

# ������ POST, GET
@app.route('/book',methods=['POST','GET'])
def bookPostAndGet():
    if request.method == 'POST':
        data = request.get_json()
        author = None
        title = None
        release = None
        edition = None
        if data:
            if 'title' in data:
                title = data['title']
            else:
                return '������� �������� �����', 403
            if 'edition' in data:
                edition = data['edition']
            else:
                return '������� ������� �����', 403
            if 'author' in data:
                author = data['author']
            else:
                return '������� ������ �����', 403
            if 'release' in data:
                release = data['release']
            else:
                return '������� ���� ������ �����', 403
        else:
            return '������� ������ �����', 403
        book = []  
        book.append(title)
        book.append(edition)
        book.append(author) 
        book.append(release)         
        books.append(book)
        # ��������� ���� � �������
        saveBooksToFile()
        return "����� ������� ���������",200
    if request.method =="GET":
        return books,200
# ������ DELETE, PUT
@app.route('/book/<int:id>',methods=['DELETE', 'PUT'])
def userPutAndDelete(id):
    if request.method =='DELETE':
        try:
            del books[id]
            return "����� �������� �������",200
        except:
            return "����������� ������",403
    if request.method =='PUT':
        if len(books) < id:
            return '����� � ����� id ���� � �����', 403
        data = request.get_json()
        if data:
            if 'title' in data:
                title = data['title']
            else:
                return '������� �������� �����', 403
            if 'edition' in data:
                edition = data['edition']
            else:
                return '������� �������', 403
            if 'author' in data:
                author = data['author']
            else:
                return '������� ������ �����', 403
            if 'release' in data:
                release = data['release']
            else:
                return '������� ���� ������ �����', 403
        else:
            return '������� ������ �����', 403
        book = [] 
        book.append(release)         
        book.append(author) 
        book.append(title)
        book.append(edition)
        books[id] = book  
        saveBooksToFile()
        return '����� ������� ��������', 200

    # ��������� ���� � �������
def saveBooksToFile():
    with open('books.data', 'wb') as filehandle:
        pickle.dump(books, filehandle)



@app.route('/cars',methods=['POST','GET'])
def musicPostAndGet():
    if request.method == 'POST':
        data = request.get_json()
        brandCar = None
        releaseCar = None
        modelCar = None
        countryCar = None
        if data:
            if 'brandCar' in data:
                brandCar = data['brandCar']
            else:
                return '�� ������� ����� ����', 403
            if 'releaseCar' in data:
                releaseCar = data['releaseCar']
            else:
                return '�� ������� ���� ������� ����', 403
            if 'modelCar' in data:
                modelCar = data['modelCar']
            else:
                return '�� ������� ������ ����', 403
            if 'countryCar' in data:
                countryCar = data['countryCar']
            else:
                return '�� ������� ������ ����', 403
            
            
        else:
            return '��� ������', 403
        car = []  
        car.append(brandCar) 
        car.append(releaseCar)         
        car.append(modelCar) 
        car.append(countryCar)
        cars.append(car)   
        saveCars()
        return "������ ���������",200
    if request.method =="GET":        
        return cars,200        
@app.route('/cars/<int:id>',methods=['DELETE', 'PUT'])

def musicPutAndDelete(id):
    if request.method =='DELETE':
        try:
            del cars[id]
            return "������ �������",200
        except:
            return "������ ��������",403

    if request.method =='PUT':
        if len(cars) < id:
            return '������ � ����� id ���', 403

        data = request.get_json()
        if data:
            if 'brandCar' in data:
                brandCar = data['brandCar']
            else:
                return '�� ������� ����� ����', 403
            if 'releaseCar' in data:
                releaseCar = data['releaseCar']
            else:
                return '�� ������� ���� ������� ����', 403
            if 'modelCar' in data:
                modelCar = data['modelCar']
            else:
                return '�� ������� ������ ����', 403
            if 'countryCar' in data:
                countryCar = data['countryCar']
            else:
                return '�� ������� ������ ����', 403
            
        else:
            return '��� ������', 403
            
        car = []  
        car.append(brandCar) 
        car.append(releaseCar)         
        car.append(modelCar) 
        car.append(countryCar)
        cars[id] = car  
        saveCars()
        return "������ ��������",200



def saveCars():
    with open('cars.data', 'wb') as filehandle:
        pickle.dump(cars, filehandle)






app.run(port=3005)


