import React, {useState} from "react";
import './App.css';

function SearchBox({onSearch}) {
    const [searchText, setSearchText] = useState("");

    const handleSearch = async () => {
        const response = await fetch(`http://127.0.0.1:4000/api/recommendation?title=${searchText}`);
        const data = await response.json();
        onSearch(data.movies);
    }

    return (
        <div className="search-container">
            <input
                type="text"
                value={searchText}
                onChange={(e) => setSearchText(e.target.value)}
                placeholder="Enter the name of a movie, and we will recommend you related movies!"
                className="search-input"
            />
            <button onClick={handleSearch} className="search-button">
                Search
            </button>
        </div>
    );

}

export default SearchBox;