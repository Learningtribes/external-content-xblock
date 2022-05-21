/* Javascript for ExternalContentXBlock. */
function ExternalContentXBlock(runtime, element) {

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });

    var handlerUrl = runtime.handlerUrl(element, 'studio_submit');

    $('.save-button', element).bind('click', function() {
        var data = {
            'iframe_url': $('#iframe_url').val(),
        };

        $.post(handlerUrl, JSON.stringify(data)).complete(function() {
            window.location.reload(false);
        });
    });

    $('.cancel-button', element).bind('click', function() {
        runtime.notify('cancel', {});
    });

    if (LearningTribes && LearningTribes.QuestionMark) {
        $wrappers = $('.wrapper-comp-settings .question-mark-wrapper')
        $wrappers.each(function(i, wrapper){
            new LearningTribes.QuestionMark(wrapper)
        })
    }
}
