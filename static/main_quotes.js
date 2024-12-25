addEventListener('DOMContentLoaded', doc_loaded => {

    const mybutton = document.getElementById('push')
    mybutton.addEventListener('click', function(event) {
      fetch('/api')
      .then(answer => answer.json())
      .then(data => {document.querySelector('#quote').innerText = data.quote
      })
    })
})