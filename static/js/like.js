
function like(e,post) {
    e.preventDefault();
    liked = e.target.classList[0];
    let user = document.getElementById('user').value;
    let csfr = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    var formData = new FormData();
    formData.append('user', user);
    formData.append('post', post);
    url = liked == 'True' ? '/posts/dislike/' : '/posts/like/';
    fetch(url, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': csfr,
        }
    })
        .then(res => res.json())
        .then(data => {
            if (data.message == 'ok') {
                count = parseInt(e.target.parentNode.children[1].innerText)
                if (liked=='True') {
                    e.target.style.color = '#000' 
                    e.target.classList.remove('True', 'fas','fa-heart');
                    e.target.classList.add('False','far','fa-heart');
                    count--;
                    e.target.parentNode.children[1].innerText = count;
                } else {
                    e.target.style.color = 'rgb(241, 45, 45)' 
                    e.target.classList.remove('False','far','fa-heart');
                    e.target.classList.add('True','fas','fa-heart');
                    count++;
                    e.target.parentNode.children[1].innerText = count;
                }

            }
        })
        .catch(e => console.log(e));
}