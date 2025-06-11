console.log("rodou o jc")

// const botaoAbrirModal = document.querySelector('.opcao-deletar')
// const botaoConfirmar = document.querySelector('.botao-confirmar')
// const botaoCancelar = document.querySelector('.botao-cancelar')

// const modal = document.querySelector('.modal-background')

// botaoAbrirModal.addEventListener('click', function() {
//     modal.style.display = 'flex';
// });

// botaoCancelar.addEventListener('click', function() {
//     modal.style.display = 'none';
// });

// botaoConfirmar.addEventListener('click', function() {
//     // LOGICA DE DELECAO ESTA NA VIEW
//     modal.style.display = 'none';
// });

document.addEventListener('DOMContentLoaded', function() {
    var deleteButtons = document.querySelectorAll('.opcao-deletar');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            var modalId = button.getAttribute('data-modal-id');
            var modal = document.getElementById(modalId);
            if (modal) {
                modal.style.display = 'flex';
            }
        });
    });

    var cancelButtons = document.querySelectorAll('.botao-cancelar');
    cancelButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            var modal = button.closest('.modal-background');
            if (modal) {
                modal.style.display = 'none';
            }
        });
    });
});
