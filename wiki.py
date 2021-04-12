#import wikipedia

#import streamlit as st

#from flask import Flask,url_for,render_template,request
#import spacy
#from spacy import displacy
#nlp = spacy.load("en_core_web_sm")
#import json

#HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

#from flaskext.markdown import Markdown

#app = Flask(__name__)
#Markdown(app)


#@app.route('/')
#def index():
#	return render_template('index.html')


#@app.route('/extract',methods=["GET","POST"])
#def extract():
#	if request.method == 'POST':
#		raw_text = request.form['rawtext']
#		html = displacy.render(docx,style="ent")
#		html = html.replace("\n\n","\n")
#		result = HTML_WRAPPER.format(html)

#	return render_template('result.html',rawtext=wikipedia.search(raw_text,results=1),result=result)


#if __name__ == '__main__':
#	app.run(debug=True)