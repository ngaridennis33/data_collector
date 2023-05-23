# Height Collector App
The Height Collector App is a simple application designed to collect and store height data from users. It provides an easy way to input and track height information, making it useful for various purposes such as health tracking, data analysis, or any other scenario where height data is required.

# Features
* Height Input: Users can input their height in a preferred unit (e.g., centimeters, inches).
* Data Storage: The app securely stores the collected height data in a mysql database.
Data sharing: Data is then sent to the user via the email uding smtp library.
Export: Users can export the height data for further analysis or sharing.
# Installation
To run the Height Collector App locally, follow these steps:

1. Ensure you have Python installed (version 3.6 or above).
2. Clone this repository to your local machine or download the source code as a ZIP file.
3. Open a terminal or command prompt and navigate to the project directory.
4. Install the required dependencies by running the following command:

```pip install -r requirements.txt```

5. Once the installation is complete, start the app by running:

```python app.py```

6. The app will be accessible at http://localhost:5000 in your web browser.

# Usage
1. Open the Height Collector App in your web browser.
2. On the home page, you will see an input field where you can enter your height.
3. Enter your height and select the appropriate unit (e.g., centimeters, inches).
4. Click the "Submit" button to store your height data.
5. You can view your previously submitted height data on the app's dashboard.
6. To export the height data, navigate to the "Export" section and follow the provided instructions.

# Contributing
Contributions to the Height Collector App are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure the app is still functioning correctly.
4. Write tests for your changes if applicable.
5. Commit your changes and push them to your fork.
6. Submit a pull request detailing your changes.
Please ensure your code follows the existing code style and includes appropriate documentation.

# License
The Height Collector App is licensed under the MIT License. Feel free to modify and use the app as per the terms of the license.

# Acknowledgments
The Height Collector App uses the Flask web framework.
Data visualization is done using Plotly.
The project structure and README template were inspired by Best-README-Template.
