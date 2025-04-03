# Schedule Your Mac to Shutdown (2023)
Do you use your Mac to watch Netflix and would you like to schedule a shutdown time for when you fall asleep? 
Then this repo is for you!

## Installation
This repo uses Python 3.9. To install a Conda environment please use:
```bash
conda create --name schedule_mac --file requirements.txt
```

## Use
1. Go to Terminal
2. Activate your virtual environment:
    ```bash
    conda activate schedule_mac
    ```
3. Go to the directory where 'main.py' is stored
4. Execute the python script:
    ```bash
    python main.py
    ```
5. If your mac has a password, you'll be asked to give it. 
6. It's done! You should see a summary of the given schedule!