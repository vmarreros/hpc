var hpc_software_request_saveForm = function () {
    var form = $(this);
    $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        cache: false,
        beforeSend: function () {
            ___HTML___application___hpc___modal___modal_content___modal_body___SHOW_LOAD___();
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                var $application___hpc___modal = $("#application___hpc___modal");
                if (data.___BOOLEAN___IS_VALID_FORM___) {
                    ___HTML___application___hpc___modal___SHOW_MESSAGE_OK___(data);
                }
                else {
                    $application___hpc___modal.html(data.___HTML___APPLICATION___HPC___MODAL___);
                    $application___hpc___modal.find(".modal___message").html(data.___HTML___APPLICATION___HPC___MODAL___MESSAGE___);
                }
            }
        }
    });
    return false;
};

$("#application___hpc___modal")
    .on("submit", "#hpc_software_request_submit", hpc_software_request_saveForm);
