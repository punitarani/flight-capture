# flight-capture
***Simple tool for tracking nearby flights and capturing images***


## Features
* **Automatically gets flight data from the OpenSky Network**
* **Camera automatically tracks and captures images of nearby planes**
* **Save data locally and can live streams video**


## Requirements
* **Python 3.9+**
* **Any Raspberry Pi w/ Wifi**
* **2-axis (Pan-Tilt) Camera Gimbal**


## Installation
**Download repo directly on RaspberryPi**

`git clone https://github.com/punitarani/flight-capture`


**Download dependencies and required libraries**

1. **Install pip** 

`sudo apt-get install python-pip`

2. **Install libraries**. First, `cd` to the project root.

*Default: `cd flight-capture`*

`pip install -r requirements.txt`

#### OR
 
**Run setup.py**:

`python setup.py`

## Usage
**Run the following command to run app**

`streamlit run main.py`

Add port (optional). *Default: **8501***

`--server.port 8501`

**Command line output should include**:
```commandline
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501

Network URL: http://RaspberryPi.IP:8501

```
*You can view the live status of the system with the **Network URL**.*
