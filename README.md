# 3d-Gesture-Feedbacks-and-Feeedforwards

- [Trello](https://trello.com/b/z04Zwrf2/uit-project)

## Introduction

## Getting Started (Development)

1. Clone the repository and `cd` into it:

    ```bash
    git clone https://github.com/tkachenko0/3d-Gesture-Feedbacks-and-Feeedforwards.git

    cd 3d-Gesture-Feedbacks-and-Feeedforwards
    ```

2. Create a virtual environment:

    ```bash
    python3.9 -m venv venv # potete provare prima anche con la versione di py che avete già, ma non è detto che non vi causi problemi dopo
    ```

3. Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

4. Install the dependencies:

    ```bash
    pip3 install -r requirements.txt
    ```

5. Verify if the imports work:

    ```bash
    python src/main.py
    ```

> **Note:** If you install new dependencies, make sure to update the `requirements.txt` file:

```bash
pip3 freeze > requirements.txt
```
