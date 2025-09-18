# app.py
# Interactive Streamlit dashboard for CORD-19 metadata

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv")
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract'] = df['abstract'].fillna("No abstract available")
    return df

df = load_data()

st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers")

# Year range slider
min_year = int(df['year'].min())
max_year = int(df['year'].max())
selected_year = st.slider("Select Year Range", min_year, max_year, (2020, 2021))

# Filter data
filtered_data = df[(df['year'] >= selected_year[0]) & (df['year'] <= selected_year[1])]
st.write(f"Number of papers published: {filtered_data.shape[0]}")

# Top 10 journals chart
top_journals = filtered_data['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=top_journals.values, y=top_journals.index, palette="coolwarm", ax=ax)
plt.xlabel("Number of Papers")
plt.ylabel("Journal")
plt.title("Top 10 Journals")
st.pyplot(fig)

# Word cloud of titles
all_titles = ' '.join(filtered_data['title'].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
fig2, ax2 = plt.subplots(figsize=(15,7))
ax2.imshow(wordcloud, interpolation='bilinear')
ax2.axis('off')
st.pyplot(fig2)

# Display sample of papers
st.subheader("Sample Papers")
st.dataframe(filtered_data[['title', 'journal', 'year', 'abstract']].head(10))
