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

Assignment #2 focuses on understanding cleaning and sorting data better using the pandas library and simple visualization using matplotlib. Althought visualization wasn't the core focus of this assignment, it allowed for better understanding of how the library works and how the data actually looks when put on a graph. 

### Overall Strategy ###

This time the Fio2 column was cleaned. First, all the strings were converted to integers, and those that produced errors or NaNs were noted. Similarly, all the values outside of the valid range were also noted. Afterwhich the median was chosen to be the data point that would be assigned to the outliers. The median was chosen because of the differences in the environment of each patient. As a result, the data would be changed depending on each environment. Taking the average of that data would result in an unequivalent representation of most patients. Thus, the median was chosen. Then the data was imputed in terms of mean, standard deviation, count, etc, was shown along with the visualized graphs. 

## Assignment No.3 ##

Assignment #3 focuses on actually implementing and using the matplotlib library to visualize data. This assignment showed how important visualizing data can be to reveal trends, issues and even factors that are overlooked. Doing this assignment allowed for better understanding of the library, the use of different graphs, the need for visualization and why it is used. 

### Overall Strategy ###

In this assignment two graphs were plotted. One, the FiO2 histogram, and the other being the Pulse vs GCS bar chart. 

The clinical question this histogram addresses is: what is the distribution of oxygen support requirements across the patient population at Mercer General ED? A histogram is the most appropriate plot here because FiO₂ is a continuous variable, making it ideal for revealing the shape and spread of values across the valid clinical range of 21–100%. It makes it immediately clear where the bulk of patients cluster and whether any outliers exist beyond the expected boundaries. The reference lines added carry direct clinical meaning. The shaded blue zone and dotted line at 21% mark the lower bound of the valid FiO₂ range, where any values below this would be physiologically impossible and would flag data quality issues. The shaded red zone and dotted line at 100% mark the upper clinical limit, where values beyond this point would similarly indicate erroneous entries and warrant further investigation.

The clinical question this bar chart addresses is: does the level of consciousness as measured by GCS have any association with a patient's heart rate across the patient population at Mercer General ED? A bar chart is the most appropriate plot here because GCS is an ordinal variable with discrete scores, and grouping mean heart rate by each score respects that discrete nature while the error bars communicate variability within each group.
The GCS severity band shading carries direct clinical meaning by dividing the chart into the three recognized neurological impairment categories (severe, moderate, and mild) immediately orienting the viewer to clinically significant thresholds. The tachycardia reference line at 100 bpm and bradycardia line at 60 bpm further contextualize the heart rate values, since abnormal readings in low GCS patients can indicate conditions such as raised intracranial pressure. Together these annotations transform the bar chart from a simple mean comparison into a clinically meaningful exploration of the relationship between consciousness level and cardiovascular response.


## Research ##
[Respiratory Rate Research](https://drive.google.com/file/d/1J2XD8Lqt-C1EzuYun97DO-44KtQK6Uzc/view)
[Blood Glucose Research](https://drive.google.com/file/d/1J2XD8Lqt-C1EzuYun97DO-44KtQK6Uzc/view)

These two documents serve as research into a vital sign that was considered for triaging for this project, and another vital sign that wasn't considered. They cover a simple overview and definition of the vital sign, the normal range that it lies in and why that vital sign is important for triaging. Additionally the sources that I used to fuel the research can be found at the end of each document. 


## Triaging System Pseudocode ##

[Triage Pseudocode Document](https://drive.google.com/file/d/1lZUalM5gEYX9rtmq4zG8VTCE8E-cYTpL/view)

This document outlines the pseudocode and logical flow behind the AI-powered triage system that is to be built over the coming weeks. It covers the seven phases of the triage pipeline. From patient intake and data collection, through scoring and risk categorization, to discharge documentation and post-visit recording. The pseudocode serves as the foundational blueprint for the system's decision making logic and is intended to guide development and clinical validation efforts.

## Career Challenge ## 

[Career Challenge Document](https://drive.google.com/file/d/109MVUfv2U-PpMzqqYUGwqnbRtogAPVi8/view?usp=sharing)

This document contains my structured study plan and framework for completing the Healthcare AI Programme. Balancing a 9-5 job with intensive technical learning requires a disciplined approach, and this documentation outlines how I manage my time to ensure consistency and prevent burnout. To maintain high levels of focus and information retention after a full workday, I will adopt the Pomodoro Technique. This method breaks study sessions into focused intervals with scheduled breaks, which is essential for managing the complex, technical material in this programme, such as coding, machine learning, and healthcare systems.