function capitalize(s){
    return s.toLowerCase().replace(/\b./g, function(a){
        return a.toUpperCase();
    });
}

function bg_job_state(state){
    if(state==='PENDING')
        return "red";
    if(state==='RUNNING')
        return "blue";
    if(state==='SUSPENDED')
        return "darker";
    if(state==='CANCELLED')
        return "orange";
    if(state==='COMPLETING')
        return "purple";
    if(state==='COMPLETED')
        return "green";
    if(state==='FAILED')
        return "red";
    if(state==='TIMEOUT')
        return "red";
    if(state==='NODE_FAIL')
        return "red";
    return "";
}

var hpc_jobs_datatable_detail = function() {
    var $table = $('#jobs___datatable');
    var tr = $(this).closest('tr');
    if (tr.hasClass('parent')) {
        var datatable = $table.DataTable();
        var row = datatable.row(tr).index();
        $.getJSON($table.attr('data-url-detail'), {'jobid': datatable.cell(row, 0).data()}, function (data) {
            if (data['___BOOLEAN___ERROR___']) {
                ___HTML___application___hpc___modal___SHOW_LOAD___();
                ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                var text = $(data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___']).find('.alert___message___text').text();
                datatable.cell(row, 9).data(text).page(datatable.page()).draw('page');
            }
            else {
                datatable.cell(row, 9).data(data.detail).page(datatable.page()).draw('page');
            }
        }).always(function () {
        });
    }
};

var hpc_jobs_datatable_actionJob = function(){
    var datatable = $('#jobs___datatable').DataTable();
    var tr = $(this).closest('tr').prev();
    var row = datatable.row(tr).index();
    $.ajax({
        url: $(this).attr('data-url'),
        data: {
            'option': $(this).attr('data-option'),
            'jobID': datatable.cell(row, 0).data()
        },
        type: 'post',
        dataType: "json",
        cache: false,
        beforeSend: function () {

        },
        success: function (data) {
            if(data['___BOOLEAN___ERROR___']){
                ___HTML___application___hpc___modal___SHOW_LOAD___();
                ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                datatable.cell(row, 1).data($(data.detail).find('.panel-heading').find('span').text());
                datatable.cell(row, 9).data(data.detail).page(datatable.page()).draw('page');
            }
        }
    });
};

$('#application___hpc___content___center')
    .on('click', '#jobs___datatable tbody td:first-child', hpc_jobs_datatable_detail)
    .on('click', '.panel-heading button:nth-child(1)', hpc_jobs_datatable_actionJob)
    .on('click', '.panel-heading button:nth-child(2)', hpc_jobs_datatable_actionJob)
    .on('click', '.panel-heading button:nth-child(3)', hpc_jobs_datatable_actionJob)
    .on('click', '.panel-heading button:nth-child(4)', hpc_jobs_datatable_actionJob);
