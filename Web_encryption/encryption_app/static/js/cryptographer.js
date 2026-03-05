$('#cryptographer-btn').click(
    function () {
        let cryptoBtn = $('#cryptographer-btn')
        const csrf = $('[name=csrfmiddlewaretoken]').val()
        const cryptographer_file = $('#cryptographer')[0];
        const file = cryptographer_file.files[0]
        console.log(cryptographer_file);
        console.log(file)

        const formData= new FormData()
        formData.append('csrfmiddlewaretoken', csrf)
        formData.append('cryptographer_file', file)

        console.log(formData);

        $.ajax({
            url: '/cryptographer/',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
        });

    }
);



