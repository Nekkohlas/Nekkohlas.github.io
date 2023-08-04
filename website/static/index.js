function deleteNote(noteID){
    fetch('/deleteNote', {
        method: "POST",
        body: JSON.stringify({noteId: noteId}),
    }).then((_res) => {
        window.location.href ="/";
    });
}

function checkNote(noteID){
    fetch('/check-note', {
        method: "POST",
        body: JSON.stringify({noteId: noteId}),
    }).then((_res) => {
        window.location.href ="/";
    });
}
