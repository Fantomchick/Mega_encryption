$('#auth-btn').click(
    function () {
        let nickname = $('#nickname').val()
        let password = $('#password').val()
        let authButton = $('#auth-btn')
        const CSRF = $('[name=csrfmiddlewaretoken]').val()

        let userData = {
            'nickname': nickname,
            'password': password,
            'csrfmiddlewaretoken': CSRF
        }
        $.ajax({
            url: '/auth/',
            type: 'POST',
            dataType: 'json',
            data: userData,

            success:
                function (data) {
                    console.log('Success: ', data);
                    authButton.text('Успешно');
                    authButton.prop('disabled', true);
                    window.location.href = '/'; //переход на главную сайта
                },//переход на главную сайта
            error:
                function (data) {
                    console.log('Error: ', data);
                    authButton.text("Нет такого пользователя");
                    authButton.prop('disabled', false);
                    alert("Нет такого пользователя")
                },
        })
    }
)