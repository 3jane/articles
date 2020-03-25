---
<img src="../3jane-logo-full.png" alt="3Jane Capital Logo" width=366/>

# Autocorrelation of returns in major cryptocurrency markets

[Other articles](https://github.com/3jane/articles/)

This article comes with the following to ensure complete reproducibility:

* Exact datasets used the experiments were conducted on (the provided Jupyter Notebook will download them automatically to `/datasets/` folder).

* Exact code used for calculations and plotting of the results.

### Prerequisites for running the code
1. Make sure you have installed python 3.6+ and pip:
    ```bash
    $ python3 -V
    Python 3.7.3

    $ pip3 -V
    pip 19.3.1 from /usr/lib/python3/dist-packages (python 3.7)
    ```
    - [How to install Python on Windows](https://www.howtogeek.com/197947/how-to-install-python-on-windows/)
    - [How to install Python on Mac OS](https://docs.python-guide.org/starting/install3/osx/)
    
2. Install [Jupyter](https://jupyter.org/)
    ```bash
    pip3 install jupyter==1.0.0
    ```
    


### How to run notebook
1. Download or `git clone` this repository.
2. Go to the folder:
    ```bash
    $ cd articles/1-autocorrelation-time-bars/
    ```
3. Install dependencies:
    ```bash
    $ pip3 install -r requirements.txt
    ```
4. Run Jupyter Server:
    ```bash
    $ jupyter notebook
    ```

It will open the current directory in Jupyter. Open `autocorrelation.ipynb` Jupyter Notebook and select `Kernel -> Restart & Run All`.
