$('#cryptographer-btn').click(
    function () {
        let cryptoBtn = $('#cryptographer-btn')
        const csrf = $('[name=csrfmiddlewaretoken]').val()
        const cryptographer_file = $('#cryptographer')[0].files;
        console.log(cryptographer_file);

        const fromData= new FormData()
        fromData.append('csrfmiddlewaretoken', csrf)
        fromData.append('cryptographer_file', cryptographer_file)

        console.log(fromData);

        $.ajax({
            url: '/cryptographer/',
            type: 'POST',
            data: fromData,
            processData: false,
            contentType: false,
        });

    }
);



