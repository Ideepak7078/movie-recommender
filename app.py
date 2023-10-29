import streamlit as st
import pickle
import pandas as pd
import requests

def recommend(movies):
    movie_index=movie[movie['title']==movies].index[0]
    distance=simlarity[movie_index]
    mlist=sorted(list(enumerate(distance)) , reverse=True,key=lambda x: x[1])[1:6]
    recm=[]
    recmposter=[]
    for i in mlist:
        movieid=    movie.iloc[i[0]].movie_id

        recm.append(movie.iloc[i[0]].title)
        recmposter.append(fetch_poster(movieid))
    return recm,recmposter


def fetch_poster(movie_id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8b17db49fb97789b270af63303909f5f&language=en-US')
    result=response.json()
    return 'https://image.tmdb.org/t/p/w500/' + result['poster_path']








movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movie=pd.DataFrame(movies_dict)

simlarity=pickle.load(open('simlarity.pkl','rb'))




st.title('Movie Recommender System')


selectMovie= st.selectbox(
   "How would you like to be contacted?",
   movie['title'].values,

)
if st.button('Recommend'):
    names,posters =recommend(selectMovie)
    col1,col2,col3,col4,col5=st.columns(5)
    



    

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])








        