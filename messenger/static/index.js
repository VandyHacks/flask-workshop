var name = '';

window.onload = function (){
    // when the page finishes loading

    name = prompt('Username: ');
    console.log('name = ' + name)
    
    function updatePage() {
        // updates the page display

        fetch('/messages')
        .then(data => {
            console.log(data.status)
            let messages = data.response;
            console.log(messages);
            document.getElementById('rand').val(messages);
        })
        .catch(err => console.error(err));

    }
    
    window.setInterval(updatePage, 3000); // every 3 seconds
    
    // do this for initial load
    updatePage();
};

// when the form is submit
$("form").on("submit", function (e) {
    e.preventDefault(); // don't reload page

    let message = $('#sendbox')[0].value; // get message
    // send to server
    fetch('/', {
                method: 'POST',
                headers : new Headers(),
                body:JSON.stringify({name:name, message:message})
            })
            .then((data) =>  console.log(data))
            .catch((err)=>console.log(err))
    $('#sendbox')[0].val(''); // clear input
    return false;
})