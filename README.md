# READ ME — CariSurg Week 0 Assignments

## Assignment No.1 ##

Assignment #1 focuses on understanding how to use the core tools that will be used in the duration of the programme, like the TenX Platform, Google Colab/Jupyter Notebooks, Python, etc. Focusing on the actual assignment deliverables, the aim was to sort the gender column only of an uncleaned data set `EmergencyTriageDataset_Reduced_Dirty.csv`. This was done using the python library, pandas, and the functions/methods associated with it. Under this library, the following were explored:

1. Reading a file
2. Note unique values
3. Count each unique value
4. Remapping each value in a column from a dictionary
5. Dropping a column
6. Renaming a column
7. Getting the head (first 10 results) of the data set

**__NOTE__**: This assignment contains a Jupyter Notebook file and a python file. This is intentional as I was experimenting and following along with the tutor as he was going through the exercise. 

### Overall Strategy ###

The gender column had data initially inputted as strings, and the data wasnt coherent. As such, the strings were converted to integers. 1 for male and 0 for female. To handle edge cases, other genders were set to be shown as 2. Integers 0 - 2 were chosen as they proved to be less computationally expensive to sort, when compared to strings. 

## Assignment No.2 ##

Assignment #2 focuses on understanding cleaning and sorting data better using the pandas library and simple visualization using matplotlib. Althought visualization wasnt the core focus of this assignment, it allowed for better understanding of how the library works and how the data actually looks when put on a graph. 

### Overall Strategy ###

This time the Fio2 column was cleaned. First, all the strings were converted to integers, and those that produced errors or NaNs were noted. Similarly, all the values outside of the valid range were also noted. Afterwhich the median was chosen to be the data point that would be assigned to the outliers. The median was chosen because of the differences in the environment of each patient. As a result, the data would be changed depending on each environment. Taking the average of that data would result in an unequivalent representation of most patients. Thus, the median was chosen. Then the data was imputed in terms of mean, standard deviation, count, etc, was shown along with the visualized graphs. 