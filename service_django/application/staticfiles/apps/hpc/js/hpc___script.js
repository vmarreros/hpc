var hpc_script_submit = function(evt){
    evt.preventDefault();
    var $form = $(this);
    var $btn = $form.find('div.form-group').find('button.active');
    var formData = new FormData(this);
    $.ajax({
        url: $form.attr("action"),
        data: formData,
        type: $form.attr("method"),
        dataType: "json",
        cache: false,
        processData: false,
        contentType: false,
        beforeSend: function () {
            ___HTML___modal___SHOW_LOAD___();
        },
        success: function (data) {
            var $application___hpc___content___center = $("#application___hpc___content___center");
            if (data['___BOOLEAN___ERROR___']) {
                ___HTML___modal___SHOW_MESSAGE_ERROR___(data);
                $application___hpc___content___center.html(data['___HTML___CONTENT___CENTER___']);
            }
            else {
                $application___hpc___content___center.html(data['___HTML___CONTENT___CENTER___']);
                ___HTML___modal___SHOW_MESSAGE_OK___(data);
            }
        }
    });
};

var hpc_script_run = function(){
    var $form = $('.form-hpc-script-submit'),
        $btn = $(this);
    var formData = new FormData($form[0]);
    formData.append('run', true);
    formData.append('csrfmiddlewaretoken', $form.find("input[name='csrfmiddlewaretoken']").val());
    $.ajax({
        url: $form.attr("action"),
        data: formData,
        type: $form.attr("method"),
        dataType: "json",
        cache: false,
        processData: false,
        contentType: false,
        beforeSend: function () {
            ___HTML___modal___SHOW_LOAD___();
        },
        success: function (data) {
            var $application___hpc___content___center = $("#application___hpc___content___center");
            if (data['___BOOLEAN___ERROR___']) {
                ___HTML___modal___SHOW_MESSAGE_ERROR___(data);
                $application___hpc___content___center.html(data['___HTML___CONTENT___CENTER___']);
            }
            else {
                $application___hpc___content___center.html(data['___HTML___CONTENT___CENTER___']);
                ___HTML___modal___SHOW_MESSAGE_OK___(data);
            }
        }
    });
};

$("#application___hpc___content")
    .on("submit", ".form-hpc-script-submit", hpc_script_submit)
    .on("click", ".form-hpc-script-run", hpc_script_run);