console.log("rodou o js")

const botaoAbrirModal = document.querySelector('.opcao-deletar')
const botaoConfirmar = document.querySelector('.botao-confirmar')
const botaoCancelar = document.querySelector('.botao-cancelar')

const modal = document.querySelector('.modal-background')

botaoAbrirModal.addEventListener('click', function() {
    modal.style.display = 'flex';
});

botaoCancelar.addEventListener('click', function() {
    modal.style.display = 'none';
});

botaoConfirmar.addEventListener('click', function() {
    // LOGICA DE DELECAO ESTA NA VIEW
    modal.style.display = 'none';
});
