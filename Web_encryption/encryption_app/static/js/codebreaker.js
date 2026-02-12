$('#codebreaker-btn').click(
    function () {
        let = $('#cryptographer-btn')
        const csrf = $('[name=csrfmiddlewaretoken]').val()
        const codebreaker_file = $('#codebreaker').file

        const fromData = new FormData()
        fromData.append('csrfmiddlewaretoken', csrf)
        fromData.append('codebreaker_files', codebreaker_file)

        $.ajax({
            url: '',
            type: 'POST',
            data: fromData,
            processData: false,
            contentType: false,
        });

    }
);