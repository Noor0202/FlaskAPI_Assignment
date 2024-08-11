# FlaskAPI_Assignment

This is a simple FastAPI application that summarizes the content of a text file hosted on a URL.

# Requirements - 

  ## fastapi
  ## uvicorn
  ## transformers
  ## torch
  ## requests

After instaling all requirements run below command - 
uvicorn main:app --reload
after that
curl -X POST "http://127.0.0.1:8000/summarize" -H "Content-Type: application/json" -d "{\"url\":\"https://www.gutenberg.org/files/1342/1342-0.txt\"}"
above command will giev me id paste this id into below command
curl -X GET "http://127.0.0.1:8000/summary/paste id here"

it will give an summary example

i added some sample output

![Alt Text](FlaskAPI_Assignment/Screenshot (668).png)
![Alt Text](FlaskAPI_Assignment/Screenshot (669).png)
