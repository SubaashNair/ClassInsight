import streamlit as st
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go
from textblob import TextBlob

# Set page title
st.title("Class Evaluation App")

# Admin password
admin_password = "admin123"

# Initialize session state for class data if not already initialized
if 'class_data' not in st.session_state:
    st.session_state.class_data = []

# Admin interface to set number of students and view data
if st.sidebar.checkbox("Admin"):
    admin_input = st.sidebar.text_input("Enter admin password:", type="password")
    if admin_input == admin_password:
        st.sidebar.success("Admin access granted.")
        st.sidebar.write("Set number of students:")
        num_students = st.sidebar.number_input("Number of students:", min_value=1, step=1)
        st.session_state.num_students = num_students
        
        if st.session_state.class_data:
            df = pd.DataFrame(st.session_state.class_data)
            st.write("Class Evaluation Data")
            st.dataframe(df)

            # Save the data to a CSV file
            df.to_csv("class_evaluation.csv", index=False)
            st.write("Data has been saved to class_evaluation.csv")

            # Visualization using Plotly
            st.subheader("Visualization")

            # Bar chart for individual ratings
            bar_fig = go.Figure(data=[
                go.Bar(name='Rating', x=df["name"], y=df["rating"])
            ])
            bar_fig.update_layout(title='Individual Ratings', xaxis_title='Student', yaxis_title='Rating')
            st.plotly_chart(bar_fig)

            # Gauge chart for overall rating
            average_rating = df["rating"].mean()
            gauge_fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=average_rating,
                title={'text': "Average Rating"},
                gauge={'axis': {'range': [1, 5]},
                       'bar': {'color': "darkblue"},
                       'steps': [
                           {'range': [1, 2], 'color': "lightgreen"},
                           {'range': [2, 3], 'color': "yellow"},
                           {'range': [3, 4], 'color': "orange"},
                           {'range': [4, 5], 'color': "red"}]}
            ))
            st.plotly_chart(gauge_fig)

            # Sentiment analysis of feedback
            st.subheader("Sentiment Analysis")
            df['polarity'] = df['feedback'].apply(lambda x: TextBlob(x).sentiment.polarity if x else None)
            df['subjectivity'] = df['feedback'].apply(lambda x: TextBlob(x).sentiment.subjectivity if x else None)
            
            sentiment_fig = go.Figure(data=[
                go.Scatter(x=df["name"], y=df["polarity"], mode='markers', marker=dict(size=10), name='Polarity'),
                go.Scatter(x=df["name"], y=df["subjectivity"], mode='markers', marker=dict(size=10), name='Subjectivity')
            ])
            sentiment_fig.update_layout(title='Sentiment Analysis of Feedback', xaxis_title='Student', yaxis_title='Sentiment Value')
            st.plotly_chart(sentiment_fig)

            # Display key areas
            st.write("Key Areas (Sentiment Analysis)")
            st.write("Polarity (range -1 to 1): Indicates positive or negative sentiment.")
            st.write("Subjectivity (range 0 to 1): Indicates personal opinion or factual information.")
        else:
            st.warning("No data available yet.")
    else:
        st.sidebar.warning("Please enter the correct admin password.")

# Student interface to provide feedback
else:
    st.subheader("Student Input")
    name = st.text_input("Enter your name:")
    rating = st.slider("Rate the class (1 = Okay, 5 = Crazy):", min_value=1, max_value=5, step=1)
    feedback = st.text_area("Optional: Write about the class (feedback):")

    # Button to submit student input
    if st.button("Submit"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.class_data.append({
            "name": name,
            "rating": rating,
            "feedback": feedback,
            "timestamp": timestamp
        })
        st.success("Your input has been submitted!")
