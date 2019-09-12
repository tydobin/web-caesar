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
    </body>
        <form action="/" method='post'>
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0">
                
            </div>
            <textarea type="text" name="text"{0}></textarea>
            <br>
            <input type="submit">          
        </form>
    
    </body>
</html>
"""

@app.route("/", methods=['post'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    encrypted = rotate_string(text, rot)
    new_encrypted = form.format(encrypted)
    return "<h1>" + encrypted + "</h1>" + new_encrypted

@app.route("/")
def index():
	
    return form.format('')

app.run()