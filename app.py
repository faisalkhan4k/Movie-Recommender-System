import streamlit as st
import pickle
import pandas as pd

def recommend(option):
    movie_index = movies_df[movies_df['title'] == option].index[0]
    distances = recommendations[movie_index]
    movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]


    L =[]
    for i in movies:

        movie_id = movies[0]
        m = movies_df.iloc[i[0]].title

        L.append(m)

    return L


st.title('Movie Recommender!')


movies_list = pickle.load(open('movies.pkl','rb'))
movies_df = pd.DataFrame(movies_list)


recommendations = pickle.load(open('similarity.pkl', 'rb'))


option = st.selectbox('Enter',movies_df['title'].values)


if st.button("Recommmed"):
    list_of_movies = recommend(option)
    for i in list_of_movies:

        st.write(i)

