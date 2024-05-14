import { useState, useEffect } from 'react';
import { nanoid } from 'nanoid';
import NotesList from './Components/NotesList';
import Search from './Components/Search';
import Header from './Components/Header';

const App = () => {
    const [notes, setNotes] = useState([]);
    const [searchText, setSearchText] = useState('');
    const [darkMode, setDarkMode] = useState(false);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const data = localStorage.getItem('notes');
                if (data) {
                    setNotes(JSON.parse(data));
                }
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        fetchData();
    }, []);

    useEffect(() => {
        localStorage.setItem('notes', JSON.stringify(notes));
    }, [notes]);

    const addNote = (text) => {
        const date = new Date();
        const newNote = {
            id: nanoid(),
            text: text,
            date: date.toLocaleDateString(),
        };
        const newNotes = [...notes, newNote];
        setNotes(newNotes);
    };

    const deleteNote = (id) => {
        const newNotes = notes.filter((note) => note.id !== id);
        setNotes(newNotes);
    };

    return (
        <div className={`${darkMode && 'dark-mode'}`}>
            <div className='container'>
                <Header handleToggleDarkMode={setDarkMode} />
                <Search handleSearchNote={setSearchText} />
                <NotesList
                    notes={notes.filter((note) =>
                        note.text.toLowerCase().includes(searchText)
                    )}
                    handleAddNote={addNote}
                    handleDeleteNote={deleteNote}
                />
            </div>
        </div>
    );
};

export default App;
