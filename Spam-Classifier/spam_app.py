# Import required libraries
import streamlit as st
import pickle 

# Load the trained model and vectorizer from saved files
# "rb" means read in binary mode
mod = pickle.load(open("Spam-Classifier/model.pkl", "rb"))
vec = pickle.load(open("Spam-Classifier/vectorizer.pkl", "rb"))

# Set title of the web app
st.title("✉️ Spam Message Classifier 📤")


# Create a text input box for user
# Whatever user types is stored in 'message'
message=st.text_area("Enter a message:")

# Create a button to trigger prediction
if st.button("predict"):
    if message.strip()=="":
        st.warning("please enter the message")
    else :
       
        # Convert input text into numerical format using trained vectorizer
        # We pass [message] because model expects list/array input
        message_vec=vec.transform([message])
        
        # Predict using trained model
        pred=mod.predict(message_vec)[0]
        
        # Display result based on prediction
        if pred==1:
            st.error("🚨 Spam Message")
        else :
            st.success("✅ Not Spam(Ham)")
