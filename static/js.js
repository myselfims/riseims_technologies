let sidebar = false

let srvdiv = document.querySelector('.services-div')

function SideBarToggle(){
    if (sidebar === true){
        document.getElementById('sidebar').style.display = 'none';
        sidebar = false;
        document.getElementById('sidebartoggelbtn').style.color = 'black';
        
        try{
            srvdiv.classList.add('.services-div')

        }catch{

        }
        // document.body.classList.remove("scroll-lock");
    }else{
   
        try{
            srvdiv.classList.remove('.services-div')

        }catch{

        }
        document.getElementById('sidebartoggelbtn').style.color = 'white';
        document.getElementById('sidebar').style.display = 'flex';
        // document.body.classList.add("scroll-lock");
        sidebar = true;
        
    }
}


var myNav = document.getElementById('navcontainer');
window.onscroll = function () { 
    if (document.body.scrollTop >= 200 || document.documentElement.scrollTop >= 200 ){
        myNav.classList.add("nav-colored");
        myNav.classList.remove("nav-transparent");
    } 
    else {
        myNav.classList.add("nav-transparent");
        myNav.classList.remove("nav-colored");
    }
};