$('#cryptographer-btn').click(
    function () {
        let cryptoBtn = $('#cryptographer-btn')
        const csrf = $('[name=csrfmiddlewaretoken]').val()
        const cryptographer_file = $('#cryptographer')[0];
        const file = cryptographer_file.files[0]
        file_size = file.size
        console.log(cryptographer_file);
        console.log(file)

        const formData= new FormData()
        formData.append('csrfmiddlewaretoken', csrf)
        formData.append('cryptographer_file', file)
        if (file.size >1024 * 1024 * 1024) {
            alert('Размер файла больше 1 Гб')
            cryptographer.value = ''
            formData=''
            return false, formData;
        }
        console.log(formData);

        $.ajax({
            url: '/cryptographer/',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: 
                function (data) {
                    if (data.download_url) {
                        // создает невидимую ссылку и активирует ее
                        let link = document.createElement('a');
                        link.href = data.download_url;
                        link.download = ''; // Браузер предложит сохранить файл
                        document.body.appendChild(link);
                        link.click();
                        document.body.removeChild(link);
                        alert('Файл зашифрован и перемещен в загрузки');
                }
            },
            error:
                    function(error) {
                        console.error('Error', error);
                        alert(error.responseJSON.error);
            }
        });

    }
);
