const eliminatedButton=document.querySelectorAll('.eliminated-category')
const eliminatedCategoryModal=document.getElementById('eliminated-category-modal')
const closeEliminatedButton=document.getElementById('close-eliminated-modal')
const confirmationEliminatedButton=document.querySelectorAll('.confirmation-eliminated ')
const onOpenEliminatedCategory=(event)=>{eliminatedCategoryModal.style.display='flex'}
const onCloseEliminatedCategory=(event)=>{eliminatedCategoryModal.style.display='none'}
const eliminatedCategory=(event)=>{eliminatedButton.forEach((button)=>{const categoryId=button.nextElementSibling.value
fetch(`/task/categories/delete/${categoryId}/`)})}
eliminatedButton.forEach((button)=>{button.addEventListener('click',onOpenEliminatedCategory)})
closeEliminatedButton.addEventListener('click',onCloseEliminatedCategory)
confirmationEliminatedButton.forEach((btn)=>{btn.addEventListener('click',eliminatedCategory)});const menu=document.getElementById('menu')
const menuButton=document.getElementById('open-menu-button')
const closeButton=document.getElementById('close-menu-button')
const openMenu=(event)=>{menu.style.display='flex'}
const closeMenu=(event)=>{menu.style.display='none'}
menuButton.addEventListener('click',openMenu)
closeButton.addEventListener('click',closeMenu);