import React, { useState } from 'react';
import SearchBox from './SearchBox';
import MovieList from './MovieList';
import './App.css';

function App() {
  const [movies, setMovies] = useState([]);

  const searchMovies = (data) => {
    setMovies(data);
  }

  return (
    <div className="App">
      <h1>Movie Recommendation ML</h1>
      <SearchBox onSearch={searchMovies}/>
    <MovieList movies={movies}/>
    </div>
  );
}

export default App;
