
# ClassInsight

ClassInsight is a Streamlit-based web application designed to gather and visualize class evaluations from students. Students can submit their feedback on a class by rating it and providing optional comments, while admins can set the number of students and view detailed visualizations of the collected data, including sentiment analysis.

## Features

- **Student Interface**: Students can enter their name, provide a rating for the class, and optionally write feedback.
- **Admin Interface**: Admins can set the number of students, view all collected data, and access visualizations and sentiment analysis of the feedback.
- **Visualizations**: Provides bar charts for individual ratings, a gauge chart for the overall average rating, and sentiment analysis of feedback comments.
- **Data Export**: Saves collected data to a CSV file.

## Installation

To run ClassInsight, you need to have Python installed on your system. Follow the steps below to set up the project:

1. **Install Pipenv**:
   ```bash
   pip install pipenv
   ```

2. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

3. **Create and Activate a Virtual Environment**:
   ```bash
   pipenv install
   pipenv shell
   ```

4. **Install the Required Packages**:
   ```bash
   pipenv install streamlit pandas plotly textblob
   ```

5. **Install Command Line Tools for Xcode (macOS Specific)**:
   ```bash
   xcode-select --install
   ```

## Running the App

After setting up the environment and installing the necessary packages, you can run the Streamlit app using the following command:

```bash
streamlit run class_evaluation.py
```

This will launch the app in your default web browser.

## Usage

### Admin Interface

1. **Set Number of Students**:
   - Open the sidebar and check the "Admin" checkbox.
   - Enter the admin password (`admin123`) to gain access.
   - Set the number of students.

2. **View Data and Visualizations**:
   - After students have submitted their feedback, log in as admin.
   - View the collected data in a table format.
   - Access various visualizations, including bar charts for individual ratings and sentiment analysis of feedback.

### Student Interface

1. **Submit Feedback**:
   - Enter your name in the provided text box.
   - Rate the class on a scale of 1 to 5 using the slider.
   - Optionally, provide feedback about the class in the text area.
   - Click the "Submit" button to save your feedback.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Thanks to the Streamlit, pandas, plotly, and textblob libraries for making this project possible.


Replace `<repository_url>` and `<repository_name>` with the actual URL and name of your repository. This README file provides a comprehensive overview of your project, including installation, usage, and contribution guidelines.