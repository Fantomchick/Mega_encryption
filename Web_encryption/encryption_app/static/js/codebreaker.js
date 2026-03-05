$('#codebreaker-btn').click(
    function () {
        let codebreakBtn = $('#cryptographer-btn')
        const csrf = $('[name=csrfmiddlewaretoken]').val()
        const codebreaker_file = $('#codebreaker')[0];
        const file = codebreaker_file.files[0]
        console.log(codebreaker_file);
        console.log(file)

        const formData = new FormData()
        formData.append('csrfmiddlewaretoken', csrf)
        formData.append('codebreaker_file', file)

        console.log(formData);

        $.ajax({
            url: '/codebreaker/',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
        });

    }
);