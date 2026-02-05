$('#reg-btn').click(
    function () {
        let nickname = $('#nickname').val()
        let password = $('#password').val()
        let email = $('#email').val()
        let codEmail = $('#cod-email').val()
        let passwordProverka = $('#password-proverka').val()
        let regButton = $('#reg-btn')
        const CSRF = $('[name=csrfmiddlewaretoken]').val()

        let userData = {
            'nickname': nickname,
            'password': password,
            'email': email,
            'codemail': codEmail,
            'passwordproverka': passwordProverka,
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
                    window.location.href = '/'; //переход на главную сайта
                },
        });

    }
);