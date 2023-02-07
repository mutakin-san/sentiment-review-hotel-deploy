import pandas as pd
import pickle
import streamlit as st

# loading in the model to predict on the data
pickle_in = open('sentiment_model.pkl', 'rb')
classifier = pickle.load(pickle_in)

def welcome():
	return 'welcome all'

# defining the function which will make the prediction using
# the data which the user inputs
def prediction(text):
	prediction = classifier.predict([text])
	print(prediction)
	return prediction

# this is the main function in which we define our webpage
def main():
	# giving the webpage a title
	st.title("Sentiments Analysis Hotel Review")
	
	# here we define some of the front end elements of the web page like
	# the font and background color, the padding and the text to be displayed
	html_temp = """
	<div style ="background-color:lightgreen;padding:13px">
	<h1 style ="color:black;text-align:center;">Hotel Review Sentiment Analysis by Mutakin & Rais</h1>
	</div>
	"""
	
	# this line allows us to display the front end aspects we have
	# defined in the above code
	st.markdown(html_temp, unsafe_allow_html = True)
	
	# the following lines create text boxes in which the user can enter
	# the data required to make the prediction
	review = st.text_input("Review", "Type Here")
	result =""
	
	# the below line ensures that when the button called 'Predict' is clicked,
	# the prediction function defined above is called to make the prediction
	# and store it in the variable result
	if st.button("Predict"):
		result = prediction(review)[0]
	st.success('The output is {}'.format(result))
	
if __name__=='__main__':
	main()
