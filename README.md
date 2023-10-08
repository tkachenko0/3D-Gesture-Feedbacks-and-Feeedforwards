# 3d-Gesture-Feedbacks-and-Feeedforwards

- [Trello](https://trello.com/b/z04Zwrf2/uit-project)

## Introduction

## Getting Started (Development)

1. Clone the repository and `cd` into it:

    ```bash
    git clone https://github.com/tkachenko0/3d-Gesture-Feedbacks-and-Feeedforwards.git
    # cd into the project directory
    cd 3d-Gesture-Feedbacks-and-Feeedforwards
    ```

2. Create a virtual environment:

    ```bash
    python3.9 -m venv <YOUR-VENV-NAME>
    # or if you use conda
    conda create -n <YOUR-VENV-NAME> python=3.9
    ```

3. Activate the virtual environment:

    ```bash
    source <YOUR-VENV-NAME>/bin/activate
    # or if you use conda
    conda activate <YOUR-VENV-NAME>
    ```

4. Install the dependencies:

    ```bash
    pip3 install -r requirements.txt
    ```

5. Setup your environment variables in the `.properties` file:

    ```
    touch .properties
    ```

    ```properties
    CAMERA_INDEX=1 # the index of the camera to use
    ```

> **Note:** If you install new dependencies, make sure to update the `requirements.txt` file:

```bash
pip3 freeze > requirements.txt
```