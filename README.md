**Тестирование API**

1. POST <http://127.0.0.1:3005/book>

Body: JSON

{

"title":"Mertvie dyshi",

"edition":"Mertvie dyshi",

"author":"Gogol",

"release": "23.21.1000"

}

` `![](https://github.com/cahashih/PiTPM_task_two/blob/master/Screens/Aspose.Words.e05d7563-d410-43e7-a04f-026977fd0751.001.png)

Выдаваемая информация: Книга успешно добавлена, 200

1. GET <http://127.0.0.1:3005/book>

![](https://github.com/cahashih/PiTPM_task_two/blob/master/Screens/Aspose.Words.e05d7563-d410-43e7-a04f-026977fd0751.002.png)

Выдаваемая информация: Все книги, 200

1. DELETE http://127.0.0.1:3005/book/0

![](https://github.com/cahashih/PiTPM_task_two/blob/master/Screens/Aspose.Words.e05d7563-d410-43e7-a04f-026977fd0751.003.png)

Выдаваемая информация: Книга успешно удалена, 200

1. PUT <http://127.0.0.1:3005/book/0>

Body: JSON

{

"title":"Mertvie dyshi2",

"edition":"Mertvie dyshi2",

"author":"Gogol2",

"release": "11.11.1111"

}

![](https://github.com/cahashih/PiTPM_task_two/blob/master/Screens/Aspose.Words.e05d7563-d410-43e7-a04f-026977fd0751.004.png)

Выдаваемая информация: Книга успешно изменена, 200

1. POST http://127.0.0.1:3005/cars

Body: JSON

{

`    `"brandCar":"VAZ",

`    `"releaseCar":"2000",

`    `"modelCar":"2109",

`    `"countryCar": "Russia"

}

![](https://github.com/cahashih/PiTPM_task_two/blob/master/Screens/Aspose.Words.e05d7563-d410-43e7-a04f-026977fd0751.005.png)

Выдаваемая информация: Машина добавлена, 200

1. GET <http://127.0.0.1:3005/cars>

![](https://github.com/cahashih/PiTPM_task_two/blob/master/Screens/Aspose.Words.e05d7563-d410-43e7-a04f-026977fd0751.006.png)

Выдаваемая информация: Все машины, 200

1. DELETE <http://127.0.0.1:3005/cars/0>

![](https://github.com/cahashih/PiTPM_task_two/blob/master/Screens/Aspose.Words.e05d7563-d410-43e7-a04f-026977fd0751.007.png)

Выдаваемая информация: Машина удалена, 200

1. PUT <http://127.0.0.1:3005/cars/0>

Body: JSON

{

`    `"brandCar":"LADA",

`    `"releaseCar":"2011",

`    `"modelCar":"SAMARA",

`    `"countryCar": "Russia"

}

![](https://github.com/cahashih/PiTPM_task_two/blob/master/Screens/Aspose.Words.e05d7563-d410-43e7-a04f-026977fd0751.008.png)

Выдаваемая информация: Машина изменена, 200




