/*! FlyThat - v0.1.0 - 2014-08-03
* https://github.com/lucasferreira/flythat
* Copyright (c) 2014 Lucas Ferreira; Licensed MIT */
(function($, window, document, undefined) {
    "use strict";

    function FlyThat(element, options)
    {
        this._element = $(element);
        this._body = $(document.body);
        this._options = this._builOptions(options);

        if(!$.support.transition)
        {
            $.support.transition = (function(){
                var thisBody = document.body || document.documentElement,
                    thisStyle = thisBody.style,
                    support = thisStyle.transition !== undefined || thisStyle.WebkitTransition !== undefined || thisStyle.MozTransition !== undefined || thisStyle.MsTransition !== undefined || thisStyle.OTransition !== undefined;
                return support;
            })();
        }

        if(!$.support.transform)
        {
            $.support.transform = (function(){
                var thisBody = document.body || document.documentElement,
                    thisStyle = thisBody.style,
                    support = thisStyle.transform !== undefined || thisStyle.WebkitTransform !== undefined || thisStyle.MozTransform !== undefined || thisStyle.MsTransform !== undefined || thisStyle.OTransform !== undefined;
                return support;
            })();
        }

        /* LOAD DATA OPTIONS */
        $.each(this._options, $.proxy(function(k, v) {
            if(this._element.data(k.toLowerCase()) != null)
            {
                this._options[k] = this._element.data(k.toLowerCase());
            }
        }, this));

        this._init();
    };
    FlyThat.fn = FlyThat.prototype = {
        _init: function()
        {
            if(this._options.backdrop)
            {
                if(!this._element.parents('.flythat-backdrop').length)
                {
                    this._element.wrap("<div class='flythat-backdrop'></div>");
                }

                this._backdrop = this._element.parents('.flythat-backdrop').data('owner', this);
                this._backdrop.css({
                    "position": "absolute",
                    "top": 0, "bottom": 0,
                    "left": 0, "right": 0,
                    "zIndex": this._options.zIndex-1
                });
                this._backdrop.css("position", "fixed");

                if(this._options.backdropClass)
                {
                    this._backdrop.addClass(this._options.backdropClass);
                }
                if(this._options.backdropColor)
                {
                    this._backdrop.css("background-color", this._options.backdropColor);
                }
                if(this._options.backdropColorRGBA)
                {
                    this._backdrop.css("background-color", this._options.backdropColorRGBA);
                }

                if($.support.transform)
                {
                    this._backdrop.css({
                        "-webkit-transform-style": "preserve-3d",
                        "-moz-transform-style": "preserve-3d",
                        "-ms-transform-style": "preserve-3d",
                        "-o-transform-style": "preserve-3d",
                        "transform-style": "preserve-3d"
                    });
                }
            }
            else
            {
                this._backdrop = false;

                this._element.css({
                    "position": "absolute",
                    "zIndex": this._options.zIndex
                });
                this._element.css("position", "fixed");

                if($.support.transform)
                {
                    this._element.css({
                        "-webkit-transform-style": "preserve-3d",
                        "-moz-transform-style": "preserve-3d",
                        "-ms-transform-style": "preserve-3d",
                        "-o-transform-style": "preserve-3d",
                        "transform-style": "preserve-3d"
                    });
                }
            }

            this._handle().css({
                "display": "none",
                "visibility": "hidden",
                "opacity": 0
            });
            this._addEventsListener();

            if(this._options.autoOpen)
            {
                if(!!this._timerToShow) clearTimeout(this._timerToShow);

                var ts = typeof this._options.autoOpen == "number" ? this._options.autoOpen : 10;
                this._timerToShow = setTimeout($.proxy(this.open, this), ts);
            }

            this.show = this.open;
            this.hide = this.close;
        },
        _builOptions: function(options)
        {
            return $.extend({
                position: "center", // left, right, left-bottom, right-bottom, center, [x, y] or a function
                autoOpen: false,
                autoClose: false,
                width: false,
                height: false,
                fadeIn: 'normal', // normal, fast, slow, miliseconds or false
                fadeOut: 'normal', // normal, fast, slow, miliseconds or false
                easing: 'swing',
                closeClass: 'close',
                closeEsc: true,
                hideOnMobile: false,
                backdrop: 'close', // false, true or 'close' - to close on click
                backdropClass: false, // custom class for backgrop/overlay
                backdropColor: '#333333',
                backdropColorRGBA: 'rgba(0, 0, 0, 0.75)',
                zIndex: 8888
            }, options);
        },
        _addEventsListener: function()
        {
            if(this._options.closeClass)
            {
                this._element.off('click.flythat').on('click.flythat', '.' + this._options.closeClass, $.proxy(this._clickClose, this));
            }

            if(this._backdrop && this._options.backdrop === "close")
            {
                this._backdrop.off('click.flythat').on('click.flythat', $.proxy(this._clickBackdrop, this));
            }

            if(this._options.closeEsc)
            {
                $(document).off('keyup.flythat').on('keyup.flythat', $.proxy(this._escClose, this));
            }
        },
        _escClose: function(event)
        {
            if(this._options.closeEsc && event.keyCode == 27)
            {
                if(this._handle().is(":visible")) this.close();
            }
        },
        _clickClose: function(event)
        {
            event.preventDefault();
            this.close();
            return false;
        },
        _clickBackdrop: function(event)
        {
            if($(event.target).hasClass(this._options.backdropClass || "flythat-backdrop"))
            {
                event.preventDefault();

                this.close();
            }
        },
        _handle: function()
        {
            if(this._backdrop)
            {
                return this._backdrop;
            }

            return this._element;
        },
        rebuild: function(options)
        {
            this._options = this._builOptions((options || this._options));
            this._init();
        },
        placeThat: function(position)
        {
            this._element.css({
                "position": "absolute",
                "display": "block",
                "top": "auto", "bottom": "auto",
                "left": "auto", "right": "auto",
                "zIndex": this._options.zIndex
            });
            this._element.css("position", "fixed");

            switch(position)
            {
                case "left":
                    this._element.css({
                        "top": 0,
                        "left": 0
                    });
                    break;
                case "right":
                    this._element.css({
                        "top": 0,
                        "right": 0
                    });
                    break;
                case "left-bottom":
                    this._element.css({
                        "bottom": 0,
                        "left": 0
                    });
                    break;
                case "right-bottom":
                    this._element.css({
                        "bottom": 0,
                        "right": 0
                    });
                    break;
                case "center":
                    this._element.css({
                        "top": "50%",
                        "left": "50%"
                    });

                    if($.support.transform)
                    {
                        this._element.css({
                            "-webkit-transform": "translateX(-50%) translateY(-50%)",
                            "-moz-transform": "translateX(-50%) translateY(-50%)",
                            "-ms-transform": "translateX(-50%) translateY(-50%)",
                            "-o-transform": "translateX(-50%) translateY(-50%)",
                            "transform": "translateX(-50%) translateY(-50%)",
                            "-webkit-transform-style": "preserve-3d",
                            "-moz-transform-style": "preserve-3d",
                            "-ms-transform-style": "preserve-3d",
                            "-o-transform-style": "preserve-3d",
                            "transform-style": "preserve-3d"
                        });
                    }
                    else
                    {
                        var __hide = false;
                        if(!this._handle().is(":visible"))
                        {
                            this._handle().show();
                            __hide = true;
                        }

                        var w = this._options.width || this._element.outerWidth(true) || this._element.width(),
                            h = this._options.height || this._element.outerHeight(true) || this._element.height();

                        if(!w || w < 1) w = this._element.find('img').width() || $(document).width();
                        if(!h || h < 1) h = this._element.find('img').height() || $(document).height();

                        this._options.width = w;
                        this._options.height = h;

                        if(__hide) this._handle().hide();

                        this._element.css({
                            "margin-left": (w/2) * -1,
                            "margin-top": (h/2) * -1
                        });
                    }
                    break;
                default:

                    if(typeof position == "string")
                    {
                        if($.isFunction(window[position]))
                        {
                            window[position](this._element, this);
                        }
                        else if($.isFunction(this[position]))
                        {
                            this[position](this._element, this);
                        }
                        else
                        {
                            var _css = {};
                            position = position.split(",");

                            if(position[0]) _css['left'] = position[0].indexOf("%") > -1 ? $.trim(position[0]) : parseFloat(position[0]);
                            if(position.length > 1 && position[1]) _css['top'] = position[1].indexOf("%") > -1 ? $.trim(position[1]) : parseFloat(position[1]);

                            this._element.css(_css);
                        }
                    }
                    else if(position instanceof Array)
                    {
                        var _css = {};
                        if(position[0]) _css['left'] = (typeof position[0] == "string" && position[0].indexOf("%") > -1) ? $.trim(position[0]) : parseFloat(position[0]);
                        if(position.length > 1 && position[1]) _css['top'] = (typeof position[1] == "string" && position[1].indexOf("%") > -1) ? $.trim(position[1]) : parseFloat(position[1]);

                        this._element.css(_css);
                    }
                    else if($.isFunction(position))
                    {
                        position(this._element, this);
                    }

                    break;
            }
        },
        open: function(customPosition)
        {
            if(this._options.hideOnMobile && this.detectMobile())
            {
                return false;
            }

            if(this._options.position)
            {
                this.placeThat(customPosition || this._options.position);
            }

            function _autoClose()
            {
                if(this._options.autoClose)
                {
                    if(!!this._timerToClose) clearTimeout(this._timerToClose);

                    var tc = typeof this._options.autoClose == "number" ? this._options.autoClose : 1000;
                    this._timerToClose = setTimeout($.proxy(this.close, this), tc);
                }

                $.proxy(_finish, this)();
            }

            function _finish()
            {
                this._element.trigger('open.flythat', [this._element, this]);
                this._element.trigger('show.flythat', [this._element, this]);
            }

            if(this._options.fadeIn)
            {
                var fs = typeof this._options.fadeIn == "boolean" ? "normal" : this._options.fadeIn;

                this._handle().stop().css({
                    "display": "block",
                    "visibility": "inherit"
                }).animate({
                    "opacity": 1
                }, fs, this._options.easing, $.proxy(_autoClose, this));
            }
            else
            {
                this._handle().css({
                    "display": "block",
                    "visibility": "inherit",
                    "opacity": 1
                });
                $.proxy(_autoClose, this)();
            }
        },
        close: function()
        {
            if(this._options.hideOnMobile && this.detectMobile())
            {
                return false;
            }

            function _finish()
            {
                this._element.trigger('close.flythat', [this._element, this]);
                this._element.trigger('hide.flythat', [this._element, this]);
            }

            if(this._options.fadeOut)
            {
                var fs = typeof this._options.fadeOut == "boolean" ? "normal" : this._options.fadeOut;

                this._handle().stop().css({
                    "display": "block",
                    "visibility": "inherit"
                }).animate({
                    "opacity": 0
                }, fs, this._options.easing, $.proxy(function() {
                    this._handle().css({
                        "display": "none",
                        "visibility": "hidden"
                    });
                    $.proxy(_finish, this)();
                }, this));
            }
            else
            {
                this._handle().css({
                    "display": "none",
                    "visibility": "hidden",
                    "opacity": 0
                });
                $.proxy(_finish, this)();
            }
        },
        toggle: function()
        {
            if(this._handle().is(":visible"))
            {
                return this.close();
            }
            else
            {
                return this.open();
            }
        },
        detectMobile: function()
        {
            if( navigator.userAgent.match(/Android/i)
                || navigator.userAgent.match(/webOS/i)
                || navigator.userAgent.match(/iPhone/i)
                || navigator.userAgent.match(/iPod/i)
                || navigator.userAgent.match(/BlackBerry/i)
                || navigator.userAgent.match(/Windows Phone/i)
            ) {
                return true;
            }

            return false;
        }
    };

    $.fn.flythat = function(options)
    {
        var args = Array.prototype.slice.call(arguments, 1),
            pluginName = 'FlyThat',
            returnValue = this;

        if (typeof options === 'string') {
            this.each(function() {
                var instance = $(this).data(pluginName);

                if (!instance) {
                    return $.error(
                        'Cannot call methods on ' + pluginName + ' prior to initialization; ' +
                        'attempted to call method "' + options + '"'
                    );
                }

                if (!$.isFunction(instance[options]) || options.charAt(0) === '_') {
                    return $.error(
                        'No such method "' + options + '" for ' + pluginName + ' instance'
                    );
                }

                var methodValue = instance[options].apply(instance, args);

                if (methodValue !== instance && typeof methodValue !== 'undefined') {
                    returnValue = methodValue;
                    return false;
                }
            });
        } else {
            this.each(function() {
                var instance = $(this).data(pluginName);

                if (instance instanceof FlyThat) {
                    instance.rebuild(options);
                } else {
                    $(this).data(pluginName, new FlyThat(this, options));
                }
            });
        }

        return returnValue;
    };

    $(document).on('click.flythat', '[data-flythat]', function(event) {
        event.preventDefault();

        var flytarget = $(this).data("flythat");
        if(flytarget != "auto" && $(flytarget).length)
        {
            var flyinstance = $(flytarget).data('FlyThat');
            if (flyinstance == null || !(flyinstance instanceof FlyThat))
            {
                $(flytarget).flythat();
            }

            $(flytarget).flythat("open");
        }

        return false;
    });

    $(window).load(function() {
        $(".flythat").each(function() {
            var flyinstance = $(this).data('FlyThat');
            if (flyinstance == null || !(flyinstance instanceof FlyThat))
            {
                $(this).flythat();
            }
        });
    });

})(jQuery, window, document);
