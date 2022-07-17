import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    respose = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=7381b86527a866cb5e04edd03f493c64&language=en-US'.format(movie_id))
    data = respose.json()
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']
def rate(movie_id):
    respose = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=7381b86527a866cb5e04edd03f493c64&language=en-US'.format(movie_id))
    data = respose.json()
    return data['vote_average']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similar[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:10]
    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_rating = []
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies_rating.append(rate(movie_id))
    return recommended_movies,recommended_movies_posters,recommended_movies_rating
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similar=pickle.load(open('similar.pkl','rb'))
col1, col2, col3, col4, col5 =st.columns(5)
with col1:
    st.title(' ')
with col2:
    st.title(' ')
with col3:
    st.header('#HASHMOVIES')
with col4:
    st.title(' ')
with col5:
    st.title(' ')

st.subheader('This is a movie Recommender system built using Machine learning. The largest movie libraries in the world are all digitized and transferred to online streaming services, like Netflix, HBO, or YouTube. Enhanced with AI-powered tools, these platforms can now assist us with probably the most difficult chore of all — picking a movie. This website does that for you,it recommends Top 10 movies based on the movie you choose. It is bulit using Streamlit')
selected_movie=st.selectbox('Type The Movie Name and Press Recommend',
    movies['title'].values)
if st.button('Recommend'):
   names,posters,rating = recommend(selected_movie)

   col1, col2, col3, col4, col5 =st.columns(5)
   with col1:
       st.text(names[0])
       st.image(posters[0])
       st.text(rating[0])
   with col2:
       st.text(names[1])
       st.image(posters[1])
       st.text(rating[1])
   with col3:
       st.text(names[2])
       st.image(posters[2])
       st.text(rating[2])
   with col4:
       st.text(names[3])
       st.image(posters[3])
       st.text(rating[3])
   with col5:
       st.text(names[4])
       st.image(posters[4])
       st.text(rating[4])
   col1, col2, col3, col4, col5 = st.columns(5)
   with col1:
       st.text(names[5])
       st.image(posters[5])
       st.text(rating[5])
   with col2:
       st.text(names[6])
       st.image(posters[6])
       st.text(rating[6])
   with col3:
       st.text(names[7])
       st.image(posters[7])
       st.text(rating[7])
   with col4:
       st.text(names[8])
       st.image(posters[8])
       st.text(rating[8])
   with col5:
       st.text(names[9])
       st.image(posters[9])
       st.text(rating[9])

#st.
# image('data:image/png;base64,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')


