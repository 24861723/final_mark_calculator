# Final Mark Calculator

This project is a Final Mark Calculator built using Python and Streamlit. It helps students calculate the required mark for their final assessment (A2) based on their semester mark (SM) and first assessment mark (A1). The app allows users to input custom weights for each component and provides the required A2 marks to pass or achieve a distinction.

## Features

- Dark Mode: The app features a dark-themed UI for an improved user experience.
- Custom Input Fields:
  - Input your Semester Mark (SM) and Assessment 1 Mark (A1).
  - Set the weight percentages for each component: SM, A1, and A2.
- Required A2 Mark Calculation:
  - The app calculates the mark required on Assessment 2 (A2) to pass (50%) or to achieve a distinction (75%).
  - If a mark is already achieved or not achievable, it notifies the user.
- Results Table: The results are displayed in a neatly formatted table.
- CSV Export: Users can export the results as a CSV file for future reference.

## How to Run the Project

1. Clone the repository:
   git clone https://github.com/your-username/final-mark-calculator.git

2. Navigate to the project directory:
   cd final-mark-calculator

3. Install the required dependencies:
   pip install -r requirements.txt

4. Run the Streamlit app:
   streamlit run fm_calculator.py

5. Access the app in your browser at http://localhost:8501.

## File Structure

- fm_calculator.py: The main Python file that contains the Streamlit app logic.
- requirements.txt: List of dependencies required to run the app.
- README.txt: This file containing the project description.

## Technologies Used

- Python
- Streamlit: For building the web interface.
- Pandas: Used for handling data and exporting CSV files.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

- Your Name - GitHub: https://github.com/your-username
