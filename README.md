*Registeration*

/api/register/

{
    "first_name": "",
    "last_name": "",
    "username": "",
    "email": "",
    "password": "",
    "contact": ""
}

*Login*
/api/login/

{
    "username": "",
    "password": ""
}


*Product view and POST*
/api/product/
[
    {
        "id": 1,
        "name": "Train",
        "add_date": "2022-03-14T05:13:23.554000Z",
        "update_date": "2022-03-14T05:13:23.554000Z",
        "price": 150,
        "quantity": 5,
        "image": "/Products/daniel-abadia-Njq3Nz6-5rQ-unsplash.jpg"
    },
    {
        "id": 2,
        "name": "Gopi",
        "add_date": "2022-03-14T06:25:40.797000Z",
        "update_date": "2022-03-14T06:25:40.797000Z",
        "price": 45,
        "quantity": 4,
        "image": "/Products/daniel-abadia-Njq3Nz6-5rQ-unsplash_Y1vPltN.jpg"
    }
]

retrive data for other operation like delete edit or single view
/api/product/{int}/