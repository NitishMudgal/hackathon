from flask import render_template, request
from app import app
from app.forms import SearchForm
import time
import json

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
       query_string = request.form.get("queryString")
       if query_string:
        start = time.time()
        final_list = []
        raw_data = [json.loads(line) for line in open('/Users/nitishmudgal/Organic/hackathon/empireio_tmp_content_first_sentence.json', 'r')]
        print('RAW DATA length')
        print(len(raw_data))
        for row in raw_data:
            if query_string in row['title']:
                final_list.append(row)
        end = time.time()
        processing_time = round((end - start)*1000)
        return render_template('results.html', final_list=final_list, processing_time=processing_time, query_string=query_string)
    return render_template('index.html')
