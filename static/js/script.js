const inputLoadImage = document.getElementById('load-image')
const previewIamge = document.getElementById('previewImage')
const preview = document.getElementById('preview')
const button = document.getElementById('create-task-button')

const inputImage = document.getElementById('load-image')
const inputTitle = document.getElementById('title')
const inputDescription = document.getElementById('description')
const inputLevel = document.getElementById('level')
const inputCategory = document.getElementById('category')
const inputDate = document.getElementById('date')
const token = document.querySelector('[name="csrfmiddlewaretoken"]');
const form = document.getElementById('form-create-task')

const changePreviewImage = ( event ) => {
    previewIamge.src = window.URL.createObjectURL(event.target.files[0])
    preview.style.display = 'none'
}


inputLoadImage.addEventListener( 'change' , changePreviewImage )


const onValidateInput= ( event )=>{
   
    const inputs = [ inputImage, inputTitle, inputDescription, inputCategory, inputDate, inputLevel ]

    let numberInputs = 0

    while( inputs.length >= numberInputs ){
        
        if( inputs[numberInputs]?.value?.length > 0 ){
           numberInputs = numberInputs + 1
        }
        else if ( inputs[numberInputs]?.value?.length <= 0 ){
            break
        }
        else{
            break
        }
    }

    if( numberInputs === 6 ){
        event.target.disabled = false
        event.target.style.backgroundColor = 'rgb(21 128 61)'
        
        const formData = new FormData(form)
        formData.append('title', inputTitle.value)
        formData.append('description', inputDescription.value)
        formData.append('level', inputLevel.value)
        formData.append('taskImage', inputImage.files[0])
        formData.append('category', inputCategory.options[inputCategory.selectedIndex].id )
        formData.append('date', inputDate.value)

        fetch('/task/create/', {
            method: 'POST',
            headers:{
                'X-CSRFToken': token.value
            },
            body: formData
        })
        .then(()=> window.location.href ='/task')
    }
}



button.addEventListener('click', onValidateInput )
