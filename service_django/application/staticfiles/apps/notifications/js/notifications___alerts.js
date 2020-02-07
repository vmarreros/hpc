$('#application___notifications___content')
    .on('click', '.LINK___alert___delete', function(){
        var $link = $(this);
        var $parent = $link.closest('.list-group-item');
        $.ajax({
            url: $link.attr("data-url"),
            type: "post",
            dataType: "json",
            cache: false,
            success: function (data) {
                if (data["___BOOLEAN___ERROR___"]) {
                    console.log('error')
                }
                else {
                    $parent.animate({
                        opacity: "toggle"
                    }, 1000, "linear", function() {
                        $parent.remove();
                        $(".list-group-message").removeClass('hidden')
                    });
                    ___HTML___header___RELOAD___()
                }
            }
        });
    })
    .on('click', '.LINK___alert___unread', function(){
        var $link = $(this);
        var $parent = $link.closest('.list-group-item');
        $.ajax({
            url: $link.attr("data-url"),
            type: "post",
            dataType: "json",
            cache: false,
            success: function (data) {
                if (data["___BOOLEAN___ERROR___"]) {
                    console.log('error')
                }
                else {
                     $parent.toggleClass('active');
                    ___HTML___header___RELOAD___()
                }
            }
        });
    });
