from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    this_year = datetime.datetime.now().year
    return render_template('index.html', num=random_number, year=this_year)

@app.route('/guess/<name>')
def guess(name):
    response = requests.get(url=f'https://api.agify.io/?name={name}')
    age = response.json()['age']
    age = response.json()['age']
    response2 = requests.get(url=f'https://api.genderize.io/?name={name}')
    gender = response2.json()['gender']

    return render_template('guess.html', name=name, age=age, gender=gender)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    response = requests.get(url='https://api.npoint.io/5abcca6f4e39b4955965')
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)