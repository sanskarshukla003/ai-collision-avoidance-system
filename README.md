# ai-collision-avoidance-system
AI-Driven Collision Avoidance System

Welcome to the AI-Driven Collision Avoidance System! This project leverages GPS data and advanced algorithms to simulate, detect, and prevent vehicle collisions by engaging an Automatic Braking System (ABS) when obstacles are detected within a threshold distance.

Features

Real-Time GPS-Based Obstacle Detection: Automatically detects nearby obstacles using GPS coordinates.

Automatic Brake System (ABS) Activation: Engages ABS when an obstacle is detected within the threshold distance to prevent collisions.

Obstacle Simulation: Generate random obstacles to test the system.

Interactive Web Interface: Users can update the vehicle's location, simulate obstacles, and check for collisions via a web-based UI.

Customizable Threshold Distance: Adjust the proximity at which ABS is triggered.

Technology Stack

Backend: Python (Flask Framework)

Frontend: HTML, CSS, JavaScript

Libraries:

Flask for creating the web server.

Math and Random modules for obstacle simulation and distance calculation.

Installation and Setup

Prerequisites

Ensure you have the following installed on your system:

Python 3.7 or later

pip (Python package manager)

Git

Steps to Run Locally

Clone the Repository:

git clone https://github.com/your-username/ai-collision-avoidance-system.git
cd ai-collision-avoidance-system

Set Up a Virtual Environment:

python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate   # For Windows

Install Dependencies:

pip install flask

Run the Application:

python app.py

Access the Application:
Open your browser and go to http://127.0.0.1:5000.

Project Structure

ai_collision_avoidance/
|
├── app.py                 # Main Flask application
├── static/
│   ├── css/
│   │   └── style.css      # Styling for the webpage
│   ├── js/
│   │   └── script.js      # Optional JavaScript for interactivity
│   └── images/            # Store images for branding and design
│       └── logo.png
│
└── templates/
    ├── base.html          # Shared layout for all pages
    ├── index.html         # Home page
    ├── features.html      # Features page
    ├── demo.html          # Interactive demo
    └── contact.html       # Contact page

Deployment

You can deploy this project on platforms like Render, Heroku, or Vercel for live hosting.

Render Deployment Steps

Log in to Render.com.

Create a new Web Service and connect your GitHub repository.

Set the Build Command: pip install -r requirements.txt.

Set the Start Command: python app.py.

Render will provide a live URL for your application.

Heroku Deployment Steps

Install the Heroku CLI: Heroku CLI Installation Guide.

Log in to Heroku:

heroku login

Create a new Heroku app:

heroku create

Push the code to Heroku:

git push heroku main

Open the app:

heroku open

Usage

Update Vehicle Location:
Enter the latitude and longitude to update the vehicle’s position.

Simulate Obstacle:
Generate random obstacles nearby for testing.

Check Collision:
Detect if there is any obstacle within the threshold distance and engage ABS if necessary.

Screenshots


Screenshot of the Home Page


Screenshot of the Interactive Demo

Contributing

Contributions are welcome! Please follow these steps to contribute:

Fork the repository.

Create a new branch:

git checkout -b feature/your-feature-name

Commit your changes:

git commit -m "Add your message here"

Push to the branch:

git push origin feature/your-feature-name

Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

For any questions or support, reach out to:

Email: support@aicollision.com

Phone: +1-800-555-1234

Thank you for using the AI-Driven Collision Avoidance System! Stay safe on the roads.
