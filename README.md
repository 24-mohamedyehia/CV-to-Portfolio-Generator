# CV-to-Portfolio-Generator
A project that uses AI Agents to automatically extract information from your CV and create a personalized portfolio website.

## Requirements
- Python 3.10

### Install Python Using Miniconda
1- Download and install MiniConda from [here](https://www.anaconda.com/docs/getting-started/miniconda/main#quick-command-line-install)

2- Create a new environment using the following command:
```bash
$ conda create --name cv_to_Protfolio_generator python=3.10 -y
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
Set your environment variables in the .env file. Like GROQ_API_KEY value.