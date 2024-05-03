import { MdDeleteForever } from 'react-icons/md';

const Note = () => {
    return(
        <div className="note">
            <span>TEST</span>
            <div className="note-footer">
                <small>03/05/2024</small>
                <MdDeleteForever className='delete-icon' size='1.3em' />
            </div>


        </div>
    )
};

export default Note;