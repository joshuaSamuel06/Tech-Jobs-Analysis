##### This README file serves as a comprehensive guide, offering information on data analysis within this project.
  
#### Official dataset source
You can find the official published results of the survey here: [2023 Stack Overflow Survey Results](https://survey.stackoverflow.co/)

## Data Cleaning Process
In the `Data-Cleaning` phase, we cleaned the original dataset, `Dataset.csv`. The primary goal was to reorganize the dataset for readability, remove irrelevant columns, and handle missing data. Below are the detailed steps taken during this iteration:
```python
Data.drop(["SurveyLength","SurveyEase","Frequency_1","Frequency_2","Frequency_3", "TimeSearching",
 "TimeAnswering", "NEWSOSites", "SOVisitFreq", "SOAccount", "SOPartFreq", "SOComm", "SOAI","TBranch","Knowledge_1","Knowledge_2", "Knowledge_3", "Knowledge_4", "Knowledge_5",
"Knowledge_6", "Knowledge_7", "Knowledge_8"
```

- The cleaned dataset was saved as `cleaned_data.csv` within the `Data_Analysis` folder.
- To optimize file storage and access, the cleaned dataset was compressed into a ZIP archive (`cleaned_data.csv.zip`).

<br />

## Data-Analysis

This folder presents insights derived from the analysis of the Stack Overflow Survey dataset. The analysis focuses on understanding programming languages and web frameworks commonly used by developers, examining salary trends in the United States for developers with one year of experience, and evaluating sentiments towards AI technologies.

#### Essential Libraries for Running the Code

Ensure you have the following libraries installed:

- pandas
- matplotlib
- seaborn
- plotly

#### Visualizations and Analysis

- **Programming Languages Worked with vs. Languages Want to Work with**: This plot compares the programming languages developers have worked with against the languages they want to work with.

- **WebFrameworks Worked with vs. WebFrameworks Want to Work with**: This plot compares the web frameworks developers have worked with against the frameworks they want to work with.

- **Top Ten Developer Types and Salaries in the USA (1 Year Experience)**: This table displays the top ten developer types in the USA along with their salaries for developers with only one year of experience.

- **Average Salaries of Top Ten Developer Types in the USA (1 Year Experience)**: This table shows the average salaries of the top ten developer types in the USA for developers with only one year of experience.

- **AI Review:** The AI Review section provides insights into sentiments towards AI technologies based on survey responses.
  
- **Usage of AI in Development Process**: This plot illustrates the usage of AI tools in the development process across different main branches of developers.


**For detailed insights and interpretations, refer to the Finding Folder.**


