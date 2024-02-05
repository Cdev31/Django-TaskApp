const inputLoadImage=document.getElementById('loadImage')
const previewIamge=document.getElementById('previewImage')
const changePreviewImage=(event)=>{console.log(event.target.files[0])}
document.addEventListener(inputLoadImage,changePreviewImage);