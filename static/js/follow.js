var btnFollow = document.getElementById('follow');

if(btnFollow){
    btnFollow.addEventListener('click',(e)=>{
        let user = document.getElementById('user').value;
        let profile = document.getElementById('profile').value;
        let csfr = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        var formData = new FormData();
        formData.append('user',user);
        formData.append('profile',profile);
        console.log(btnFollow.value);
        url = btnFollow.innerText == 'Unfollow' ? '/users/unfollow/' : '/users/follow/';
        console.log(url);
        fetch(url,{
            method:'POST',
            body:formData,
            headers:{
                'X-CSRFToken':csfr,
            }
        })
        .then(res=>res.json())
        .then(data =>{
            if(data.message == 'ok'){
                if(btnFollow.innerText == 'Unfollow'){
                    btnFollow.classList.remove('btn-danger');
                    btnFollow.classList.add('btn-primary');
                    btnFollow.innerText = 'Follow';
                }else{
                    btnFollow.classList.remove('btn-primary');
                    btnFollow.classList.add('btn-danger');
                    btnFollow.innerText = 'Unfollow';
                }
                
            }
        })
        .catch(e => console.log(e));
    });
}