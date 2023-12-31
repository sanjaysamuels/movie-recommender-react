import pickle 
from sklearn.metrics.pairwise import cosine_similarity
import requests
import config

df1 = pickle.load(open('./data/movie_list.pkl', 'rb'))
tfidf_matrix = pickle.load(open('./data/tfidf_matrix.pkl', 'rb'))

def get_recommendation(title):
    try:
        idx = df1[df1['title'] == title].index[0]
    except:

        try:
            results = requests.get("https: //api.themoviedb.org/3/search/movie?api key="+config.api_key+"&query="+title)
            title = results.json()['results'][0]['title']
            idx = df1[df1['title'] == title].index[0]
        except:
            return "No Results Found"
    
    sim_score = list(enumerate(cosine_similarity(tfidf_matrix, tfidf_matrix[idx])))
    
    sim_score = sorted(sim_score, key=lambda x: x[1], reverse=True)
    
    sim_score = sim_score[1:9]
    
    movie_indices = [i[0] for i in sim_score]
    
    results = df1.iloc[movie_indices]
    
    recommendation = []
    
    for i in range (len(results)):
        recommendation.append({
            'title': results.iloc[i]['title'],
            'release_date': results.iloc[i]['release_date'],
            'popularity': results.iloc[i]['popularity'],
            'vote_count': results.iloc[i]['vote_count'],
            'vote_average': results.iloc[i]['vote_average'],
            'poster_path': 'https://image.tmdb.org/t/p/w500' + results.iloc[i]['poster_path'],
            'url': 'https://www.themoviedb.org/movie/' + str(results.iloc[i]['id'])
            })
    
    return recommendation

# print(get_recommendation('The Dark Knight'))