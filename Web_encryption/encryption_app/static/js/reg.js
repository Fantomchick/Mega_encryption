$('#reg-btn').click(
    function () {
        let nickname = $('#nickname').val()
        let password = $('#password').val()
        let email = $('#email').val()
        let codEmail = $('#cod-email').val()
        let regButton = $('#reg-btn')
        let passwordExamination = $('#password-examination').val()
        if (password !== passwordExamination){
            $('#password-examination').val('');
            $('#password-examination').attr('placeholder', 'Пароли не совпадают');
            $('#password-examination').css({
                'border': '1px solid red',
                'transtion': '0.3s',
            });
            $('#password-examination').addClass('error-plaseholder')
            return
        }

        const CSRF = $('[name=csrfmiddlewaretoken]').val()

        let userData = {
            'nickname': nickname,
            'password': password,
            'email': email,
            'codemail': codEmail,
            'csrfmiddlewaretoken': CSRF
        }
        $.ajax({
            url: '/reg/',
            type: 'POST',
            dataType: 'json',
            data: userData,

            success:
                function (data) {
                    console.log('Success: ', data);
                    regButton.text('Успешно');
                    regButton.prop('disabled', true);
                    regButton.css({
                        'background-color': '#4CAF50',
                        'color': '#fff',
                    });
                    window.location.href = '/'
                },
            error:
                function (data) {
                    console.log('Error: ', data);
                    regButton.text("Нет такого пользователя");
                    regButton.prop('disabled', false);
                    alert("Такой пользователь уже существует")
                }
        });

    }
);