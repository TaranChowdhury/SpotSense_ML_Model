

## How to use

* IPython Notebook:

``` Download the notebook and upload Jupyter Notebooks. The rest of the instructions are in the notebook. ```

## To run code on a local machine

* Create a Python virtual environment and install the dependencies using the following command:

``` pip install -r requirements.txt ```

* Use set_regions.py to set the parking regions:

``` python set_regions.py PATH_OF_VIDEO_FILE NAME_OF_OUTPUT_FILE(optional)```

* Use detector.py to get the output:

``` python detector.py PATH_OF_VIDEO_FILE PATH_OF_PARKING_REGIONS_FILE ```


