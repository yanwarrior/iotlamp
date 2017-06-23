## IOT Lamp Project

This is an example of my IoT project that is implemented for my friend's lecture. This project is to turn off and turn on the remote light using API to handle it and some devices like android and arduino.

### API model
Consists of the following models:

1. `Lamp`.
2. `Schedule`.
3. `Log`.

### Dependencies
You can install some Python packages needed for this project. I am using Python in version 3.x.

```txt
pip install -r requirements.txt
```

Run the development server in your command line:

```txt
python manage.py runserver
```

### Endpoint API
To be able to access the API, you need some tools, maybe use postman.

#### Lamps API
To get all the data of Lamps, you can use the following Endpoint with `GET` method:

```
http://127.0.0.1:8000/api/v1/lamps/
```

The result is as follows:

```json
{
    "count": 22,
    "next": "http://127.0.0.1:8000/api/v1/lamps/?page=2",
    "previous": null,
    "results": [
        {
            "id": 36,
            "name": "Tokyo Lamps Philips",
            "status": true,
            "schedules": []
        },
        {
            "id": 35,
            "name": "New Lampsss",
            "status": false,
            "schedules": []
        },
        { ... },
        {
            "id": 11,
            "name": "Lampu ke",
            "status": true,
            "schedules": [
                {
                    "id": 2,
                    "lamp": 11,
                    "lamp_date": "2017-06-29",
                    "lamp_time": "18:00:29",
                    "status": false,
                    "logs": []
                },
                {
                    "id": 3,
                    "lamp": 11,
                    "lamp_date": "2017-06-29",
                    "lamp_time": "18:00:29",
                    "status": false,
                    "logs": []
                }
            ]
        },
    ]
}
```

To create a new lamp, use the `POST` method with json data like the following:

```json
{
    "name": "Lamp in room 3443",
    "default": false
}
```

..with the same URL like:

```
http://127.0.0.1:8000/api/v1/lamps/
```

The result is as follows:

```json
{
    "id": 37,
    "name": "Lamp in room 3443",
    "status": false,
    "schedules": []
}
```

For other models, you can try it by opening my URL on this app and project.



