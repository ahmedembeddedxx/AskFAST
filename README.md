# AskFAST Chat Bot
## Overview

The AskFAST project features a chat bot that utilizes advanced machine learning techniques to provide interactive responses. The chat bot is implemented in Python and can be run both locally and on the cloud. The data used for training and evaluation is publicly available and was scraped using PyTesseract.

## Contributors

- **Duaa Fatima**
  - [GitHub Profile](https://github.com/Duaa-Fatima)
  - [LinkedIn Profile](https://www.linkedin.com/in/duaa-fatima-3b03ab260/)

- **Dawood Tanvir**
  - [GitHub Profile](https://github.com/dawoodTanvir)
  - [LinkedIn Profile](https://www.linkedin.com/in/dawood-tanvir-5a5365283/)

- **Mahum Raza**
  - [GitHub Profile](https://github.com/SyedaMahum)
  - [LinkedIn Profile](https://www.linkedin.com/in/syeda-mahum-raza-17596928b/)

- **Ahmed Abdullah**
  - [GitHub Profile](https://github.com/ahmedembeddedxx)
  - [LinkedIn Profile](https://www.linkedin.com/in/ahmed-abdullah)


## Repository Link

- [AskFAST GitHub Repository](https://github.com/ahmedembeddedxx/AskFAST)

## Requirements

- Python 3.8 or later
- CUDA enabled GPU (for local runs)
- Google Colab (for cloud runs)
- Gradio (for creating interactive web interfaces)
- Vercel (for deployment)

## Setup and Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/ahmedembeddedxx/AskFAST.git
    cd AskFAST
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure CUDA is enabled**

    If running locally, make sure CUDA is properly installed and configured (not suggested at all). For running in Google Colab, ensure the notebook is set to use a GPU runtime (preferably T4 GPU).

## Running the Chat Bot

1. **Execute the API Script**

    Navigate to the `src/scripts/` directory and run the `5_AskFAST_API.py` script:

    ```bash
    cd src/scripts
    python 5_AskFAST_API.py
    ```

    Upon successful execution, a link similar to `<random-string>.gradio.live` will be generated.

2. **Update the Web Application**

    Copy the generated link and paste it in the `src/web-app/index.html` file, replacing the placeholder in the `<Button>` send tag.

    ```html
    <Button send="https://<random-string>.gradio.live">
    ```

3. **Run the Web Application**

    You can run the application on localhost or deploy it on Vercel.

    - **Localhost:**

        Navigate to the web app directory and start a local server:

        ```bash
        cd src/web-app
        python -m http.server
        ```

    - **Vercel:**

        Follow the Vercel deployment guide to deploy your application.

## Data

A large amount of data is available in the `src/data` directory. This data was scraped using PyTesseract and is publicly available under the GNU and MIT licenses.

- **Data Directory:** `src/data`
- **Scripts for Data Scraping:** `src/scripts/`

## License

The data used in this project is publicly available under the GNU and MIT licenses.

## Demonstration Video

Watch the demonstration video for a quick overview of the project:

[![Watch the video](https://img.youtube.com/vi/Kd4OszKxlwc/0.jpg)](https://youtu.be/Kd4OszKxlwc)

---

Feel free to reach out to any of the contributors for questions or collaboration opportunities.
