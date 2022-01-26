from flask import render_template
from app import app
from app.forms import SearchForm
import time
import json

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        # return f'''<h1> Welcome {form.query_string.data} </h1>'''
        start = time.time()
        print('Start Time')
        print(start)
        final_list = []
        raw_data = [json.loads(line) for line in open('/Users/nitishmudgal/Organic/hackathon/empirio_tmp.json', 'r')]
        # data1 = json.load(json.dumps([f]))
        # print(raw_data)
        for row in raw_data:
            if form.query_string.data in row['title']:
                final_list.append(row)
        # print(final_list)
        end = time.time()
        print('ENd time')
        print(end)
        processing_time = round((end - start)*1000)
        print('processing time')
        print(processing_time)
        print(type(processing_time))
        return render_template('results.html', final_list=final_list, processing_time=processing_time)
    return render_template('index.html', form=form)
    # return render_template('index.html', title='Home', user=user)

@app.route('/index2', methods=['GET', 'POST'])
def index2():
    return render_template('index2.html')

@app.route('/index3', methods=['GET', 'POST'])
def index3():
    return render_template('index3.html')

