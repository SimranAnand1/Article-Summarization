
import streamlit as st 
import os


# Sumy Summary Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


# Function for Sumy Summarization
def sumy_summarizer(docx):
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document,3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result


def main():
	""" NLP Based App with Streamlit """

	# Title
	st.title("NLPiffy with Streamlit")
	st.subheader("Natural Language Processing On the Go..")
	st.markdown("""
    	#### Description
    	+ This is a Natural Language Processing(NLP) Based App useful for basic NLP task
    	like Text Summarization
    	""")


	# Summarization
	if st.checkbox("Show Text Summarization"):
		st.subheader("Summarize Your Text")

		message = st.text_area("Enter Text","Type Here ..")
		summary_options = st.selectbox("Choose Summarizer",['sumy','gensim'])
		if st.button("Summarize"):
			if summary_options == 'sumy':
				st.text("Using Sumy Summarizer ..")
				summary_result = sumy_summarizer(message)

		
			st.success(summary_result)



	st.sidebar.subheader("About App")
	st.sidebar.text("NLPiffy App with Streamlit")
	

	st.sidebar.subheader("By")
	st.sidebar.text("SIMRAN ANAND")
	st.sidebar.text("SIMRAN ANAND")
	
