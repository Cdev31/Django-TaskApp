const inputLoadImage=document.getElementById('loadImage')
const previewIamge=document.getElementById('previewImage')
const changePreviewImage=(event)=>{previewIamge.src=window.URL.createObjectURL(event.target.files[0])}
inputLoadImage.addEventListener('change',changePreviewImage);