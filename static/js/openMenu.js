const menu = document.getElementById('menu')
const menuButton = document.getElementById('open-menu-button')
const closeButton = document.getElementById('close-menu-button')


const openMenu = ( event )=>{
    menu.style.display = 'flex'
}

const closeMenu = ( event )=>{
    menu.style.display = 'none'
}

menuButton.addEventListener('click', openMenu)
closeButton.addEventListener('click', closeMenu)
