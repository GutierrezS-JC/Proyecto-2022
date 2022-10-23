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

const warningAlert = (text) =>{
    Swal.fire({
      title: 'Cuidate cuidate',
      text: text,
      icon: 'warning',
      confirmButtonText: 'Ok'
    })
}

const questionAlert = (text, title='¿Seguro?') =>{
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
            Swal.fire(
              'Agregado!',
              'El socio fue agregado con exito',
              'success'
            )
        }
    })
}