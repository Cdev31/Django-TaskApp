const inputLoadImage=document.getElementById('load-image')
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
const onValidateInput=(event)=>{const inputs=[inputImage,inputTitle,inputDescription,inputCategory,inputDate,inputLevel]
const numberInputs=0
console.log(numberInputs)
while(inputs.length>=numberInputs){if(inputs[numberInputs].value?.length>0){numberInputs=numberInputs+1}
break}
if(numberInputs===6){event.target.disabled=false
event.target.style.backgroundColor='rgb(21 128 61)'}}
button.addEventListener('click',onValidateInput);const menu=document.getElementById('menu')
const menuButton=document.getElementById('open-menu-button')
const closeButton=document.getElementById('close-menu-button')
const openMenu=(event)=>{menu.style.display='flex'}
const closeMenu=(event)=>{menu.style.display='none'}
menuButton.addEventListener('click',openMenu)
closeButton.addEventListener('click',closeMenu);