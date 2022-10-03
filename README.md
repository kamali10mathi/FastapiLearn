# FastapiLearn
#### To run the project 
Open terminal where you checkout the project and do run the following steps
> uvicorn main:app --reload
# Run the GET/ POST commands using postman
- GET -> http://127.0.0.1:8000/items/7
- POST -> http://127.0.0.1:8000/path/ 
- PAYLOAD FOR POST -> {
    "msg":"All are happy"
}
- PUT-> http://127.0.0.1:8000/items/1
- PAYLOAD FOR PUT -> {"name":"kfhj", "price":19}
