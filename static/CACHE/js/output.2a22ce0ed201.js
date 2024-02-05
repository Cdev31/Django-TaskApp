const inputLoadImage=document.getElementById('loadImage')
const previewIamge=document.getElementById('previewImage')
const preview=document.getElementById('preview')
const changePreviewImage=(event)=>{previewIamge.src=window.URL.createObjectURL(event.target.files[0])
preview.attributes.display=='none'}
inputLoadImage.addEventListener('change',changePreviewImage);