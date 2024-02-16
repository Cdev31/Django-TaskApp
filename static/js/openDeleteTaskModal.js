const eliminatedButton = document.querySelectorAll('.eliminated-task')
const eliminatedTaskModal = document.getElementById('eliminated-task-modal')
const closeEliminatedButton = document.getElementById('close-eliminated-modal')
const confirmationEliminatedButton = document.querySelectorAll('.confirmation-eliminated')
const taskId = document.getElementById('task-id')



const onOpenEliminatedTask = ( event )=>{
    const button = event.target
    eliminatedTaskModal.style.display = 'flex'
    taskId.value = button.nextElementSibling.value
}


const onCloseEliminatedTask = ( event )=>{
    eliminatedTaskModal.style.display = 'none'
}

const eliminatedTask = ( event )=>{
    const clickButton = event.target
    const taskId = clickButton.nextElementSibling.value
    
    fetch(`/task/delete/${taskId}/`)
    .then(() => {
        window.location.href="/task/"
    })
}

eliminatedButton.forEach(( button )=>{
    button.addEventListener( 'click' , onOpenEliminatedTask)
})

closeEliminatedButton.addEventListener( 'click',  onCloseEliminatedTask)

confirmationEliminatedButton.forEach(( btn )=>{
    btn.addEventListener( 'click', eliminatedTask )
   
})