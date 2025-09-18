# CORD-19 Research Data Analysis & Streamlit App
**Project Overview**

This project is a beginner-friendly data analysis of COVID-19 research papers using the CORD-19 dataset. The focus is on exploring publication trends, identifying top journals, analyzing paper titles, and visualizing findings with interactive dashboards.

Dataset Source: CORD-19 Research Challenge - Kaggle

**Key Objectives:**

- Load and explore real-world COVID-19 research data

- Clean and prepare data for analysis

- Generate meaningful visualizations

- Build an interactive Streamlit app to explore trends

- Gain hands-on experience with Python, Pandas, Matplotlib, Seaborn, and Streamlit

**Dataset**

The project uses metadata.csv from the CORD-19 dataset, which includes:

- Paper titles and abstracts

- Publication dates

- Authors and journals

- Source information

Note: Only the metadata.csv file is used to simplify the analysis.

Download Link: [CORD-19 Dataset on Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

**Project Structure**

Frameworks_Assignment/

  │
  
  ├── metadata.csv          # CORD-19 metadata file
  
  ├── CORD19_Analysis.ipynb # Jupyter notebook with analysis & visualizations
  
  ├── app.py                # Streamlit interactive dashboard
  
  └── README.md             # Project documentation

**Part 1: Data Loading & Exploration**

- Load metadata.csv into a Pandas DataFrame

- Inspect dataset structure, rows, and columns

- Check missing values and data types

- Generate basic statistics

```bash
import pandas as pd

df = pd.read_csv('metadata.csv')
print(df.head())
print(df.info())
print(df.isnull().sum())
```

**Part 2: Data Cleaning & Preparation**

- Convert publish_time to datetime format

- Extract publication year for time-based analysis

- Fill missing abstracts with "No abstract available"

- Optionally create additional columns, e.g., abstract word count

- Remove duplicate entries

```bash
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['abstract'] = df['abstract'].fillna("No abstract available")
df.drop_duplicates(subset=['sha'], inplace=True)
```

**Part 3: Data Analysis & Visualization**

Analysis Includes:

- Number of papers published per year

- Top 10 journals publishing COVID-19 research

- Most frequent words in paper titles (Word Cloud)

- Distribution of papers by source

Sample Visualization:

```bash
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

year_counts = df['year'].value_counts().sort_index()
plt.figure(figsize=(10,5))
sns.barplot(x=year_counts.index, y=year_counts.values)
plt.title("Publications by Year")
plt.show()
```

**Part 4: Streamlit Application**

The interactive dashboard allows users to:

- Filter publications by year using a slider

- Display the number of papers in the selected range

- Show top 10 journals in the selected range

- Visualize a Word Cloud of paper titles

- Display a sample of papers including title, journal, year, and abstract

Running the App:

```bash
pip install streamlit pandas matplotlib seaborn wordcloud
streamlit run app.py
```

***Part 5: Requirements***

- Python 3.7+

- Libraries: pandas, matplotlib, seaborn, wordcloud, streamlit

```bash
pip install pandas matplotlib seaborn wordcloud streamlit
```

***Part 6: Expected Outcomes***

- Cleaned and explored COVID-19 research dataset

- Visual insights into publication trends

- Interactive Streamlit app for exploring papers

- Experience with data analysis workflow, visualization, and dashboard creation

**Part 7: Reflection**

- Challenges: Handling missing data, large dataset size, creating interactive visualizations

- Learning: Pandas for data cleaning, Matplotlib/Seaborn for visualization, Streamlit for dashboards

- Next Steps: Analyze abstracts or authors, implement search, create time-series plots

## Author

Name: _Raphael Msomea_

Email: _msomearaphael@gmail.com_

[GitHub Repo](https://github.com/msomea/covid-19-data-analysis.git)
