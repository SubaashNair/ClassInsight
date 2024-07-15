import streamlit as st
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go

# Set page title
st.title("Class Evaluation App")

# Admin password
admin_password = "admin123"

# Number of students is preset to 5
num_students = 5

# Initialize session state for ratings and names if not already initialized
if 'students' not in st.session_state:
    st.session_state.students = {f"Student {i+1}": {"name": "", "rating": None, "timestamp": ""} for i in range(num_students)}

# Input: Names and ratings for each student
st.subheader("Enter the name and rating for each student (1 = Okay, 5 = Crazy):")

for i in range(num_students):
    student_key = f"Student {i+1}"
    name = st.text_input(f"Name of {student_key}:", key=f"name_{i}")
    rating = st.slider(f"Rating of {student_key}:", min_value=1, max_value=5, step=1, key=f"rating_{i}")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.students[student_key]["name"] = name
    st.session_state.students[student_key]["rating"] = rating
    st.session_state.students[student_key]["timestamp"] = timestamp

# Display the order of student entries
st.subheader("Order of student entries:")
for i in range(num_students):
    student_key = f"Student {i+1}"
    student_info = st.session_state.students[student_key]
    name_display = student_info["name"] if student_info["name"] else "Awaiting input..."
    st.write(f"{student_key}: {name_display} - {student_info['timestamp']}")

# Check if all students have entered their names and ratings
all_ratings_entered = all(
    student_info["name"] != "" and student_info["rating"] is not None 
    for student_info in st.session_state.students.values()
)

if all_ratings_entered:
    ratings_list = [student_info["rating"] for student_info in st.session_state.students.values()]
    average_rating = sum(ratings_list) / len(ratings_list)
    st.write(f"Average rating: {average_rating:.2f}")

    # Determine if the class is okay or crazy
    if average_rating <= 2:
        st.success("The class is okay!")
    else:
        st.error("The class is crazy!")

    # Save the data to a CSV file
    df = pd.DataFrame(st.session_state.students).T
    df.to_csv("class_evaluation.csv", index=False)
    st.write("Data has been saved to class_evaluation.csv")

    # Admin section
    st.subheader("Admin Section")
    admin_input = st.text_input("Enter admin password:", type="password")
    if admin_input == admin_password:
        st.write("Admin access granted.")

        # Display the dataframe
        st.write("Class Evaluation Data")
        st.dataframe(df)

        # Visualization using Plotly
        st.subheader("Visualization")

        # Bar chart for individual ratings
        bar_fig = go.Figure(data=[
            go.Bar(name='Rating', x=list(st.session_state.students.keys()), y=ratings_list)
        ])
        bar_fig.update_layout(title='Individual Ratings', xaxis_title='Student', yaxis_title='Rating')
        st.plotly_chart(bar_fig)

        # Gauge chart for overall rating
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
    else:
        st.warning("Please enter the correct admin password to view data and visualizations.")
else:
    st.warning("Please ensure all students have entered their names and ratings.")
