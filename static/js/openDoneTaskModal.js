const completedButton = document.querySelectorAll('.completed-task')
const completedTaskModal = document.getElementById('completed-task-modal')
const closeCompletedButton = document.getElementById('close-completed-eliminated-modal')
const confirmationCompletedButton = document.querySelectorAll('.confirmation-completed')
const taskCompletedId = document.getElementById('task-completed-id')



const onOpenCompletedTask = ( event )=>{
    const button = event.target
    completedTaskModal.style.display = 'flex'
    taskCompletedId.value = button.nextElementSibling.value
}


const onCloseCompletedTask = ( event )=>{
    completedTaskModal.style.display = 'none'
}

const completedTask = ( event )=>{
    const clickButton = event.target
    const taskId = clickButton.nextElementSibling.value
    
    fetch(`/task/completed/${taskId}/`)
    .then(() => {
        window.location.href="/task/"
    })
}

completedButton.forEach(( button )=>{
    button.addEventListener( 'click' , onOpenCompletedTask)
})

closeCompletedButton.addEventListener( 'click',  onCloseCompletedTask)

confirmationCompletedButton.forEach(( btn )=>{
    btn.addEventListener( 'click', completedTask )
   
})