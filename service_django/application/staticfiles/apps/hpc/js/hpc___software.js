var hpc_software_request_saveForm = function () {
    var form = $(this);
    $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        cache: false,
        beforeSend: function () {
            ___HTML___modal___modal_content___modal_body___SHOW_LOAD___();
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                var $site___modal = $("#site___modal");
                if (data.___BOOLEAN___IS_VALID_FORM___) {
                    ___HTML___modal___SHOW_MESSAGE_OK___(data);
                }
                else {
                    $site___modal.html(data.___HTML___MODAL___);
                    $site___modal.find(".modal___message").html(data.___HTML___MODAL___MESSAGE___);
                }
            }
        }
    });
    return false;
};

$("#site___modal")
    .on("submit", "#hpc_software_request_submit", hpc_software_request_saveForm);
