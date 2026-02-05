$('#codebreaker-btn').click(
    function () {
        let cdButton = $('#codebreaker-btn')
        const cdFile = $("codebreake").files;
        const CSRF = $('[name=csrfmiddlewaretoken]').val()

        let userData = {
            'cdfile': cdFile,
            'csrfmiddlewaretoken': CSRF
        }
        $.ajax({
            url: '/index/',
            type: 'POST',
            dataType: 'json',
            data: userData,

            success:
                function (data) {
                    console.log('Success: ', data);
                    cdButton.text('Успешно');
                    cdButton.prop('disabled', true);
                    cdButton.css({
                        'background-color': '#4CAF50',
                        'color': '#fff',
                    });
                },
        });

    }
);