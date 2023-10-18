import streamlit as st
import pickle
import pandas as pd
import requests

st.title('Movie Recommandation System')


def poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=452c558281dfb78ea4d992edfb68b90f&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/original"+data['poster_path']

def recommand(movie_name):
    movie=movie_list[movie_list['title']==movie_name].index[0]
    distance=similarity[movie]
    movies=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

    recomand_movie=[]
    posters=[]
    for i in movies:
        # movie
        id=movie_list.iloc[i[0]].movie_id
        recomand_movie.append(movie_list.iloc[i[0]]['title'])
        #fetch poster from API
        posters.append(poster(id))
    
    return recomand_movie,posters


#we need movies list so for we need to fetch from recommanded system file so use pickle 

# movies_list=pickle.load(open('movies.pkl','rb'))
# movies_list=movies_list['title'].values           #we need to use values other wise it come with index
# print(movies_list)

#it give error so we not send dataframe, we will send dictionary by pickle

movies_list=pickle.load(open('movie_dick.pkl','rb'))
movie_list=pd.DataFrame(movies_list)

similarity=pickle.load(open('similarity.pkl','rb'))

Movie_name=st.selectbox('Select the Movie:',movie_list['title'].values)



if st.button('Recommand Movies'):
    recommand_movies,posters=recommand(Movie_name)
    # for i in recommand_movies:
        # st.write(Movie_name)
        # st.write(i)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        # st.header(recommand_movies[0])
        st.text(recommand_movies[0])
        st.image(posters[0])
    with col2:
        # st.header(recommand_movies[1])
        st.text(recommand_movies[1])
        st.image(posters[1])

    with col3:
        st.text(recommand_movies[2])
        st.image(posters[2])

    with col4:
        st.text(recommand_movies[3])
        st.image(posters[3])

    with col5:
        st.text(recommand_movies[4])
        st.image(posters[4])