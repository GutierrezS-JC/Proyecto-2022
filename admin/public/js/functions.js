const errorAlert = (text) =>{
    Swal.fire({
      title: 'Error!',
      text: text,
      icon: 'error',
      confirmButtonText: 'Ok'
    })
}

const successAlert = (text) =>{
    Swal.fire({
      title: 'Todo bien!',
      text: text,
      icon: 'success',
      confirmButtonText: 'Ok'
    })
}

const warningAlert = (text, title='Alerta') =>{
    Swal.fire({
      title: title,
      text: text,
      icon: 'warning',
      confirmButtonText: 'Ok'
    })
}

const questionAlert = (text, doc_num, disciplineId, title='¿Seguro?') =>{
    Swal.fire({
      title: title,
      text: text,
      icon: 'question',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Confirmar',
      cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed){
            window.location.href = `/disciplines/agregar_socio_disciplina/${doc_num}/${disciplineId}`
        }
    })
}