// $('#codebreaker-btn').click(
//     function () {
//         let cdButton = $('#codebreaker-btn')
//         const cdFile = $("codebreake").files;
//         const CSRF = $('[name=csrfmiddlewaretoken]').val()

//         let userData = {
//             'cdfile': cdFile,
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
//                     cdButton.text('Успешно');
//                     cdButton.prop('disabled', true);
//                     cdButton.css({
//                         'background-color': '#4CAF50',
//                         'color': '#fff',
//                     });
//                 },
//         });

//     }
// );
document.getElementById('codebreaker-btn').addEventListener('click', () => {
    const codebreaker = document.getElementById('codebreaker');
    const file = codebreaker.files[0];
    const formData = new FormData();
    formData.append('file', file);
    // Добавьте CSRF-токен, если необходимо
    formData.append('csrfmiddlewaretoken', '{{ csrf_token }}');

    fetch('', {
        method: 'POST',
        body: formData
    })
});