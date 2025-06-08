# CV-to-Portfolio-Generator
A project that uses AI Agents to automatically extract information from your CV and create a personalized portfolio website.

## Screenshots
![image](./public/Screenshot%202025-04-25%20203613.png)

## Demo
<video src="./public/Demo.mp4" controls></video>

## Requirements
- Python 3.11

### Install Python Using Miniconda
1- Download and install MiniConda from [here](https://www.anaconda.com/docs/getting-started/miniconda/main#quick-command-line-install)

2- Create a new environment using the following command:
```bash
$ conda create --name cv_to_Protfolio_generator python=3.11 -y
```

3- Activate the environment:
```bash
$ conda activate cv_to_Protfolio_generator
```

### Installation

#### Install the required packages
```bash
$ pip install -r requirements.txt
```

### Setup the environment variables
```bash
$ cp .env.example .env
```
Set your environment variables in the .env file. Like OPEN_ROUTER_API_KEY value.

You can get your Open Router API key from [here](https://openrouter.ai/settings/keys).

## Run the application
```bash
$ python app.py
```

## Access the application
Open your browser and navigate to `http://127.0.0.1:5000`.

To stop the application, press `Ctrl+C` in your terminal.

## Features
- Upload a CV in PDF format
- Extract information from the CV using AI Agents
- Generate a personalized portfolio website
- Download the generated portfolio website

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
