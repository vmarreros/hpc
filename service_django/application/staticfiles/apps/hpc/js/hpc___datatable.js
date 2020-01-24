dtresponsive = true;
dtlanguage = {
        "sProcessing":     gettext('DATATABLE_Processing'),
        "sLengthMenu":     gettext('DATATABLE_Length_Menu'),
        "sZeroRecords":    gettext('DATATABLE_Zero_Records'),
        "sEmptyTable":     gettext('DATATABLE_Empty_Table'),
        "sInfo":           gettext('DATATABLE_Info'),
        "sInfoEmpty":      gettext('DATATABLE_Info_Empty'),
        "sInfoFiltered":   gettext('DATATABLE_Info_Filtered'),
        "sInfoPostFix":    "",
        "sSearch":         gettext('DATATABLE_Search'),
        "sUrl":            "",
        "sInfoThousands":  ",",
        "sLoadingRecords": gettext('DATATABLE_Loading_Records'),
        "oPaginate": {
            "sFirst":    gettext('DATATABLE_First'),
            "sLast":     gettext('DATATABLE_Last'),
            "sNext":     gettext('DATATABLE_Next'),
            "sPrevious": gettext('DATATABLE_Previous')
        },
        "oAria": {
            "sSortAscending":  gettext('DATATABLE_Sort_Ascending'),
            "sSortDescending": gettext('DATATABLE_Sort_Descending')
        }
    };
dtsPaginationType = 'numbers';

var dataTableStyles = function () {
    $('.dataTables_length').addClass('col-sm-6').css('padding', '0');
    $('.dataTables_filter').addClass('col-sm-6').css('padding', '0');
};

$('#application___hpc___content___center')
    .on('nodes', '#nodes___datatable', function(){
        $(this).DataTable({
            dom: "lfrtip",
            responsive: dtresponsive,
            language: dtlanguage,
            sPaginationType: dtsPaginationType
        });
        dataTableStyles()
    })
    .on('software', '#software___datatable', function(){
        $(this).DataTable({
            dom: "lfrtip",
            responsive: dtresponsive,
            language: dtlanguage,
            sPaginationType: dtsPaginationType
        });
        dataTableStyles()
    })
    .on('jobs', '#jobs___datatable', function(){
        $(this).DataTable({
            dom: "Blfrtip",
            buttons: [
                {
                    extend: "pdf",
                    text: "pdf",
                    className: "btn-primary btn-sm",
                    exportOptions: {
                        columns: [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ] //':visible'
                    }
                },
                {
                    extend: "print",
                    text: "print",
                    className: "btn-primary btn-sm",
                    exportOptions: {
                        columns: [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ] //':visible'
                    }
                },
                {
                    extend: "csv",
                    text: "csv",
                    className: "btn-primary btn-sm",
                    exportOptions: {
                        columns: [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ] //':visible'
                    }
                }
            ],
            ajax: {
                url: $(this).attr('data-url-jobs'),
                type: "GET",
                dataSrc: function(response) {
                    if(response['___BOOLEAN___ERROR___']){
                        ___HTML___application___hpc___modal___SHOW_LOAD___();
                        ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(response);
                        return [];
                    }
                    else {
                        for (var i=0; i<response.data.length; i++ ) {
                            if(response.data[i][2].length > 15)
                                response.data[i][2] = response.data[i][2].slice(0,14)+'...';
                            if(response.data[i][3].length > 15)
                                response.data[i][3] = response.data[i][3].slice(0,14)+'...';
                            response.data[i][6] = capitalize(response.data[i][6])
                        }
                        return response.data;
                    }
                }
            },
            columnDefs: [
                {
                    "render": function ( data/*, type, row*/ ) {
                        return '<span class="label" data-background-color="'+bg_job_state(data)+'">' + data + '</span>'
                    },
                    "targets": 1
                },
                {
                    "render": function ( data/*, type, row*/ ) {
                        return data
                    },
                    "targets": 0
                }
            ],
            aoColumns: [
                null,
                null,
                null,
                null,
                null,
                null,
                null,
                null,
                null,
                {
                    "data" : '',
                    "defaultContent": '<span class="fa fa-spinner fa-pulse fa-lg fa-4x"></span>',
                    "orderable": false,
                    "searchable": false
                }
            ],
            responsive: dtresponsive,
            language: dtlanguage,
            sPaginationType: dtsPaginationType
        });
        dataTableStyles()
    })
    .on('history', '#history___datatable', function(){
        $(this).DataTable({
            dom: "lfrtip",
            ajax: {
                url: $(this).attr('data-url'),
                type: "GET",
                data: function ( d ) {
                    d.date = $('#history-search').val();
                },
                dataSrc: function(response) {
                    if(response['___BOOLEAN___ERROR___']){
                        ___HTML___application___hpc___modal___SHOW_LOAD___();
                        ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(response);
                        return [];
                    }
                    else {
                        for (var i=0; i<response.data.length; i++) {
                            response.data[i][1] = response.data[i][1].split(' ')[0]
                        }
                        return response.data;
                    }
                }
            },
            columnDefs: [
                {
                    "render": function ( data/*, type, row*/ ) {
                        return '<span class="label" data-background-color="'+bg_job_state(data)+'">' + data + '</span>'
                    },
                    "targets": 1
                },
            ],
            responsive: dtresponsive,
            language: dtlanguage,
            sPaginationType: dtsPaginationType
        });
        dataTableStyles()
    })
    .on("submit", "#hpc_job_history_search", function(evt){
        evt.preventDefault();
        $('#history___datatable').DataTable().clear().draw();
        $('#history___datatable').DataTable().ajax.reload();
    });
