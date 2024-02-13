const inputLoadImage=document.getElementById('loadImage')
const previewIamge=document.getElementById('previewImage')
const preview=document.getElementById('preview')
const changePreviewImage=(event)=>{previewIamge.src=window.URL.createObjectURL(event.target.files[0])
preview.style.display='none'}
inputLoadImage.addEventListener('change',changePreviewImage);const menu=document.getElementById('menu')
const menuButton=document.getElementById('open-menu-button')
const closeButton=document.getElementById('close-menu-button')
const openMenu=(event)=>{menu.style.display='flex'}
const closeMenu=(event)=>{menu.style.display='none'}
menuButton.addEventListener('click',openMenu)
closeButton.addEventListener('click',closeMenu);