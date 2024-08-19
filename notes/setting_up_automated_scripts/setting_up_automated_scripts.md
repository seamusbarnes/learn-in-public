# Tutorial: Creating and Running a python Script from Anywhere on macOS

## Introduction

<u>Problem</u>: How do I get the daily opening prices of several cryptocurrencies using a single shell command from anywhere on my MacOS?

<u>Solution</u>:

1. Write a `crypto-prices.py` script that scrapes the data from the Binance API using the requests package.
2. Make this `crypto-prices.py` script accessible from any shell.
3. Create a bash script to activate a virtual environment, run the python script, and then deactivate the environment, making the whole process executable from any shell.

## Detailed Steps

### Part 1: Setting Up the Virtual Environment

Before writing the python script, it's crucial to set up a python virtual environment. This environment helps manage dependencies and ensures that your script does not interfere with system-level python packages.

<b>Create virtual environment</b>

```bash
# Navigate to your project directory
cd /path/to/project/directory

# Create a virtual environment
python3 -m venv venv
```

### Part 2: Writing the `crypto-prices.py` Script

The python script will use the requests library to fetch cryptocurrency data from the Binance API. Install the requests package within the virtual environment:

```bash
# Activate the virtual environment
source venv/bin/activate

# Install requests
pip install requests

# Deactivate the virtual environment
deactivate
```

<b> Example python Script (`crypto-prices.py`) (complete script at the bottom of page)</b>

```python
#!/usr/bin/env python3
import requests

def get_crypto_prices():
    url = "https://api.binance.com/api/v3/ticker/price"
    response = requests.get(url)
    prices = response.json()
    return prices

if __name__ == "__main__":
    prices = get_crypto_prices()
    for price in prices:
    print(f"{price['symbol']}: {price['price']}")
```

<b>Explanation:</b>

- Shebang: The shebang line #!/usr/bin/env python3 tells the shell to use python 3 from the environment.
- Function get_crypto_prices(): This function fetches the current prices from Binance's API.

<b>Executable: Make the script executable:</b>

```bash
chmod +x crypto-prices.py
```

### Part 3: Making the Script Globally Accessible

Update `.zshrc`
To run the script from anywhere, add its directory to your shell's `PATH` in `.zshrc` (or `.bash_profile` for bash users):

```bash

# Open .zshrc with nano
nano ~/.zshrc

# Add the following line
export PATH="$PATH:/path/to/project/directory"

# Save and exit, then apply changes
source ~/.zshrc
```

### Part 4: Automating Environment Activation

The bash script will handle the environment activation, script execution, and deactivation, streamlining the entire process.

<b>Create the bash Wrapper Script (`run-crypto-prices.sh`)</b>

```bash
#!/bin/bash
# Path to the virtual environment

VENV_PATH="/path/to/project/directory/venv"

# Activate the virtual environment

source "${VENV_PATH}/bin/activate"

# Run the python script

/path/to/project/directory/crypto-prices.py

# Deactivate the virtual environment

deactivate
```

<b>Make it executable:</b>

```bash
chmod +x run-crypto-prices.sh
```

### Conclusion

With these steps, you've created a python script to fetch cryptocurrency prices, made it executable and accessible from anywhere on your macOS, and automated its execution within a virtual environment. This setup ensures that your development environment remains clean and your script execution is efficient.
