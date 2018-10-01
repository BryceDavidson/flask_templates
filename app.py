from flask import Flask, render_template

# create instance of server
app = Flask(__name__)
# __name__ placeholder for app

# creating root page
@app.route('/')
def index():
    # will look inside /templates for html templates
    return render_template('index.html')

if __name__ == '__main__':
    # debug will refesh server for each save
    app.run(debug=True)
