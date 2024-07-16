from flask import Flask,render_template,request,url_for
import random

app = Flask(__name__)

# @app.route('/gifs')
# def gifs():
#     myGifs = [
#          "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmVmb21hdXU0ZTR5YjRsaHFocXJnZXRyam9taWhudGdjYTNkajRwdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Z0OzbQZYnnyN6u9Lr8/giphy.webp",
#          "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHN0YngzZnR0cTcxaHFzYXhocTAxeHV2bjk5czE4eWlnbnJ4aHh2OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cc1qxG84S13aCAbuKQ/giphy.webp",
#          "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjVmbGEzODRkNGY0Y2Nxb2F2NTRxemJsM2MzM3U3Y3AxejRleW1rZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5ZZSYqvcH6QppFQGI5/giphy.webp",
#          "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHprOGw2dm0ydWpwcTV1eWg2OWdxeW0wbXNvZHRkYnlwbDJyZGc1NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oEdv9R4D62GPrVY4g/giphy.webp",
#          "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMm9yaGFobm44a2V2dmt0ZWNxMzkxcXBvOGpqY2xqb3FrMXNjczc4NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5vD8o9XWJ5FLaHe8YP/giphy.webp",
#          "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGs3bXlnd3FkMzgwa3RiajZ2cXFibjVxaDV2OXk0MmU2cnVnZHlyZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1BXa2alBjrCXC/giphy.webp"
#     ]  
#     randomGif = random.choice(myGifs)
#     return render_template('gifs.html',random=randomGif, randomBool=False,myGifs=myGifs)

@app.route('/input', methods=['GET','POST'])
def input():
    imgData = {
         "dog":["https://i.natgeofe.com/n/4f5aaece-3300-41a4-b2a8-ed2708a0a27c/domestic-dog_thumb_square.jpg",
                "https://cdn.psychologytoday.com/sites/default/files/styles/article-inline-half-caption/public/field_blog_entry_images/2020-06/angry_chihuahua.png?itok=TWxYDbOT",
                "https://www.usatoday.com/gcdn/authoring/authoring-images/2024/04/25/PMJS/73459685007-240425-local-wisconsin-humane-society-p-3.jpg?width=1200&disable=upscale&format=pjpg&auto=webp"]
    }
    if request.method == 'POST':
        query = request.form['query']
        if query not in imgData:
            return "No data found for " + query # quits the function
        return render_template('gifs.html',imgData=imgData[query])

    return render_template('input.html',url=url_for('input'))

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80, debug=True)
