import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')
st.title('the song between 2010 and 2019 on Spotify')
df = pd.read_csv('top10s.csv')
df['count'] = 1
year_of_song = st.slider('year',2010,2019)
df.isnull().sum()
form = st.sidebar
choose_filter = form.radio('choose something you want to learn about :', ('genre','bpm','nrgy','dnce','dB','live'))

if st.checkbox('you can check all the infromation there if you want'):
    st.write(df)

fig, ax = plt.subplots(figsize=(30, 15))
if choose_filter == 'genre':
    a = df.topgenre
    ax.set_xlabel('top genre')
elif choose_filter == 'bpm':
    a = df.bpm
    ax.set_xlabel('bpm')
elif choose_filter =='nrgy':
    a = df.nrgy
    ax.set_xlabel('nrgy')
elif choose_filter =='dnce':
    a = df.dnce
    ax.set_xlabel('dnce')
elif choose_filter == 'dB':
    a = df.dB
    ax.set_xlabel('dB')
else:
    a = df.live
    ax.set_xlabel('live')
b = a[df.year == year_of_song]
b.hist()
ax.set_ylabel('amount')
st.pyplot(fig)


st.subheader('problem analysis :')

st.subheader('Q1:Current situation of song industry on spotify:')
fig1, ax = plt.subplots(figsize=(15, 15))
a = df.groupby('year').sum()
a = a['count']
ax.set_title('number change')
ax.set_ylabel('Number of popular songs on spotify')
ax.set_xlabel('year')
a.plot(marker='s',color='red', linestyle='dashed')
st.pyplot(fig1)
st.write('At the same time, as shown in the figure above, the number of song creations after the epidemic has declined significantly, which means that the appeal of the song market is not as good as before. Now, it is necessary to be more cautious to join the song industry')

st.subheader('Q2:Commemorate popular trends of popular song genre:')
st.write('Genre with the largest number of creations and dnceularity in recent years :')
genre1 = df['topgenre'].value_counts().sort_values(ascending = False).reset_index().head(5)
genre2 = df.groupby(['topgenre'])['pop'].mean().sort_values(ascending = False).reset_index().head(5)
genre1 , genre2

fig8, ax = plt.subplots(figsize=(15, 15))
ax.set_title('Genre percentage chart')
ax=plt.pie(df['topgenre'].value_counts().iloc[:5],labels=df['topgenre'].value_counts().iloc[:5].index,autopct='%1.1f%%')
st.pyplot(fig8)

st.write('Analysis:')
st.write('We can find that on Spotify platform the creation of genre with the largest number does not coincide with the most dnceular genre among audience, instead some niche song is more dnceular')
st.write('So for creators, it is not necessary to follow the public to create song. Finding their own style may attract more  loyal fans')

st.subheader('Q3:The impact of beat and volume on song experience')
st.write('Beat and volume are the most basic factors of a song. Combine the senses in the data to explore the relationship between them')
fig2,ax = plt.subplots(figsize=(10, 10))
ax.set_xlabel('dB&bpm')
ax.set_ylabel('nrgy')
ax.set_title('nrgy')
ax=plt.scatter(df.bpm,df.nrgy)
ax=plt.scatter(df.dB,df.nrgy)
st.pyplot(fig2)

fig3,ax = plt.subplots(figsize=(10, 10))
ax.set_xlabel('dB&bpm')
ax.set_ylabel('dnce')
ax.set_title('dnce')
ax=plt.scatter(df.bpm,df.dnce)
ax=plt.scatter(df.dB,df.dnce)
st.pyplot(fig3)

st.write('According to the density of data distribution, most music decibels are the same size. There is no great relationship between rhythm and song energy. Songs with different rhythms can have great energy. However, there are some obvious relationships between the beat and the dance ability. Most of the songs with the highest dance ability are between 100-140')
