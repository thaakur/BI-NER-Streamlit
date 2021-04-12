import wikipedia

import streamlit as st 

import spacy_streamlit
import spacy
import en_core_web_md
#nlp = spacy.load("en_core_web_sm")
nlp = en_core_web_md.load()


def main():
	"""A NLP NER app with Spacy-Streamlit"""

	st.title("Board Infinity TASK")
	
	st.subheader("Named Entity Recognition")

	raw_text = st.text_area("Your Text","Enter Any Name")
	for i in range(20):
		docx = nlp(wikipedia.summary(raw_text,sentences=5))
		if st.button("Display About Topic"):
			spacy_streamlit.visualize_ner(docx,labels=nlp.get_pipe('ner').labels)


if __name__ == '__main__':
	main()