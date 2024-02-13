const inputLoadImage=document.getElementById('loadImage')
const previewIamge=document.getElementById('previewImage')
const preview=document.getElementById('preview')
const button=document.getElementById('create-task-button')
const inputImage=document.getElementById('load-image')
const inputTitle=document.getElementById('title')
const inputDescription=document.getElementById('description')
const inputLevel=document.getElementById('level')
const inputCategory=document.getElementById('category')
const inputDate=document.getElementById('date')
const changePreviewImage=(event)=>{previewIamge.src=window.URL.createObjectURL(event.target.files[0])
preview.style.display='none'}
inputLoadImage.addEventListener('change',changePreviewImage)
const onInputDateChange=(event)=>{console.log(event.target.value)}
inputDate.addEventListener('change',onInputDateChange);const menu=document.getElementById('menu')
const menuButton=document.getElementById('open-menu-button')
const closeButton=document.getElementById('close-menu-button')
const openMenu=(event)=>{menu.style.display='flex'}
const closeMenu=(event)=>{menu.style.display='none'}
menuButton.addEventListener('click',openMenu)
closeButton.addEventListener('click',closeMenu);