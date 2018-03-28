from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True



form = """

 <!DOCTYPE html>



<html>

    <head>

        <style>

            form {{

                background-color: #eee;

                padding: 20px;

                margin: 0 auto;

                width: 540px;

                font: 16px sans-serif;

                border-radius: 10px;

            }}

            textarea {{

                margin: 10px 0;

                width: 540px;

                height: 120px;

            }}

        </style>

    </head>

    <body>
        <form method="post">
             <lable>Rotate by:</lable> 
             <input type="text" name="rot" value="0"/>
             <textarea name="text">{0}</textarea>
             <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>
"""


@app.route("/")
def index():
    return form.format("") 
    

@app.route("/", methods=['POST'])
def encrypt():
    #print(request)
    #print(request.args)
    #print(request.form)
    #print(request.form['rot'])
    #print(request.form['text'])
    rot = (int(request.form['rot']))
    text = request.form['text']
    #rot = (int(""))
    rotated_text = rotate_string(text, rot)
    #text = (str("" + rotate_string))
    return form.format(rotated_text)

app.run()


