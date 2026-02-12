$('#cryptographer-btn').click(
    function () {
        let  = $('#cryptographer-btn')
        const csrf = $('[name=csrfmiddlewaretoken]').val()
        const cryptographer_file = $('#cryptographer').file

        const fromData= new FormData()
        fromData.append('csrfmiddlewaretoken', csrf)
        fromData.append('cryptographer_files', cryptographer_file)

        $.ajax({
            url: '',
            type: 'POST',
            data: fromData,
            processData: false,
            contentType: false,
        });

    }
);



