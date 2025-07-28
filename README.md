
#  Robot Arm Control System (Django Web App)

This project is a complete web-based interface for controlling a 6-DOF robotic arm using Django. It provides both a user-friendly control panel and a REST-style API for robot-to-server communication.

## Features

-  Control 6 motor angles via interactive sliders
-  Save named poses to a database
-  Load and remove saved poses
-  Send a pose to the robot for execution
-  Robot polling via `/api/get_run_pose/`
-  Robot status update via `/api/update_status/`
-  Admin panel to manage poses and commands

##  Interface Preview

<img width="1907" height="852" alt="Screenshot 2025-07-28 190447" src="https://github.com/user-attachments/assets/a2673167-5f65-4854-b98d-a750640b48f4" />
<img width="1913" height="862" alt="Screenshot 2025-07-28 192545" src="https://github.com/user-attachments/assets/c7b62ab8-b35d-4864-954f-7bcbda675be9" />
<img width="1918" height="862" alt="image" src="https://github.com/user-attachments/assets/918efb68-584a-4412-ad61-a03a362d3214" />
<img width="233" height="652" alt="image" src="https://github.com/user-attachments/assets/fe7a965e-26cc-4ff2-aff8-d147d5c83f02" />



##  Tech Stack

| Layer       | Technology        |
|-------------|-------------------|
| Frontend    | HTML, CSS, JS     |
| Backend     | Django (Python)   |
| Database    | SQLite            |
| API Format  | JSON              |


## For more detailed explanation, refer to the full project report PDF.


