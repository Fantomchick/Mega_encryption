//   $('#cryptographer-btn').click(
//     function () {
//         let crButton = $('#cryptographer-btn')
//         const crFile = $("codebreake").files;
//         const CSRF = $('[name=csrfmiddlewaretoken]').val()

//         let userData = {
//             'crfile': crFile,
//             'csrfmiddlewaretoken': CSRF
//         }
//         $.ajax({
//             url: '/index/',
//             type: 'POST',
//             dataType: 'json',
//             data: userData,

//             success:
//                 function (data) {
//                     console.log('Success: ', data);
//                     crButton.text('Успешно');
//                     crButton.prop('disabled', true);
//                     crButton.css({
//                         'background-color': '#4CAF50',
//                         'color': '#fff',
//                     });
//                 },
//         });

//     }
// );
document.getElementById('cryptographer-btn').addEventListener('click', () => {
    const cryptographer = document.getElementById('cryptographer');
    const file = cryptographer.files[0];
    const formData = new FormData();
    formData.append('file', file);
    // Добавьте CSRF-токен, если необходимо
    formData.append('csrfmiddlewaretoken', '{{ csrf_token }}');

    fetch('', {
        method: 'POST',
        body: formData
    })
});

