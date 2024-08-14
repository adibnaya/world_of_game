# World of Game

Welcome to the **World of Game** repository! This project is part of a DevOps course and serves as a practical example of integrating various DevOps practices into a game development project.

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Game](#running-the-game)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## About the Project

**World of Game** is a collection of mini-games developed as a part of a DevOps course project. The goal is to demonstrate the integration of continuous integration/continuous deployment (CI/CD) pipelines, infrastructure as code (IaC), containerization, and monitoring tools in a software development lifecycle.

This repository contains the source code, configuration files, and scripts necessary to build, test, deploy, and monitor the game.

## Features

- **Memory Game**: A sequence of numbers will appear for 1 second, and you have to guess it back.
- **Guess Game**: Guess a number and see if you chose the same as the computer.
- **Currency Roulette**: Try to guess the value of a random amount of USD in ILS.

## Getting Started

### Prerequisites

To get started with the project, you'll need the following tools installed on your system:

- Python 3.8+
- Git
- Docker (optional for containerization)
- Jenkins or any CI/CD tool (optional for CI/CD integration)

### Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/adibnaya/world_of_game.git
   cd world-of-game
   
2. Install Dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   
3. Set Up Environment Variables:
Create a .env file in the root directory and add any necessary environment variables for your project.

### Running the Game

1. You can run the game using the following command: 
    ```sh
    python main.py
    ```
Follow the on-screen prompts to select and play one of the available mini-games.

## Usage
This project can be used as a reference or a starting point for integrating DevOps practices into a game development project. You can extend it by adding more games, improving the CI/CD pipeline, or implementing additional monitoring and logging tools.

## License
This project is licensed under the MIT License. See `LICENSE` for more information.

## Contact
If you have any questions or suggestions, feel free to contact me:

Name: Adi Bnaya
Email: adibnaya@gmail.com
You can also open an issue in this repository for any bug reports or feature requests.

