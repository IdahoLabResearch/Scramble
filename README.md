## Scramble: Cross-validation for data sets with heterogeneous n values. 
## Description
Scramble was designed to deal with heterogeneous n values in modeling classes. This can occur when sample sizes differ between the classes the model is trying to identify. A reality of data that is gathered from real world environments. Scramble takes the principle of cross-validation, that resampling of data sets is critical to accurately estimate model accuracy during the training and testing process and utilizes the principle in the module’s functions. Scramble requires a user to provide the number of iterations (eg., 5). The module will then randomize each model class k number of times and then split the resulting randomize data sets along a user designated percentage training/testing split (eg., 80 % training and 20% testing). The module will then activate the user designated machine learning model they wish to use. This process will then be repeated k number of times. While this process is occurring Scramble will record progress and output them to the user’s IDLE console.

A little history. Scramble was originally developed for a computer vision project. The version of Scramble pushed to this repo uses labels and directory system structures inspired by the Functional Map of the World (fMoW) data set. https://github.com/fMoW/dataset

A note to potential users. Scramble was developed during the course of a low TRL R&D project. As such this code base has been thoroughly tested and used. However, the code base is not polished, and you will have to update a few variables for the code to work for your use case. All required updates are flagged in comments in the code.  

## What does Scramble actaully do?
Scramble performs cross-validation for n number of times. Ideally giving users a better idea of how their models will perform in a real world environment. 
![Semantic description of image](/images/scramble_process.png)
## Installation
Scramble will work with the standard Python 3 install

## Authors and acknowledgment
[Shiloh Elliott](https://www.linkedin.com/in/shiloh-elliott-279356133/) 

[Ashley Shields](https://github.com/ashleyshields)

Elizabeth Klaehn
## License
Go check out our lovely License doc. 

## Project status
At this time no further development of Scramble is planned. 
