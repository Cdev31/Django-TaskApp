const eliminatedButton = document.querySelectorAll('.eliminated-category')
const eliminatedCategoryModal = document.getElementById('eliminated-category-modal')
const closeEliminatedButton = document.getElementById('close-eliminated-modal')
const confirmationEliminatedButton = document.querySelectorAll('.confirmation-eliminated ')
const categoryId = document.getElementById('category-id')



const onOpenEliminatedCategory = ( event )=>{
    const button = event.target
    eliminatedCategoryModal.style.display = 'flex'
    categoryId.value = button.nextElementSibling.value
}


const onCloseEliminatedCategory = ( event )=>{
    eliminatedCategoryModal.style.display = 'none'
}

const eliminatedCategory = ( event )=>{
    const clickButton = event.target
    const categoryId = clickButton.nextElementSibling.value
    
    fetch(`/task/categories/delete/${categoryId}/`)
    .then(() => {
        window.location.reload();  
    })
}

eliminatedButton.forEach(( button )=>{
    button.addEventListener( 'click' , onOpenEliminatedCategory)
})

closeEliminatedButton.addEventListener( 'click',  onCloseEliminatedCategory)

confirmationEliminatedButton.forEach(( btn )=>{
    btn.addEventListener( 'click', eliminatedCategory )
   
})