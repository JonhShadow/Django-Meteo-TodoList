const navSlide = () =>{
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.sidenav');
    const sidelinks = document.querySelectorAll('.sidenav a, .user-info');

    burger.addEventListener('click', () =>{
        nav.classList.toggle('sidenav-active');

        sidelinks.forEach((link) => {
            if (link.style.animation){
                link.style.animation = '';
            } else{
                link.style.animation = `sidenavFade 1s ease forwards`;
            }
        });
    });

}

navSlide();