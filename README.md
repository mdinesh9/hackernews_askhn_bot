# Steps in order:

### Create the following folders in the root folder OR same as 1_pull_hn_data.py and 2_create_training_data.py
    - data/raw
    - data/processed 

### Scripts to run in order
    -   1_pull_hn_data.py 
    -   2_create_training_data.py

### Clone nmt-chatbot repo from Daniel Kukiela
    - git clone --branch v0.1 --recursive https://github.com/daniel-kukiela/nmt-chatbot.git
    - Manually install packages from requirements.txt based on your machine specifications  

    - My installation notes:
        - I trained the model in Paperspace - Ubuntu ML in a box 16 version.
        - When I tried to run train.py inside nmt-chatbot, I got tensorflow libcublas.so.9.0: cannot open shared file error
        - So, I installed tensorflow-gpu==1.4 using 
            - pip3 install --upgrade tensorflow-gpu==1.4  

