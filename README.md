# ZeroEyes: Innovations in Weapon Detection and Integrated Security

**A Graduation Project Submitted to the Faculty of Artificial Intelligence in Partial Fulfillment of the Requirements for the Degree of Bachelor Artificial Intelligence**

## Project Overview
ZeroEyes is an advanced surveillance system designed to enhance public safety by utilizing cutting-edge technologies for real-time threat detection and response. The system integrates various state-of-the-art models including YOLOv8 for gun and fire detection, MobileNet and Bi-directional LSTM for violence detection, and advanced face recognition techniques to identify suspicious individuals. This comprehensive solution is specifically tailored to meet the security needs of smart cities, important buildings such as government offices and corporate headquarters, as well as public places like parks, transportation hubs, and educational institutions. 

The main goal of ZeroEyes is to provide a robust and reliable security solution that can detect and respond to potential threats in real-time, thereby preventing incidents before they escalate. By combining advanced AI technologies with a user-friendly web interface, ZeroEyes ensures that security personnel can efficiently monitor and manage the system, enhancing the overall safety and security of the monitored environments.

## Introduction
Ensuring safety and security has become more crucial than ever. ZeroEyes integrates advanced surveillance technologies to monitor real-time activities and identify potential risks such as suspicious individuals, dangerous items, fights, and fires.

## Installation
To set up ZeroEyes locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Doha-Tarek/ZeroEyes.git
    cd ZeroEyes
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

## Features
- **Real-Time Threat Detection**: Detects guns, fires, and violent activities in real-time using advanced machine learning models.
- **Face Recognition**: Identifies and alerts about suspicious individuals.
- **User-Friendly Interface**: Easy-to-use web interface for monitoring and managing the system.
- **Live Streaming**: Supports real-time video streaming for immediate threat detection.

## Technologies Used
- **YOLOv8**: For gun and fire detection.
- **MobileNet and LSTM**: For real-time violence detection.
- **Face Recognition Libraries**: For identifying suspicious individuals.
- **Flask**: For integrating machine learning models with the web application.
- **Google Colab & Ngrok**: For running the Flask server and creating a public URL for the local server.

## System Design
ZeroEyes consists of multiple components:
1. **Detection Models**: YOLOv8 for gun and fire detection, MobileNet and LSTM for violence detection.
2. **Web Interface**: Developed using Flask to allow users to upload videos, view detection results, and use the live streaming feature.
3. **Database**: SQLite for storing user information and detection results.

## Contributors
- Doha Tarek Ismail
- Raneem Sabr Dawood
- Salma Saleh Saady
- Nada Mostafa Mohi Eldin

## Acknowledgments
We extend our heartfelt gratitude to Dr. Samar Elbedwehy for her invaluable guidance and support, as well as to the Faculty of Artificial Intelligence at Kafr El-Sheikh University.
