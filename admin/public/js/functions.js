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