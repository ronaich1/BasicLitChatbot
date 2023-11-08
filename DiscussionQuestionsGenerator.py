import openai
# TODO: use gradio to make this format more palatable before putting it on an actual website
#   so replace all the inputs and prints with input that you receive from the gradio website interface

# NOTE: using Literature Discussion Questions key in .env file
openai.api_key_path = ".env"

# establish messages list
set_type = "You are an insightful English teacher who likes to challenge their students"
messages = [{"role": "system", "content": set_type}]

# get the name of the novel the questions are being generated for
title = input("Please enter the name of the book: ")

# get the name of the author
author = input("Author of the book: ")

# get the number of discussion questions generated
num_questions = input("Please enter the number of discussion questions needed: ")

# add the api query to the messages:
query = "Please generate " + num_questions + " discussion questions about " + title + " by " + author
messages.append({"role": "user", "content": query})

# use the chatgpt api to generate a response object, add it to the messages, and print the discussion questions:
response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
response_text = response["choices"][0]["message"]["content"]
messages.append({"role": "assistant", "content": response_text})
print(response_text)
