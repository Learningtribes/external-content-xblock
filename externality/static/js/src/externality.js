//$(document).ready(
$(document).on("hover", ".supported-tags-nav > li",
    function ExternalContentXBlock(runtime, element) {
        $(function ($) {
            /* Here's where you'd do things on page load. */
        });

        window.onload = function() {
            setTimeout(function() {
                var data = {
                    'completion': 1.0,
                };
                var handlerUrl = runtime.handlerUrl(element, 'publish_completion');

                $.post(handlerUrl, JSON.stringify(data)).complete(function() {});
            }, 1000);

        };

        function updateResList(activeTab) {
            // const $listing = $('.supported-resources');
            var $resources = $(".supported-resources li.resource-item");
            var activeStatus = activeTab;

            $resources.each(function () {
                if (activeStatus == 'all-tags' || $(this).data('status').split(',').includes(activeStatus) ) {
                    $(this).show();
                } else {
                    $(this).hide();
                }
            })

            // if (Array.from($courses).every(p=>$(p).css('display')=='none')) {
            //     $('.empty-tab-message').removeClass('hidden')
            //     $listing.addClass('hidden')
            // }else {
            //     $('.empty-tab-message').addClass('hidden')
            //     $listing.removeClass('hidden')
            // }
        }

        $('.supported-tags-nav > li', element).bind('click', function() {
            $(this).find('.btn-link').addClass('active-section');
            $(this).siblings().find('.btn-link').removeClass('active-section');
            updateResList($(this).attr('id'));

        });

    }
)
