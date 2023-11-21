from flask import Flask, render_template, request
from chat import get_answer
app= Flask(__name__)
#list to store history of chat bot questions and answers
chatting_history= []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer', methods= ['GET', 'POST'])
def answer():
    #We use request.form to get data where we have used the POST method
    question = request.form['question']
    
    #now we have the question just pass the question to function we have made in chat.py
    answer= get_answer(question)
    
    #appending question and answer in the list of the chatting_history
    chatting_history.append({"User's Question": question, "ChatBot's Answer": answer})
    #stroing
    #sending question, answer, chat history to show on frontend
    return render_template('index.html', que = question, ans= answer, hist= chatting_history)


if __name__ == '__main__': 
   app.run()

