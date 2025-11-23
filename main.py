from fastapi import FastAPI, Body
from pydantic import BaseModel,Field
from typing import Optional

app=FastAPI()

class Book:
    id: int 
    title: str 
    author: str 
    description: str 
    rating: int 
    published_date: int
    price: float

    def __init__(self,id,title,author,description,rating,published_date,price):
        self.id=id
        self.title=title 
        self.author=author
        self.description=description
        self.rating=rating 
        self.published_date=published_date 
        self.price=price 

BOOKS = [

    Book(1, 'AI Engineering', 'Sam Johnson', 'Introduction to Artificial Intelligence', 5, 2022, 250.37),

    Book(2, 'Mastering Python', 'John Smith', 'Advanced Python programming techniques', 5, 2020, 199.99),

    Book(3, 'Data Science Fundamentals', 'Emily Carter', 'Core concepts of Data Science', 4, 2019, 180.50),

    Book(4, 'Machine Learning Basics', 'Andrew Miles', 'Beginner guide to Machine Learning', 4, 2021, 210.00),

    Book(5, 'Deep Learning Illustrated', 'Sophia Ray', 'Neural networks and deep learning concepts', 5, 2023, 299.99),

    Book(6, 'SQL for Analysts', 'David Brown', 'SQL mastery for data professionals', 5, 2021, 175.75),

    Book(7, 'Cloud Computing Essentials', 'Ravi Kumar', 'Introduction to cloud platforms', 4, 2020, 225.40),

    Book(8, 'Cyber Security 101', 'Alan Turing', 'Basics of cyber security and protection', 4, 2018, 160.00),

    Book(9, 'Big Data Analytics', 'Nina Patel', 'Understanding big data tools and techniques', 5, 2022, 285.20),

    Book(10, 'The Power of Algorithms', 'Grace Hopper', 'In-depth analysis of algorithms', 5, 2017, 195.99),

    Book(11, 'Natural Language Processing', 'James Allen', 'Text processing and AI communication', 4, 2023, 260.49),

    Book(12, 'Python for Finance', 'Michael Bloom', 'Using Python in financial analysis', 4, 2019, 215.60),

    Book(13, 'Web Development Bootcamp', 'Laura King', 'Frontend and backend web technologies', 5, 2021, 245.00),

    Book(14, 'DevOps Handbook', 'Chris Martin', 'CI/CD and automation with DevOps', 5, 2022, 320.75),

    Book(15, 'Prompt Engineering Guide', 'Daniel Roth', 'How to write effective AI prompts', 5, 2023, 150.25)

]

class BookRequest(BaseModel):
     id: Optional[int] =Field(description="ID is not Mandatory",default=None)
     title: str =Field(min_length=5)
     author: str =Field(min_length=1)
     description: str =Field(min_length=1,max_length=100)
     rating: int =Field(gt=0,lt=6)
     published_date: int=Field(gt=1999,lt=2030)
     price: float=Field(gt=0)

     model_config={
        "json_schema_extra":{
            "example":{
                "id": 101,
                "title":"Learning Fast API in 90 Days",
                "author": "ABC",
                "description":"This Book is a masterclass on FastAPI",
                "rating": 5,
                "published_date": 2010,
                "price": 230.56

            }
        }
     }

class BookResponse():
    status: str 
    payload: dict




# Health Check

@app.get("/health")
def health():
    return {"status":"ok"}

# Read all Books

@app.get("/getbooks")
def read_book():
    return BOOKS

# Reading Individual Books # Path Parameter # Query Parameter 

@app.get("/books/{book_id}")
def read_book(book_id:int,rating:int):
    for book in BOOKS:
        if book.id==book_id:
            return book

# Read Book by Rating

@app.get("/bookrating/{rating}")
def read_book(rating:int):
    books_to_return=[]
    for book in BOOKS:
        if book.rating==rating:
            books_to_return.append(book)

    return books_to_return


# Creating a Query Parameter

@app.get("/readbooks/")
def read_book(book_id:int):
    for book in BOOKS:
        if book.id==book_id:
            return book
            

# Create Book

@app.post("/create_book")
async def create_book(book_request:BookRequest):
    new_book=Book(**book_request.model_dump())
    BOOKS.append(new_book)

    return {"status":"Book is Created", "payload":new_book }

















