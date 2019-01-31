function getCookie(c_name) {
    if (document.cookie.length > 0)
    {
        var c_start = document.cookie.indexOf(c_name + "=");
        if (c_start !== -1)
        {
            c_start = c_start + c_name.length + 1;
            var c_end = document.cookie.indexOf(";", c_start);
            if (c_end === -1) c_end = document.cookie.length;
            return decodeURI(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}

var hpc_explorer_init = function(){
    const
        $hpc__content__center = $('#application___hpc___content___center'),
        $hpc__modal =  $('#application___hpc___modal'),
        $hpc__tbody =  $hpc__content__center.find('#explorer___content').find('#tableFileSystem').find('tbody'),
        $hpc__buttons = $hpc__content__center.find('#explorer___content').find('#actionsFileSystem'),
        url_list =  $hpc__content__center.find('#explorer___content').find('#tableFileSystem').attr('data-url-list'),
        url_error =  $hpc__content__center.find('#explorer___content').find('#tableFileSystem').attr('data-url-error'),
        home =  $hpc__content__center.find('#explorer___content').find('#tableFileSystem').attr('data-home');
    var filesToCopy = [];

    function breadcumbs (p) {
        var $breadcumbs = $hpc__content__center.find('#explorer___content').find('#printWorkingDirectory'),
            pwd = p.split("/"),
            i = 1;
        $breadcumbs.html('<a data-path="' + pwd.slice(0,4).join("/") + '"><span class="glyphicon glyphicon-home" aria-hidden="true"></span></a>');
        pwd.slice(4).forEach(function(e){
            $breadcumbs.append('&nbsp;/&nbsp;<a data-path="' + pwd.slice(0,4+i).join("/") + '">' + e + '</a>');
            i++;
        });
    }

    var hpc__explorer__btn__disable = function(){
        $hpc__buttons.find('a[data-option]').each(function(){
            $(this).attr('disabled', 'disabled');
        });
        $hpc__buttons.find('li[data-option]').each(function(){
            $(this).addClass('disabled');
        });
    };
    var hpc__explorer__btn__enable = function(){
        hpc__explorer__btn__disable();
        var i = 0, count = 0, d = false, f = false;
        $hpc__tbody.find('tr').each(function(){
            if($(this).hasClass('primary')) {
                i++;
                if ($(this).attr('data-type') === 'directory')
                    d = true;
                if ($(this).attr('data-type') === 'file')
                    f = true;
            }
            count++;
        });
        $hpc__buttons.find('a[data-option="goto"]').removeAttr('disabled');
        $hpc__buttons.find('a[data-option="unselect-all"]').removeAttr('disabled');
        $hpc__buttons.find('a[data-option="select-all"]').removeAttr('disabled');
        $hpc__buttons.find('a[data-option="folder"]').removeAttr('disabled');
        $hpc__buttons.find('a[data-option="file"]').removeAttr('disabled');
        $hpc__buttons.find('li[data-option="file"]').removeClass('disabled');
        $hpc__buttons.find('a[data-option="upload"]').removeAttr('disabled');
        if(path !== home)
            $hpc__buttons.find('a[data-option="back"]').removeAttr('disabled');
        if(i === 1) {
            $hpc__buttons.find('a[data-option="rename"]').removeAttr('disabled');
            $hpc__buttons.find('li[data-option="rename"]').removeClass('disabled');
            if (d)
                $hpc__buttons.find('a[data-option="open"]').removeAttr('disabled');
            if (f) {
                $hpc__buttons.find('a[data-option="edit"]').removeAttr('disabled');
                $hpc__buttons.find('li[data-option="edit"]').removeClass('disabled');
                $hpc__buttons.find('a[data-option="execute"]').removeAttr('disabled');
                $hpc__buttons.find('li[data-option="execute"]').removeClass('disabled');
            }
        }
        if(i > 0){
            $hpc__buttons.find('a[data-option="download"]').removeAttr('disabled');
            $hpc__buttons.find('a[data-option="download-small"]').removeAttr('disabled');
            $hpc__buttons.find('a[data-option="copy"]').removeAttr('disabled');
            $hpc__buttons.find('li[data-option="copy"]').removeClass('disabled');
            $hpc__buttons.find('a[data-option="delete"]').removeAttr('disabled');
            $hpc__buttons.find('li[data-option="delete"]').removeClass('disabled');
        }
        if(filesToCopy.length > 0){
            $hpc__buttons.find('li[data-option="paste"]').removeClass('disabled');
            $hpc__buttons.find('a[data-option="paste"]').removeAttr('disabled');
        }
        if(i === count)
            $hpc__buttons.find('a[data-option="select-all"]').attr('data-option', 'unselect-all').find('span').eq(0).removeClass('glyphicon-check').addClass('glyphicon-unchecked');
        else
            $hpc__buttons.find('a[data-option="unselect-all"]').attr('data-option', 'select-all').find('span').eq(0).removeClass('glyphicon-unchecked').addClass('glyphicon-check');
    };
    var hpc__explorer__list = function(){
        hpc__explorer__btn__disable();
        $.getJSON(url_list, {'path': path}, function(data) {
            if(data['___BOOLEAN___ERROR___']){
                ___HTML___application___hpc___modal___SHOW_LOAD___();
                ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
               $(data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___']).find('.alert___message___text').text();
            }
            else {
                $hpc__tbody.html(data.list);
                breadcumbs(path);
                hpc__explorer__btn__enable();
            }
        }).always(function() {});
    };
    hpc__explorer__list();

    $hpc__content__center.find('#explorer___content').find('#printWorkingDirectory').on('click', 'a', function(){
        path = $(this).attr('data-path');
        $hpc__tbody.html('<tr><td colspan="3"><span class="fa fa-spinner fa-pulse"></span> Cargando...</td></tr>');
        hpc__explorer__list()
    });

    /*<<<<<<<<*/
    var hpc__explorer__action__activeRow = function (event) {
        if(event.ctrlKey) {
            if ($(this).hasClass('primary'))
                $(this).removeClass('primary');
            else
                $(this).addClass('primary');
        }
        else{
            $(this).parent().find('tr').each(function(){
                $(this).removeClass('primary');
            });
            $(this).addClass('primary');
        }
        hpc__explorer__btn__enable();
    };
    var hpc__explorer__action__dblClick = function() {
        if ($(this).attr('data-type') === 'directory') {
            path = path + '/' + $(this).attr('data-name');
            $hpc__tbody.html('<tr><td colspan="3"><span class="fa fa-spinner fa-pulse"></span> Cargando...</td></tr>');
            hpc__explorer__list();
        }
    };
    $hpc__tbody
        .on('click', 'tr', hpc__explorer__action__activeRow)
        .on('dblclick', 'tr', hpc__explorer__action__dblClick);
    /*>>>>>>>>*/


    /*<<<<<<<<*/
    var hpc__explorer__a__back = function(){
        if($(this).attr('disabled')!=='disabled') {
            $(this).attr('disabled', 'disabled');
            var tmp = path.split('/');
            if (tmp.length)
                tmp.pop();
            path = tmp.join('/');
            $hpc__tbody.html('<tr><td colspan="3"><span class="fa fa-spinner fa-pulse"></span> Cargando...</td></tr>');
            hpc__explorer__list();
        }
    };
    var hpc__explorer__a__open = function(){
        if($(this).attr('disabled')!=='disabled') {
            $(this).attr('disabled', 'disabled');
            path += '/' + $hpc__tbody.find('tr.primary').attr('data-name');
            $hpc__tbody.html('<tr><td colspan="3"><span class="fa fa-spinner fa-pulse"></span> Cargando...</td></tr>');
            hpc__explorer__list();
        }
    };
    var hpc__explorer__a__edit = function(){
        if($(this).attr('disabled')!=='disabled') {
            $(this).attr('disabled', 'disabled');
            var data = {
                file_name: $hpc__tbody.find('tr.primary').attr('data-name'),
                path: path
            };
            $.ajax({
                url: $(this).attr('data-url'),
                type: 'GET',
                data: data,
                dataType: 'json',
                beforeSend: function () {
                    ___HTML___application___hpc___modal___SHOW_LOAD___();
                },
                success: function (data) {
                    if (data['___BOOLEAN___ERROR___']) {
                        ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data, 10000);
                    }
                    else {
                        $hpc__modal.html(data['___HTML___APPLICATION___HPC___MODAL___']);
                        $hpc__modal.find('.modal___message').html(data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___']);
                        ___HTML___application___hpc___modal___EVENTS_ON___();
                    }
                    hpc__explorer__btn__enable();
                }
            });
        }
    };
    var hpc__explorer__li__edit = function(){
        if(!$(this).hasClass('disabled')) {
            $(this).addClass('disabled');
            var data = {
                file_name: $hpc__tbody.find('tr.primary').attr('data-name'),
                path: path
            };
            $.ajax({
                url: $(this).attr('data-url'),
                type: 'GET',
                data: data,
                dataType: 'json',
                beforeSend: function () {
                    ___HTML___application___hpc___modal___SHOW_LOAD___();
                },
                success: function (data) {
                    if (data['___BOOLEAN___ERROR___']) {
                        ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data, 10000);
                    }
                    else {
                        $hpc__modal.html(data['___HTML___APPLICATION___HPC___MODAL___']);
                        $hpc__modal.find('.modal___message').html(data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___']);
                        ___HTML___application___hpc___modal___EVENTS_ON___();
                    }
                    hpc__explorer__btn__enable();
                }
            });
        }
    };
    var hpc__explorer__a__rename = function(){
        if($(this).attr('disabled')!=='disabled') {
            $(this).attr('disabled', 'disabled');
            $.ajax({
                url: $(this).attr('data-url'),
                type: 'GET',
                dataType: 'json',
                beforeSend: function () {
                    ___HTML___application___hpc___modal___SHOW_LOAD___();
                },
                success: function (data) {
                    if (data['___BOOLEAN___ERROR___']) {
                        ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                    }
                    else {
                        $hpc__modal.html(data['___HTML___APPLICATION___HPC___MODAL___']);
                        $hpc__modal.find('.modal___message').html(data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___']);
                        ___HTML___application___hpc___modal___EVENTS_ON___();
                    }
                }
            });
        }
    };
    var hpc__explorer__li__rename = function(){
        if(!$(this).hasClass('disabled')) {
            $(this).addClass('disabled');
            $.ajax({
                url: $(this).attr('data-url'),
                type: 'GET',
                dataType: 'json',
                beforeSend: function () {
                    ___HTML___application___hpc___modal___SHOW_LOAD___();
                },
                success: function (data) {
                    if (data['___BOOLEAN___ERROR___']) {
                        ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                    }
                    else {
                        $hpc__modal.html(data['___HTML___APPLICATION___HPC___MODAL___']);
                        $hpc__modal.find('.modal___message').html(data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___']);
                        ___HTML___application___hpc___modal___EVENTS_ON___();
                    }
                }
            });
        }
    };
    var hpc__explorer__a__download = function(){
        var $button_download = $(this);
        if($button_download.attr('disabled')==='disabled')
            return;
        $button_download.button('loading');
        var events = [];
        $hpc__tbody.find('tr.primary').each(function () {
            events.push(
                $.ajax({
                    url: $button_download.attr('data-url'),
                    method: 'GET',
                    data: {
                        path: path,
                        name: $(this).attr('data-name'),
                        type: $(this).attr('data-type')
                    },
                    xhrFields: {
                        responseType: 'blob'
                    },
                    success: function (data, status, jqxhr) {
                        if (status === 'success') {
                            // Try to find out the filename from the content disposition `filename` value
                            var disposition = jqxhr.getResponseHeader('Content-Disposition');
                            var matches = /"([^"]*)"/.exec(disposition);
                            var filename = (matches !== null && matches[1] ? matches[1] : "unnamed");
                            // The actual download
                            var blob = new Blob([data], {type: jqxhr.getResponseHeader('Content-Type')});
                            var link = document.createElement('a');
                            link.href = window.URL.createObjectURL(blob);
                            link.download = filename;
                            document.body.appendChild(link);
                            link.click();
                            document.body.removeChild(link);
                        }
                        else
                            $.ajax({
                                url: url_error,
                                type: 'GET',
                                data: {
                                    'message': interpolate(gettext('HPC___SSH___MESSAGES_DownloadFilesException'), [name])
                                },
                                dataType: 'json',
                                beforeSend: function () {
                                    ___HTML___application___hpc___modal___SHOW_LOAD___();
                                },
                                success: function (data) {
                                    ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                                }
                            });
                    }
                })
            );
        });
        $.when.apply($, events).then(function() {
           $button_download.button('reset');
        });
    };
    var hpc__explorer__a__copy = function(){
        if($(this).attr('disabled')!=='disabled') {
            filesToCopy = [];
            filesToCopy.push(path);
            $.each($hpc__tbody.find('tr.primary'), function (index, elem) {
                filesToCopy.push($(elem).attr('data-name'));
            });
            $hpc__buttons.find('a').eq(6).removeAttr('disabled');
        }
    };
    var hpc__explorer__li__copy = function(){
        if(!$(this).hasClass('disabled')) {
            filesToCopy = [];
            filesToCopy.push(path);
            $.each($hpc__tbody.find('tr.primary'), function (index, elem) {
                filesToCopy.push($(elem).attr('data-name'));
            });
            $hpc__buttons.find('a').eq(6).removeAttr('disabled');
        }
    };
    var hpc__explorer__a__paste = function(){
        if($(this).attr('disabled')!=='disabled') {
            $(this).attr('disabled', 'disabled');
            $.ajaxSetup({
                headers: {"X-CSRFToken": getCookie("csrftoken")}
            });
            $.ajax({
                url: $(this).attr('data-url'),
                data: {
                    'from': filesToCopy.shift(),
                    'filesToCopy': filesToCopy,
                    'to': path
                },
                type: 'post',
                dataType: 'json',
                cache: false,
                beforeSend: function () {
                    $hpc__tbody.html('' +
                        '<tr>' +
                        '<td colspan="3"><span class="fa fa-spinner fa-pulse"></span> Cargando...</td>' +
                        '</tr>'
                    );
                    hpc__explorer__btn__disable();
                },
                success: function (data) {
                    filesToCopy = [];
                    if (data['___BOOLEAN___ERROR___']) {
                        ___HTML___application___hpc___modal___SHOW_LOAD___();
                        ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data, 10000);
                        $(data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___']).find('.alert___message___text').text();
                    }
                    else {
                        $hpc__tbody.html(data.list);
                        breadcumbs(path);
                        hpc__explorer__btn__enable();
                    }
                }
            });
        }
    };
    var hpc__explorer__li__paste = function(){
        if(!$(this).hasClass('disabled')) {
            $(this).addClass('disabled');
            $.ajaxSetup({
                headers: {"X-CSRFToken": getCookie("csrftoken")}
            });
            $.ajax({
                url: $(this).attr('data-url'),
                data: {
                    'from': filesToCopy.shift(),
                    'filesToCopy': filesToCopy,
                    'to': path
                },
                type: 'post',
                dataType: 'json',
                cache: false,
                beforeSend: function () {
                    $hpc__tbody.html('' +
                        '<tr>' +
                        '<td colspan="3"><span class="fa fa-spinner fa-pulse"></span> Cargando...</td>' +
                        '</tr>'
                    );
                    hpc__explorer__btn__disable();
                },
                success: function (data) {
                    filesToCopy = [];
                    if (data['___BOOLEAN___ERROR___']) {
                        ___HTML___application___hpc___modal___SHOW_LOAD___();
                        ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data, 10000);
                        $(data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___']).find('.alert___message___text').text();
                    }
                    else {
                        $hpc__tbody.html(data.list);
                        breadcumbs(path);
                        hpc__explorer__btn__enable();
                    }
                }
            });
        }
    };
    var hpc__explorer__a__selectAll = function(){
        var tr = $hpc__tbody.find('tr');
        tr.each(function(){
            $(this).addClass('primary');
        });
        hpc__explorer__btn__enable();
    };
    var hpc__explorer__a__unSelectAll = function(){
        var tr = $hpc__tbody.find('tr');
        tr.each(function(){
            $(this).removeClass('primary');
        });
        hpc__explorer__btn__enable();
    };
    var hpc__explorer__a__execute = function(){
        if($(this).attr('disabled')!=='disabled') {
            $.ajax({
                url: $(this).attr('data-url'),
                type: 'GET',
                dataType: 'json',
                beforeSend: function () {
                    ___HTML___application___hpc___modal___SHOW_LOAD___();
                },
                success: function (data) {
                    if (data['___BOOLEAN___ERROR___']) {
                        ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                    }
                    else {
                        $hpc__modal.html(data['___HTML___APPLICATION___HPC___MODAL___']);
                        $hpc__modal.find('.modal___message').html(data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___']);
                        ___HTML___application___hpc___modal___EVENTS_ON___();
                    }
                }
            });
        }
    };
    var hpc__explorer__li__execute = function(){
        if(!$(this).hasClass('disabled')) {
            $.ajax({
                url: $(this).attr('data-url'),
                type: 'GET',
                dataType: 'json',
                beforeSend: function () {
                    ___HTML___application___hpc___modal___SHOW_LOAD___();
                },
                success: function (data) {
                    if (data['___BOOLEAN___ERROR___']) {
                        ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                    }
                    else {
                        $hpc__modal.html(data['___HTML___APPLICATION___HPC___MODAL___']);
                        $hpc__modal.find('.modal___message').html(data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___']);
                        ___HTML___application___hpc___modal___EVENTS_ON___();
                    }
                }
            });
        }
    };
    var hpc__explorer__a__delete = function(){
        if($(this).attr('disabled')!=='disabled') {
            $(this).attr('disabled', 'disabled');
            $.ajax({
                url: $(this).attr('data-url'),
                type: 'GET',
                dataType: 'json',
                beforeSend: function () {
                    ___HTML___application___hpc___modal___SHOW_LOAD___();
                },
                success: function (data) {
                    if (data['___BOOLEAN___ERROR___']) {
                        ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                    }
                    else {
                        $hpc__modal.html(data['___HTML___APPLICATION___HPC___MODAL___']);
                        $hpc__modal.find('.modal___message').html(data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___']);
                        ___HTML___application___hpc___modal___EVENTS_ON___();
                    }
                }
            });
        }
    };
    var hpc__explorer__li__delete = function(){
        if(!$(this).hasClass('disabled')) {
            $(this).addClass('disabled');
            $.ajax({
                url: $(this).attr('data-url'),
                type: 'GET',
                dataType: 'json',
                beforeSend: function () {
                    ___HTML___application___hpc___modal___SHOW_LOAD___();
                },
                success: function (data) {
                    if (data['___BOOLEAN___ERROR___']) {
                        ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                    }
                    else {
                        $hpc__modal.html(data['___HTML___APPLICATION___HPC___MODAL___']);
                        $hpc__modal.find('.modal___message').html(data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___']);
                        ___HTML___application___hpc___modal___EVENTS_ON___();
                    }
                }
            });
        }
    };
    var hpc__explorer__a__generic = function(){
        if($(this).attr('disabled'))
            return;
        var option = $(this).attr('data-option');
        $.ajax({
            url: $(this).attr('data-url'),
            type: 'GET',
            dataType: 'json',
            beforeSend: function () {
                ___HTML___application___hpc___modal___SHOW_LOAD___();
            },
            success: function (data) {
                if (data['___BOOLEAN___ERROR___']) {
                    ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                }
                else {
                    $hpc__modal.html(data['___HTML___APPLICATION___HPC___MODAL___']);
                    $hpc__modal.find('.modal___message').html(data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___']);
                    ___HTML___application___hpc___modal___EVENTS_ON___();
                }
            }
        });
    };
    var hpc__explorer__li__file = function(){
        if(!$(this).hasClass('disabled')) {
            $(this).addClass('disabled');
            var option = $(this).attr('data-option');
            $.ajax({
                url: $(this).attr('data-url'),
                type: 'GET',
                dataType: 'json',
                beforeSend: function () {
                    ___HTML___application___hpc___modal___SHOW_LOAD___();
                },
                success: function (data) {
                    if (data['___BOOLEAN___ERROR___']) {
                        ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                    }
                    else {
                        $hpc__modal.html(data['___HTML___APPLICATION___HPC___MODAL___']);
                        $hpc__modal.find('.modal___message').html(data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___']);
                        ___HTML___application___hpc___modal___EVENTS_ON___();
                    }
                }
            });
        }
    };
    $hpc__buttons
        .on('click', 'a[data-option="back"]', hpc__explorer__a__back)
        .on('click', 'a[data-option="open"]', hpc__explorer__a__open)
        .on('click', 'a[data-option="edit"]', hpc__explorer__a__edit)
        .on('click', 'li[data-option="edit"]', hpc__explorer__li__edit)
        .on('click', 'a[data-option="rename"]', hpc__explorer__a__rename)
        .on('click', 'li[data-option="rename"]', hpc__explorer__li__rename)
        .on('click', 'a[data-option="download"]', hpc__explorer__a__download)
        .on('click', 'a[data-option="download-small"]', hpc__explorer__a__download)
        .on('click', 'a[data-option="copy"]', hpc__explorer__a__copy)
        .on('click', 'li[data-option="copy"]', hpc__explorer__li__copy)
        .on('click', 'a[data-option="paste"]', hpc__explorer__a__paste)
        .on('click', 'li[data-option="paste"]', hpc__explorer__li__paste)
        .on('click', 'a[data-option="select-all"]', hpc__explorer__a__selectAll)
        .on('click', 'a[data-option="unselect-all"]', hpc__explorer__a__unSelectAll)
        .on('click', 'a[data-option="execute"]', hpc__explorer__a__execute)
        .on('click', 'li[data-option="execute"]', hpc__explorer__li__execute)
        .on('click', 'a[data-option="delete"]', hpc__explorer__a__delete)
        .on('click', 'li[data-option="delete"]', hpc__explorer__li__delete)
        .on('click', 'a[data-option="goto"]', hpc__explorer__a__generic)
        .on('click', 'a[data-option="folder"]', hpc__explorer__a__generic)
        .on('click', 'a[data-option="file"]', hpc__explorer__a__generic)
        .on('click', 'li[data-option="file"]', hpc__explorer__li__file)
        .on('click', 'a[data-option="upload"]', hpc__explorer__a__generic);
    /*>>>>>>>>*/


    /*<<<<<<<<*/
    var hpc__explorer__modal__click__go_to = function(){
        var dir = $hpc__modal.find('#modal-goto').find('input[name=goto]').val();
        path = '/' + path.split('/')[1] + '/' + path.split('/')[2] + '/' + path.split('/')[3];
        if (dir)
            path += '/' + $hpc__modal.find('#modal-goto').find('input[name=goto]').val();
        $.ajax({
            url: url_list,
            data: {
                'path': path
            },
            type: 'GET',
            dataType: 'json',
            cache: false,
            beforeSend: function () {
                $hpc__tbody.html('' +
                    '<tr>' +
                        '<td colspan="3"><span class="fa fa-spinner fa-pulse"></span> Cargando...</td>' +
                    '</tr>'
                );
                hpc__explorer__btn__disable();
                ___HTML___application___hpc___modal___SHOW_LOAD___();
                $('.application___hpc___load').css('height', '20px');
            },
            success: function (data) {
                if(data['___BOOLEAN___ERROR___'])
                    ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data, 10000);
                else
                    ___HTML___application___hpc___modal___ACTION_CLOSE___();
                if(data.list) {
                    $hpc__tbody.html(data.list);
                    breadcumbs(path);
                    hpc__explorer__btn__enable();
                }
            }
        });
    };
    var hpc__explorer__modal__submit__create_folder = function(evt){
        evt.preventDefault();
        var $form = $(this);
        var $btn =$form.find('.modal-footer').find('button').eq(0);
        if($btn.attr('disabled'))
            return;
        var formData = new FormData(this);
        formData.append('path', path);
        $.ajax({
            url: $form.attr('action'),
            data: formData,
            type: $form.attr('method'),
            dataType: 'json',
            cache: false,
            processData: false,
            contentType: false,
            beforeSend: function () {
                $hpc__tbody.html('' +
                    '<tr>' +
                        '<td colspan="3"><span class="fa fa-spinner fa-pulse"></span> Cargando...</td>' +
                    '</tr>'
                );
                hpc__explorer__btn__disable();
                ___HTML___application___hpc___modal___SHOW_LOAD___();
                $('.application___hpc___load').css('height', '20px');
            },
            success: function (data) {
                if(data['___BOOLEAN___ERROR___'])
                    ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data, 10000);
                else
                    ___HTML___application___hpc___modal___ACTION_CLOSE___();
                if (data.list) {
                    $hpc__tbody.html(data.list);
                    breadcumbs(path);
                    hpc__explorer__btn__enable();
                }
            }
        });
    };
    var hpc__explorer__modal__submit__create_file = function(evt){
        evt.preventDefault();
        var $form = $(this);
        var $btn =$form.find('.modal-footer').find('button').eq(0);
        if($btn.attr('disabled'))
            return;
        var formData = new FormData(this);
        formData.append('path', path);
        $.ajax({
            url: $form.attr('action'),
            data: formData,
            type: $form.attr('method'),
            dataType: 'json',
            cache: false,
            processData: false,
            contentType: false,
            beforeSend: function () {
                $hpc__tbody.html('' +
                    '<tr>' +
                        '<td colspan="3"><span class="fa fa-spinner fa-pulse"></span> Cargando...</td>' +
                    '</tr>'
                );
                hpc__explorer__btn__disable();
                ___HTML___application___hpc___modal___SHOW_LOAD___();
                $('.application___hpc___load').css('height', '20px');
            },
            success: function (data) {
                if(data['___BOOLEAN___ERROR___'])
                    ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data, 10000);
                else
                    ___HTML___application___hpc___modal___ACTION_CLOSE___();
                if (data.list) {
                    $hpc__tbody.html(data.list);
                    breadcumbs(path);
                    hpc__explorer__btn__enable();
                }
            }
        });
    };
    var hpc__explorer__modal__submit__upload = function(evt){
        evt.preventDefault();
        var $form = $(this);
        var $btn =$form.find('.modal-footer').find('button').eq(0);
        if($btn.attr('disabled'))
            return;
        var formData = new FormData(this);
        formData.append('path', path);
        $.ajax({
            url: $form.attr('action') + '?upload=',
            data: formData,
            type: $form.attr('method'),
            dataType: 'json',
            cache: false,
            processData: false,
            contentType: false,
            beforeSend: function () {
                $hpc__tbody.html('' +
                    '<tr>' +
                        '<td colspan="3"><span class="fa fa-spinner fa-pulse"></span> Cargando...</td>' +
                    '</tr>'
                );
                hpc__explorer__btn__disable();
                ___HTML___application___hpc___modal___SHOW_LOAD___();
                $('.application___hpc___load').css('height', '20px');
            },
            success: function (data) {
                if(data['___BOOLEAN___ERROR___'])
                    ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data, 10000);
                else
                    ___HTML___application___hpc___modal___ACTION_CLOSE___();
                if (data.list) {
                    $hpc__tbody.html(data.list);
                    breadcumbs(path);
                    hpc__explorer__btn__enable();
                }
            }
        });
    };
    var hpc__explorer__modal__submit__edit = function(evt){
        evt.preventDefault();
        var $form = $(this);
        var $btn =$form.find('.modal-footer').find('button').eq(0);
        if($btn.attr('disabled'))
            return;
        var formData = new FormData(this);
        formData.append('path', path);
        formData.append('file_name', $hpc__tbody.find('tr.primary').attr('data-name'));
        $.ajax({
            url: $form.attr('action') + '?save=',
            data: formData,
            type: $form.attr('method'),
            dataType: 'json',
            cache: false,
            processData: false,
            contentType: false,
            beforeSend: function () {
                $form.find('.modal-header').append('' +
                    '<div style="position: absolute; top: 16px; right: 60px">' +
                    '   <span class="fa fa-spinner fa-pulse"></span> ' + gettext('HPC___SSH___FILE_EDITOR___Saving') +
                    '</div>'
                );
            },
            success: function (data) {
                var $div = $form.find('.modal-header').find('div');
                if (data['___BOOLEAN___ERROR___']) {
                    $div.html('<span class="fa fa-warning fa-fw"></span> ' + gettext('HPC___SSH___FILE_EDITOR___SaveError'));
                }
                else {
                    $btn.attr('disabled', 'disabled');
                    $div.html('<span class="fa fa-check-circle fa-fw"></span> ' + gettext('HPC___SSH___FILE_EDITOR___Saved'));
                }
                setTimeout(function(){
                    $div.remove();
                }, 4000);
            }
        });
    };
    var hpc__explorer__modal__submit__rename = function(evt){
        evt.preventDefault();
        var $form = $(this);
        var $btn =$form.find('.modal-footer').find('button').eq(0);
        if($btn.attr('disabled'))
            return;
        var formData = new FormData(this);
        formData.append('path', path);
        formData.append('name', $hpc__tbody.find('tr.primary').attr('data-name'));
        $.ajax({
            url: $form.attr('action') + '?' + $form.attr('data-option') + '=',
            data: formData,
            type: $form.attr('method'),
            dataType: 'json',
            cache: false,
            processData: false,
            contentType: false,
            beforeSend: function () {
                $hpc__tbody.html('' +
                    '<tr>' +
                        '<td colspan="3"><span class="fa fa-spinner fa-pulse"></span> Cargando...</td>' +
                    '</tr>'
                );
                hpc__explorer__btn__disable();
                ___HTML___application___hpc___modal___SHOW_LOAD___();
                $('.application___hpc___load').css('height', '20px');
            },
            success: function (data) {
                if(data['___BOOLEAN___ERROR___'])
                    ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data, 10000);
                else
                    ___HTML___application___hpc___modal___ACTION_CLOSE___();
                if (data.list) {
                    $hpc__tbody.html(data.list);
                    breadcumbs(path);
                    hpc__explorer__btn__enable();
                }
            }
        });
    };
    var hpc__explorer__modal__click__execute = function () {
        var url = $('#modal-execute').find('.modal-footer').find('button').eq(0).attr('data-url');
        var values = [path, $hpc__tbody.find('tr.primary').attr('data-name')];
        $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie("csrftoken") }
        });
        $.ajax({
            url: url,
            data: {
                'values': values
            },
            type: 'post',
            dataType: 'json',
            cache: false,
            beforeSend: function () {
                hpc__explorer__btn__disable();
                ___HTML___application___hpc___modal___SHOW_LOAD___();
                $('.application___hpc___load').css('height', '20px')
            },
            success: function (data) {
                if(data['___BOOLEAN___ERROR___'])
                    ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data, 10000);
                else
                    ___HTML___application___hpc___modal___SHOW_MESSAGE_OK___(data);
                hpc__explorer__btn__enable();
            }
        });
    };
    var hpc__explorer__modal__click__delete = function() {
        var $btn = $('#modal-delete').find('.modal-footer').find('button').eq(0);
        var values = [path];
        $.each($hpc__tbody.find('tr.primary'), function(index, elem){
            values.push($(elem).attr('data-name'));
        });
        $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie("csrftoken") }
        });
        $.ajax({
            url: $btn.attr('data-url'),
            data: {
                'values': values
            },
            type: 'post',
            dataType: 'json',
            cache: false,
            beforeSend: function () {
                $hpc__tbody.html('' +
                    '<tr>' +
                        '<td colspan="3"><span class="fa fa-spinner fa-pulse"></span> Cargando...</td>' +
                    '</tr>'
                );
                hpc__explorer__btn__disable();
                ___HTML___application___hpc___modal___SHOW_LOAD___();
                $('.application___hpc___load').css('height', '20px')
            },
            success: function (data) {
                if(data['___BOOLEAN___ERROR___'])
                    ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data, 10000);
                else
                    ___HTML___application___hpc___modal___ACTION_CLOSE___();
                if (data.list) {
                    $hpc__tbody.html(data.list);
                    breadcumbs(path);
                    hpc__explorer__btn__enable();
                }
            }
        });
    };
    $hpc__modal
        .on('click', '.hpc___modal___click___go_to', hpc__explorer__modal__click__go_to)
        .on('submit', '.hpc___modal___submit___create_folder', hpc__explorer__modal__submit__create_folder)
        .on('submit', '.hpc___modal___submit___create_file', hpc__explorer__modal__submit__create_file)
        .on('submit', '.hpc___modal___submit___upload', hpc__explorer__modal__submit__upload)
        .on('submit', '.hpc___modal___submit___edit', hpc__explorer__modal__submit__edit)
        .on('submit', '.hpc___modal___submit___rename', hpc__explorer__modal__submit__rename)
        .on('click', '.hpc___modal___click___execute', hpc__explorer__modal__click__execute)
        .on('click', '.hpc___modal___click___delete', hpc__explorer__modal__click__delete);
    /*>>>>>>>>*/


    /*<<<<<<<<*/
    var hpc__explorer__modal__upload__validation = function() {
        var $hpc__modal__body = $hpc__modal.find('.modal-body'),
            $hpc__modal__footer = $hpc__modal.find('.modal-footer');
        var files = $hpc__modal__body.find('#files').get(0).files,
            $input = $hpc__modal__body.find('#files_selected');
        if (files.length > 1) $input.val(files.length + ' archivos seleccionados');
        if (files.length === 1) $input.val('Un archivo seleccionado: '+files[0].name);
        if (files.length === 0) $input.val('');
        var i = 0,
            error = false;
        if (files.length > 0 && files.length < 11){
            for(i; i<files.length; i++) {
                if (files[i].size > 1024 * 1024 * 150) {
                    error = true;
                    $hpc__modal__body.find('.help-block').html('<span class="fa fa-exclamation-circle fa-fw"></span> ' + gettext('HPC___EXPLORER___MODAL___UPLOAD___VALIDATION___Size'));
                    break;
                }
                for (var j = 0; j < files[i].name.length; j++) {
                    if (files[i].name[j] === '\\'){
                        error = true;
                        $hpc__modal__body.find('.help-block').html('<span class="fa fa-exclamation-circle fa-fw"></span> ' + gettext('HPC___EXPLORER___MODAL___UPLOAD___VALIDATION___Char'));
                        break;
                    }
                }
                if (j !== files[i].name.length)
                    break;
            }
            if(i === files.length){
                error = false;
                $hpc__modal__body.find('.help-block').html('');
            }
        }
        else{
            error = true;
            $hpc__modal__footer.find('button.btn-primary').attr('disabled', 'disabled');
            if(files.length === 0)
                $hpc__modal__body.find('.help-block').html('<span class="fa fa-exclamation-circle fa-fw"></span> ' + gettext('HPC___EXPLORER___MODAL___UPLOAD___VALIDATION___Min'));
            else
                $hpc__modal__body.find('.help-block').html('<span class="fa fa-exclamation-circle fa-fw"></span> ' + gettext('HPC___EXPLORER___MODAL___UPLOAD___VALIDATION___Max'));
        }
        var elem = $hpc__modal__body.find('.btn');
        var formGroup = $hpc__modal__body.find('.form-group');
        if (error) {
            $hpc__modal__footer.find('button').eq(0).attr('disabled', 'disabled');
            if (elem.hasClass('btn-default')) elem.removeClass('btn-default').addClass('btn-danger');
            if (!formGroup.hasClass('has-error')) formGroup.addClass('has-error')
        }
        else {
            $hpc__modal__footer.find('button').eq(0).removeAttr('disabled');
            if (elem.hasClass('btn-danger')) elem.removeClass('btn-danger').addClass('btn-default');
            if (formGroup.hasClass('has-error')) formGroup.removeClass('has-error')
        }
    };
    var eblur = function(){
        $(this).siblings().eq(0).removeClass('border-shadow');
    };
    var efocus = function(){
        $(this).siblings().eq(0).addClass('border-shadow');
    };
    var ekeyup = function(){
        var $btn = $hpc__modal.find('.modal-footer').find('button').eq(0);
        // var expreg = new RegExp('.*(/|\\\\).*');
        var expreg = new RegExp('.*/.*');
        if($(this).val().length>0){
            if(expreg.test($(this).val()))
                $btn.attr('disabled', 'disabled');
            else
                $btn.removeAttr('disabled');
        }else
            if(!$btn.attr('disabled'))
                $btn.attr('disabled', 'disabled');
    };
    $hpc__modal
        .on('blur', '#modal-goto input[name=goto]', eblur)
        .on('focus', '#modal-goto input[name=goto]', efocus)
        .on('change', '#files', hpc__explorer__modal__upload__validation)
        .on('keyup', '#modal-file #id_generic', ekeyup)
        .on('keyup', '#modal-folder #id_generic', ekeyup)
        .on('keyup', '#modal-rename #id_generic', ekeyup);
    /*>>>>>>>>*/
};