!function (a, b, c) {
    function d(b, c) {
        this.element = a(b), this.settings = a.extend({}, f, c), this._defaults = f, this._name = e, this.init()
    }

    var e = "application___help___leftside___nav", f = {toggle: !1, doubleTapToGo: !1};
    d.prototype = {
        init: function () {
            var b = this.element, d = this.settings.toggle, f = this;
            this.isIE() <= 9 ? (b.find("li.active").has("ul").children("ul").collapse("show"), b.find("li").not(".active").has("ul").children("ul").collapse("hide")) : (b.find("li.active").has("ul").children("ul").addClass("collapse in"), b.find("li").not(".active").has("ul").children("ul").addClass("collapse")), f.settings.doubleTapToGo && b.find("li.active").has("ul").children("a").addClass("doubleTapToGo"), b.find("li").has("ul").children("a").on("click." + e, function (b) {
                return b.preventDefault(), f.settings.doubleTapToGo && f.doubleTapToGo(a(this)) && "#" !== a(this).attr("href") && "" !== a(this).attr("href") ? (b.stopPropagation(), void(c.location = a(this).attr("href"))) : (a(this).parent("li").toggleClass("active").children("ul").collapse("toggle"), void(d && a(this).parent("li").siblings().removeClass("active").children("ul.in").collapse("hide")))
            })
        }, isIE: function () {
            for (var a, b = 3, d = c.createElement("div"), e = d.getElementsByTagName("i"); d.innerHTML = "<!--[if gt IE " + ++b + "]><i></i><![endif]-->", e[0];)return b > 4 ? b : a
        }, doubleTapToGo: function (a) {
            var b = this.element;
            return a.hasClass("doubleTapToGo") ? (a.removeClass("doubleTapToGo"), !0) : a.parent().children("ul").length ? (b.find(".doubleTapToGo").removeClass("doubleTapToGo"), a.addClass("doubleTapToGo"), !1) : void 0
        }, remove: function () {
            this.element.off("." + e), this.element.removeData(e)
        }
    }, a.fn[e] = function (b) {
        return this.each(function () {
            var c = a(this);
            c.data(e) && c.data(e).remove(), c.data(e, new d(this, b))
        }), this
    }
}(jQuery, window, document);
/* */
var ___HTML___application___RELOAD___ = function () {
    var $link = $(this);
    window.location = $link.attr("data-url");
};
/* */
var ___HTML___load___RELOAD___ = function () {
    var identifier = "#application___help___load";
    $.ajax({
        url: $(identifier).attr("data-url"),
        type: "get",
        dataType: "json",
        beforeSend: function () {
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___modal___SHOW_LOAD___();
                ___HTML___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                $(identifier).html(data.___HTML___LOAD___);
            }
        }
    });
};
/* */
var ___HTML___title___RELOAD___ = function () {
    var identifier = "title";
    $.ajax({
        url: $(identifier).attr("data-url"),
        type: "get",
        dataType: "json",
        beforeSend: function () {
            document.title = ___TEXT___LOAD___;
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___modal___SHOW_LOAD___();
                ___HTML___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                document.title = data.___HTML___TITLE___;
            }
        }
    });
};
/* */
var ___HTML___header___RELOAD___ = function () {
    var identifier = "#application___help___header";
    $.ajax({
        url: $(identifier).attr("data-url"),
        type: "get",
        dataType: "json",
        beforeSend: function () {
            $(identifier).html(___HTML___LOAD___);
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___modal___SHOW_LOAD___();
                ___HTML___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                $(identifier).html(data.___HTML___HEADER___);
                /* remove event */
                $(identifier).off("click", ".LINK___application___reload");
                $(identifier).off("click", ".LINK___modal___reload");
                $(identifier).off("click", ".LINK___modal___action_locale");
                /* add event */
                $(identifier).on("click", ".LINK___application___reload", ___HTML___application___RELOAD___);
                $(identifier).on("click", ".LINK___modal___reload", ___HTML___modal___RELOAD___);
                $(identifier).on("click", ".LINK___modal___action_locale", ___HTML___modal___ACTION_LOCALE___);
            }
        }
    });
};
/* */
var ___HTML___leftside___RELOAD___ = function () {
    var identifier_2 = "#application___help___content___center";
    $.ajax({
        url: $(identifier_2).attr("data-url"),
        type: "get",
        dataType: "json",
        beforeSend: function () {
            $(identifier_2).html(___HTML___LOAD___);
        },
        success: function (data) {
            $(identifier_2).html(data.___HTML___CONTENT___CENTER___);
        }
    });
};
/* */
var ___HTML___content___center___RELOAD___ = function (event) {
    var $link = $(this);
    $.ajax({
        url: $link.attr("data-url"),
        type: "get",
        dataType: "json",
        beforeSend: function () {
            $(".LINK___content___center___reload").removeClass("active");
            $link.addClass("active");
            $("#application___help___leftside.collapse").removeClass("in");
            $("#application___help___content___center").html(___HTML___LOAD___);
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___modal___SHOW_LOAD___();
                ___HTML___modal___SHOW_MESSAGE_ERROR___(data);
                $("#application___help___content___center").html("");
            }
            else {
                $("#application___help___content___center").html(data.___HTML___CONTENT___CENTER___);
            }
        }
    });
};
/* */
var ___HTML___content___footer___RELOAD___ = function () {
    var identifier = "#application___help___content___footer";
    $.ajax({
        url: $(identifier).attr("data-url"),
        type: "get",
        dataType: "json",
        beforeSend: function () {
            $(identifier).html(___HTML___LOAD___);
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___modal___SHOW_LOAD___();
                ___HTML___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                $(identifier).html(data.___HTML___CONTENT___FOOTER___);
            }
        }
    });
};
/* */
var ___HTML___modal___RELOAD___ = function () {
    var $link = $(this);
    $.ajax({
        url: $link.attr("data-url"),
        type: "get",
        dataType: "json",
        beforeSend: function () {
            ___HTML___modal___SHOW_LOAD___();
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                var $site___modal = $("#site___modal");
                $site___modal.html(data.___HTML___MODAL___);
                $site___modal.find(".modal___message").html(data.___HTML___MODAL___MESSAGE___);
                /* */
                ___HTML___modal___EVENTS_ON___();
            }
        }
    });
};
var ___HTML___modal___ACTION_REFRESH___ = function () {
    var $link = $(this);
    $.ajax({
        url: $link.attr("data-url"),
        type: "get",
        dataType: "json",
        beforeSend: function () {
            ___HTML___modal___modal_content___modal_body___SHOW_LOAD___();
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                var $site___modal = $("#site___modal");
                $site___modal.html(data.___HTML___MODAL___);
                $site___modal.find(".modal___message").html(data.___HTML___MODAL___MESSAGE___);
            }
        }
    });
};
var ___HTML___modal___ACTION_REFRESH___SECURITY___LOGIN___ = function () {
    var $link = $(this);
    $.ajax({
        url: $link.attr("data-url"),
        type: "get",
        dataType: "json",
        beforeSend: function () {
            ___HTML___modal___modal_content___modal_body___SHOW_LOAD___SECURITY___LOGIN___();
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                $("#site___modal").html(data.___HTML___MODAL___);
            }
        }
    });
};
var ___HTML___modal___ACTION_CLOSE___ = function () {
    $("#site___modal").modal("hide").html("");
    /* */
};
var ___HTML___modal___ACTION_LOGIN___ = function () {
    var $form = $(this);
    $.ajax({
        url: $form.attr("action"),
        data: $form.serialize(),
        type: $form.attr("method"),
        dataType: "json",
        beforeSend: function () {
            ___HTML___modal___modal_content___modal_body___SHOW_LOAD___SECURITY___LOGIN___();
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                var $site___modal = $("#site___modal");
                if (data.___BOOLEAN___IS_METHOD_POST___) {
                    if (data.___INT___IS_VALID_FORM___ == 1) {
                        ___HTML___load___RELOAD___();
                        ___HTML___title___RELOAD___();
                        ___HTML___header___RELOAD___();
                        ___HTML___leftside___RELOAD___();
                        ___HTML___content___footer___RELOAD___();
                        /* */
                        ___HTML___modal___SHOW_MESSAGE_OK___(data);
                    }
                    else {
                        $site___modal.html(data.___HTML___MODAL___);
                        $site___modal.find(".tab-pane.active").find(".modal___message").html(data.___HTML___MODAL___MESSAGE___);
                    }
                }
                else {
                    $site___modal.html(data.___HTML___MODAL___);
                }
            }
        }
    });
    return false;
};
var ___HTML___modal___ACTION_LOGOUT___ = function () {
    var $form = $(this);
    $.ajax({
        url: $form.attr("action"),
        data: $form.serialize(),
        type: $form.attr("method"),
        dataType: "json",
        beforeSend: function () {
            ___HTML___modal___modal_content___modal_body___SHOW_LOAD___();
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                if (data.___BOOLEAN___IS_METHOD_POST___) {
                    ___HTML___modal___SHOW_MESSAGE_OK___(data);
                }
                else {
                    $("#site___modal").html(data.___HTML___MODAL___);
                }
            }
        }
    });
    return false;
};
var ___HTML___modal___ACTION_PROFILE___ = function () {
    var $form = $(this);
    $.ajax({
        url: $form.attr("action"),
        data: new FormData(this),
        type: $form.attr("method"),
        dataType: "json",
        cache: false,
        processData: false,
        contentType: false,
        beforeSend: function () {
            ___HTML___modal___modal_content___modal_body___SHOW_LOAD___();
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                var $site___modal = $("#site___modal");
                if (data.___BOOLEAN___IS_METHOD_POST___) {
                    if (data.___BOOLEAN___IS_VALID_FORM___) {
                        ___HTML___header___RELOAD___();
                        ___HTML___leftside___RELOAD___();
                        /* */
                        $site___modal.html(data.___HTML___MODAL___);
                        $site___modal.find(".modal___message").html(data.___HTML___MODAL___MESSAGE___);
                    }
                    else {
                        $site___modal.html(data.___HTML___MODAL___);
                        $site___modal.find(".modal___message").html(data.___HTML___MODAL___MESSAGE___);
                    }
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
var ___HTML___modal___ACTION_LOCALE___ = function () {
    var $link = $(this);
    $.ajax({
        url: $link.attr("data-url"),
        type: "get",
        dataType: "json",
        beforeSend: function () {
            ___HTML___modal___SHOW_LOAD___();
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                /* */
                ___HTML___load___RELOAD___();
                ___HTML___title___RELOAD___();
                ___HTML___header___RELOAD___();
                ___HTML___leftside___RELOAD___();
                ___HTML___content___footer___RELOAD___();
                /* */
                ___HTML___modal___SHOW_MESSAGE_OK___(data);
            }
        }
    });
};
/* */
var ___HTML___modal___SHOW_LOAD___ = function () {
    $("#application___help___leftside.collapse").removeClass("in");
    var $site___modal = $("#site___modal");
    if ($site___modal.hasClass("in")) {
        ___HTML___modal___modal_content___SHOW_LOAD___();
    }
    else {
        $site___modal.html("<div class='modal-dialog modal-sm'><div class='modal-content'>" + ___HTML___LOAD___ + "</div></div>");
    }
    $site___modal.modal("show");
};
var ___HTML___modal___modal_content___SHOW_LOAD___ = function () {
    var $identifier = $("#site___modal").find(".modal-content");
    var int___height___modal_content = $identifier.height();
    $identifier.html(___HTML___LOAD___);
    var int___height___application___help___load = $identifier.find(".application___help___load").height();
    int___height___application___help___load = (int___height___modal_content > int___height___application___help___load) ? int___height___modal_content : int___height___application___help___load;
    $identifier.find(".application___help___load").height(int___height___application___help___load);
};
var ___HTML___modal___modal_content___modal_body___SHOW_LOAD___ = function () {
    var $identifier = $("#site___modal").find(".modal-content").find(".modal-body");
    var int___height___modal_body = $identifier.height();
    $identifier.html(___HTML___LOAD___);
    var int___height___application___help___load = $identifier.find(".application___help___load").height();
    int___height___application___help___load = (int___height___modal_body > int___height___application___help___load) ? int___height___modal_body : int___height___application___help___load;
    $identifier.find(".application___help___load").height(int___height___application___help___load);
};
var ___HTML___modal___modal_content___modal_body___SHOW_LOAD___SECURITY___LOGIN___ = function () {
    var $identifier = $("#site___modal").find(".modal-content").find(".tab-pane.active").find(".modal-body");
    var int___height___tab_pane_active___modal_body = $identifier.height();
    $identifier.html(___HTML___LOAD___);
    var int___height___application___help___load = $identifier.find(".application___help___load").height();
    int___height___application___help___load = (int___height___tab_pane_active___modal_body > int___height___application___help___load) ? int___height___tab_pane_active___modal_body : int___height___application___help___load;
    $identifier.find(".application___help___load").height(int___height___application___help___load);
};
var ___HTML___modal___EVENTS_OFF___ = function () {
    $("#site___modal")
        .off("click", ".LINK___modal___action_refresh")
        .off("click", ".LINK___modal___action_refresh___security___login")
        .off("click", ".LINK___modal___action_close")
        .off("submit", ".LINK___modal___action_login")
        .off("submit", ".LINK___modal___action_logout")
        .off("submit", ".LINK___modal___action_profile")
        .off("click", ".LINK___modal___modal___reload");
};
var ___HTML___modal___EVENTS_ON___ = function () {
    ___HTML___modal___EVENTS_OFF___();
    $("#site___modal")
        .on("click", ".LINK___modal___action_refresh", ___HTML___modal___ACTION_REFRESH___)
        .on("click", ".LINK___modal___action_refresh___security___login", ___HTML___modal___ACTION_REFRESH___SECURITY___LOGIN___)
        .on("click", ".LINK___modal___action_close", ___HTML___modal___ACTION_CLOSE___)
        .on("submit", ".LINK___modal___action_login", ___HTML___modal___ACTION_LOGIN___)
        .on("submit", ".LINK___modal___action_logout", ___HTML___modal___ACTION_LOGOUT___)
        .on("submit", ".LINK___modal___action_profile", ___HTML___modal___ACTION_PROFILE___)
        .on("click", ".LINK___modal___modal___reload", ___HTML___modal___modal___RELOAD___);
};
var ___HTML___modal___SHOW_MESSAGE_ERROR___ = function (data) {
    var $site___modal = $("#site___modal");
    $site___modal.html(data.___HTML___MODAL___);
    $site___modal.find(".modal___message").html(data.___HTML___MODAL___MESSAGE___);
    /* */
    var int___message_state = 0;

    function ___JS___modal___message___close1___() {
        if ($site___modal.find(".modal___message").find(".alert").find("button.close").length <= 1) {
            ___JS___modal___message___close___();
        }
    }

    function ___JS___modal___message___close2___() {
        if (int___message_state == 0) {
            ___JS___modal___message___close___();
        }
    }

    function ___JS___modal___message___close___() {
        $site___modal.find(".modal___message").off("click", ".alert button.close");
        $site___modal.modal("hide").html("");
        int___message_state = 1;
        if (typeof(data.___APPLICATION___SECURITY___USER___WITHOUT_PERMISSION___) != "undefined" && data.___APPLICATION___SECURITY___USER___WITHOUT_PERMISSION___ == true) {
            window.location.replace(data.___APPLICATION___SECURITY___USER___URL_REDIRECT___);
        }
    }

    $site___modal.find(".modal___message")
        .off("click", ".alert button.close")
        .on("click", ".alert button.close", ___JS___modal___message___close1___);
    function ___JS___modal___message___alert___close___() {
        if (int___message_state == 0) {
            $site___modal.find(".modal___message").fadeOut("slow", function () {
                ___JS___modal___message___close2___();
            });
        }
    }

    setTimeout(___JS___modal___message___alert___close___, 3000);
};
var ___HTML___modal___SHOW_MESSAGE_OK___ = function (data) {
    var $site___modal = $("#site___modal");
    $site___modal.html(data.___HTML___MODAL___);
    $site___modal.find(".modal___message").html(data.___HTML___MODAL___MESSAGE___);
    /* */
    var int___message_state = 0;

    function ___JS___modal___message___close1___() {
        if ($site___modal.find(".modal___message").find(".alert").find("button.close").length <= 1) {
            ___JS___modal___message___close___();
        }
    }

    function ___JS___modal___message___close2___() {
        if (int___message_state == 0) {
            ___JS___modal___message___close___();
        }
    }

    function ___JS___modal___message___close___() {
        $site___modal.find(".modal___message").off("click", ".alert button.close");
        $site___modal.modal("hide").html("");
        int___message_state = 1;
        if (typeof(data.___APPLICATION___SECURITY___USER___WITHOUT_PERMISSION___) != "undefined" && data.___APPLICATION___SECURITY___USER___WITHOUT_PERMISSION___ == true) {
            window.location.replace(data.___APPLICATION___SECURITY___USER___URL_REDIRECT___);
        }
    }

    $site___modal.find(".modal___message")
        .off("click", ".alert button.close")
        .on("click", ".alert button.close", ___JS___modal___message___close1___);
    function ___JS___modal___message___alert___close___() {
        if (int___message_state == 0) {
            $site___modal.find(".modal___message").fadeOut("slow", function () {
                ___JS___modal___message___close2___();
            });
        }
    }

    setTimeout(___JS___modal___message___alert___close___, 3000);
};
/* */
var ___HTML___modal___modal___RELOAD___ = function () {
    var $link = $(this);
    $.ajax({
        url: $link.attr("data-url"),
        type: "get",
        dataType: "json",
        beforeSend: function () {
            $("#site___modal").addClass("application___help___invisible");
            ___HTML___modal___modal___SHOW_LOAD___();
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___modal___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                $("#site___modal___modal").html(data.___HTML___MODAL___MODAL___);
                /* */
                ___HTML___modal___modal___EVENTS_ON___();
            }
        }
    });
};
var ___HTML___modal___modal___ACTION_REFRESH___ = function () {
    var $link = $(this);
    $.ajax({
        url: $link.attr("data-url"),
        type: "get",
        dataType: "json",
        beforeSend: function () {
            ___HTML___modal___modal___modal_content___modal_body___SHOW_LOAD___();
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___modal___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                var $site___modal___modal = $("#site___modal___modal");
                $site___modal___modal.html(data.___HTML___MODAL___MODAL___);
                $site___modal___modal.find(".modal___message").html(data.___HTML___MODAL___MODAL___MESSAGE___);
            }
        }
    });
};
var ___HTML___modal___modal___ACTION_CLOSE___ = function () {
    $("#site___modal___modal").modal("hide").html("");
    $("#site___modal").removeClass("application___help___invisible");
};
var ___HTML___modal___modal___ACTION_SUBMIT_AND_KEEP_THE_MODAL_OPEN___ = function () {
    var $form = $(this);
    $.ajax({
        url: $form.attr("action"),
        data: $form.serialize(),
        type: $form.attr("method"),
        dataType: "json",
        beforeSend: function () {
            ___HTML___modal___modal___modal_content___modal_body___SHOW_LOAD___();
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___modal___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                var $site___modal___modal = $("#site___modal___modal");
                if (data.___BOOLEAN___IS_METHOD_POST___) {
                    if (data.___BOOLEAN___IS_VALID_FORM___) {
                        $site___modal___modal.html(data.___HTML___MODAL___MODAL___);
                        $site___modal___modal.find(".modal___message").html(data.___HTML___MODAL___MODAL___MESSAGE___);
                    }
                    else {
                        $site___modal___modal.html(data.___HTML___MODAL___MODAL___);
                    }
                }
                else {
                    $site___modal___modal.html(data.___HTML___MODAL___MODAL___);
                }
            }
        }
    });
    return false;
};
var ___HTML___modal___modal___ACTION_SUBMIT_AND_CLOSE_THE_MODAL___ = function () {
    var $form = $(this);
    $.ajax({
        url: $form.attr("action"),
        data: $form.serialize(),
        type: $form.attr("method"),
        dataType: "json",
        beforeSend: function () {
            ___HTML___modal___modal___modal_content___modal_body___SHOW_LOAD___();
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___modal___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                var $site___modal___modal = $("#site___modal___modal");
                if (data.___BOOLEAN___IS_METHOD_POST___) {
                    if (data.___BOOLEAN___IS_VALID_FORM___) {
                        ___HTML___modal___modal___SHOW_MESSAGE_OK___(data);
                    }
                    else {
                        $site___modal___modal.html(data.___HTML___MODAL___MODAL___);
                    }
                }
                else {
                    $site___modal___modal.html(data.___HTML___MODAL___MODAL___);
                }
            }
        }
    });
    return false;
};
var ___HTML___modal___modal___SHOW_LOAD___ = function () {
    var $site___modal___modal = $("#site___modal___modal");
    if ($site___modal___modal.hasClass("in")) {
        ___HTML___modal___modal___modal_content___SHOW_LOAD___();
    }
    else {
        $site___modal___modal.html("<div class='modal-dialog modal-sm'><div class='modal-content'>" + ___HTML___LOAD___ + "</div></div>");
    }
    $site___modal___modal.modal("show");
};
var ___HTML___modal___modal___modal_content___SHOW_LOAD___ = function () {
    var $identifier = $("#site___modal___modal").find(".modal-content");
    var int___height___modal_content = $identifier.height();
    $identifier.html(___HTML___LOAD___);
    var int___height___application___help___load = $identifier.find(".application___help___load").height();
    int___height___application___help___load = (int___height___modal_content > int___height___application___help___load) ? int___height___modal_content : int___height___application___help___load;
    $identifier.find(".application___help___load").height(int___height___application___help___load);
};
var ___HTML___modal___modal___modal_content___modal_body___SHOW_LOAD___ = function () {
    var $identifier = $("#site___modal___modal").find(".modal-content").find(".modal-body");
    var int___height___modal_body = $identifier.height();
    $identifier.html(___HTML___LOAD___);
    var int___height___application___help___load = $identifier.find(".application___help___load").height();
    int___height___application___help___load = (int___height___modal_body > int___height___application___help___load) ? int___height___modal_body : int___height___application___help___load;
    $identifier.find(".application___help___load").height(int___height___application___help___load);
};
var ___HTML___modal___modal___EVENTS_OFF___ = function () {
    $("#site___modal___modal")
        .off("click", ".LINK___modal___modal___action_refresh")
        .off("click", ".LINK___modal___modal___action_close")
        .off("submit", ".LINK___modal___modal___action_submit_and_keep_the_modal_open")
        .off("submit", ".LINK___modal___modal___action_submit_and_close_the_modal");
};
var ___HTML___modal___modal___EVENTS_ON___ = function () {
    ___HTML___modal___modal___EVENTS_OFF___();
    $("#site___modal___modal")
        .on("click", ".LINK___modal___modal___action_refresh", ___HTML___modal___modal___ACTION_REFRESH___)
        .on("click", ".LINK___modal___modal___action_close", ___HTML___modal___modal___ACTION_CLOSE___)
        .on("submit", ".LINK___modal___modal___action_submit_and_keep_the_modal_open", ___HTML___modal___modal___ACTION_SUBMIT_AND_KEEP_THE_MODAL_OPEN___)
        .on("submit", ".LINK___modal___modal___action_submit_and_close_the_modal", ___HTML___modal___modal___ACTION_SUBMIT_AND_CLOSE_THE_MODAL___);
};
var ___HTML___modal___modal___SHOW_MESSAGE_ERROR___ = function (data) {
    var $site___modal___modal = $("#site___modal___modal");
    $site___modal___modal.html(data.___HTML___MODAL___MODAL___);
    $site___modal___modal.find(".modal___message").html(data.___HTML___MODAL___MODAL___MESSAGE___);
    /* */
    var int___message_state = 0;

    function ___JS___modal___message___close1___() {
        if ($site___modal___modal.find(".modal___message").find(".alert").find("button.close").length <= 1) {
            ___JS___modal___message___close___();
        }
    }

    function ___JS___modal___message___close2___() {
        if (int___message_state == 0) {
            ___JS___modal___message___close___();
        }
    }

    function ___JS___modal___message___close___() {
        $site___modal___modal.find(".modal___message").off("click", ".alert button.close");
        ___HTML___modal___modal___ACTION_CLOSE___();
        int___message_state = 1;
        if (typeof(data.___APPLICATION___SECURITY___USER___WITHOUT_PERMISSION___) != "undefined" && data.___APPLICATION___SECURITY___USER___WITHOUT_PERMISSION___ == true) {
            window.location.replace(data.___APPLICATION___SECURITY___USER___URL_REDIRECT___);
        }
    }

    $site___modal___modal.find(".modal___message")
        .off("click", ".alert button.close")
        .on("click", ".alert button.close", ___JS___modal___message___close1___);
    function ___JS___modal___message___alert___close___() {
        if (int___message_state == 0) {
            $site___modal___modal.find(".modal___message").fadeOut("slow", function () {
                ___JS___modal___message___close2___();
            });
        }
    }

    setTimeout(___JS___modal___message___alert___close___, 3000);
};
var ___HTML___modal___modal___SHOW_MESSAGE_OK___ = function (data) {
    var $site___modal___modal = $("#site___modal___modal");
    $site___modal___modal.html(data.___HTML___MODAL___MODAL___);
    $site___modal___modal.find(".modal___message").html(data.___HTML___MODAL___MODAL___MESSAGE___);
    /* */
    var int___message_state = 0;

    function ___JS___modal___message___close1___() {
        if ($site___modal___modal.find(".modal___message").find(".alert").find("button.close").length <= 1) {
            ___JS___modal___message___close___();
        }
    }

    function ___JS___modal___message___close2___() {
        if (int___message_state == 0) {
            ___JS___modal___message___close___();
        }
    }

    function ___JS___modal___message___close___() {
        $site___modal___modal.find(".modal___message").off("click", ".alert button.close");
        ___HTML___modal___modal___ACTION_CLOSE___();
        int___message_state = 1;
        if (typeof(data.___APPLICATION___SECURITY___USER___WITHOUT_PERMISSION___) != "undefined" && data.___APPLICATION___SECURITY___USER___WITHOUT_PERMISSION___ == true) {
            window.location.replace(data.___APPLICATION___SECURITY___USER___URL_REDIRECT___);
        }
    }

    $site___modal___modal.find(".modal___message")
        .off("click", ".alert button.close")
        .on("click", ".alert button.close", ___JS___modal___message___close1___);
    function ___JS___modal___message___alert___close___() {
        if (int___message_state == 0) {
            $site___modal___modal.find(".modal___message").fadeOut("slow", function () {
                ___JS___modal___message___close2___();
            });
        }
    }

    setTimeout(___JS___modal___message___alert___close___, 10000);
};
/* */
/* Binding */
$(document).ready(function () {
    /* Instructions to excecute when end the load. */
    ___HTML___header___RELOAD___();
    ___HTML___leftside___RELOAD___();
    ___HTML___content___footer___RELOAD___();
});
