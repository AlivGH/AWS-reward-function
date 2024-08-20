# AWS DeepRacer Custom Reward Function

## Project Overview
This repository contains the code and documentation for a project focused on developing a custom reward function to enhance the performance of an autonomous vehicle within the AWS DeepRacer simulation environment. The primary goal of this project is to optimize the vehicle's adherence to the center line, speed maintenance, and overall track positioning, resulting in faster lap times and improved stability.

## Key Features
- **Custom Reward Function:** Designed to improve the performance of the AWS DeepRacer by focusing on key aspects like centerline adherence, speed optimization, and track positioning.
- **Reinforcement Learning:** Implementation leverages reinforcement learning principles to continuously improve the vehicle's performance based on the reward function.
- **Detailed Analysis:** Includes comprehensive documentation of the methodology, implementation process, and key insights derived from the project.

## Skills Utilized
- **Reinforcement Learning**
- **Python Programming**

## Getting Started

### Prerequisites
- AWS DeepRacer console or local simulation environment
- Python 3.x

### Installation
1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/deepracer-reward-function.git
    cd deepracer-reward-function
    ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Customize the `reward_function.py` file with your own reward logic.
2. Upload the custom reward function to the AWS DeepRacer console.
3. Train your model and observe the performance improvements in the simulation.

## Results
The project has demonstrated significant improvements in lap times and vehicle stability within the AWS DeepRacer simulation. The custom reward function effectively guides the vehicle to maintain optimal track positioning while balancing speed and stability.

## Contact
Feel free to reach out for any questions or collaboration opportunities:

- **Gmail:** alivghasemi@gmail.com
- **LinkedIn:** [Ali V Ghasemi](https://www.linkedin.com/in/alivghasemi/)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
