function updateHeight() {
    $('main').css('height', 'auto');
    let bodyHeight = $(window).height() - $('footer').outerHeight();

    if ($(document).height() <= $(window).height()) {
        $('main').css('height', bodyHeight + 'px');
    }
}
$(document).ready(updateHeight);

$(window).on('resize', updateHeight);
// let bodyHeight = $(document).height() - $('footer').height();

// //Если высота экрана сходится с высотой документа
// if ($(window).height() == $(document).height()) {
//     $('main').css('height', bodyHeight + 'px');
// }