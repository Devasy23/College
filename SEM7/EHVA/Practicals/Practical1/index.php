<!DOCTYPE html>
<html dir="ltr" lang="en" xml:lang="en">
    <head>
        <title>Nirma University  LMS: Log in to the site</title>
        <link rel="shortcut icon" href="https://lms.nirmauni.ac.in/theme/image.php/boost/theme/1689588549/favicon"/>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <meta name="keywords" content="moodle, Nirma University  LMS: Log in to the site"/>
        <link rel="stylesheet" type="text/css" href="https://lms.nirmauni.ac.in/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.css"/>
        <script id="firstthemesheet" type="text/css">
            /** Required in order to fix style inclusion problems in IE with YUI **/
        </script>
        <link rel="stylesheet" type="text/css" href="https://lms.nirmauni.ac.in/theme/styles.php/boost/1689588549_1660622646/all"/>
        <script>
            //<![CDATA[
            var M = {};
            M.yui = {};
            M.pageloadstarttime = new Date();
            M.cfg = {
                "wwwroot": "https:\/\/lms.nirmauni.ac.in",
                "homeurl": {},
                "sesskey": "qWCz3WUb8g",
                "sessiontimeout": "7200",
                "sessiontimeoutwarning": 1200,
                "themerev": "1689588549",
                "slasharguments": 1,
                "theme": "boost",
                "iconsystemmodule": "core\/icon_system_fontawesome",
                "jsrev": "1689588549",
                "admin": "admin",
                "svgicons": true,
                "usertimezone": "America\/Chicago",
                "courseId": 1,
                "courseContextId": 5,
                "contextid": 2,
                "contextInstanceId": 0,
                "langrev": 1689588549,
                "templaterev": "1689588549"
            };
            var yui1ConfigFn = function(me) {
                if (/-skin|reset|fonts|grids|base/.test(me.name)) {
                    me.type = 'css';
                    me.path = me.path.replace(/\.js/, '.css');
                    me.path = me.path.replace(/\/yui2-skin/, '/assets/skins/sam/yui2-skin')
                }
            };
            var yui2ConfigFn = function(me) {
                var parts = me.name.replace(/^moodle-/, '').split('-')
                  , component = parts.shift()
                  , module = parts[0]
                  , min = '-min';
                if (/-(skin|core)$/.test(me.name)) {
                    parts.pop();
                    me.type = 'css';
                    min = ''
                }
                if (module) {
                    var filename = parts.join('-');
                    me.path = component + '/' + module + '/' + filename + min + '.' + me.type
                } else {
                    me.path = component + '/' + component + '.' + me.type
                }
            };
            YUI_config = {
                "debug": false,
                "base": "https:\/\/lms.nirmauni.ac.in\/lib\/yuilib\/3.17.2\/",
                "comboBase": "https:\/\/lms.nirmauni.ac.in\/theme\/yui_combo.php?",
                "combine": true,
                "filter": null,
                "insertBefore": "firstthemesheet",
                "groups": {
                    "yui2": {
                        "base": "https:\/\/lms.nirmauni.ac.in\/lib\/yuilib\/2in3\/2.9.0\/build\/",
                        "comboBase": "https:\/\/lms.nirmauni.ac.in\/theme\/yui_combo.php?",
                        "combine": true,
                        "ext": false,
                        "root": "2in3\/2.9.0\/build\/",
                        "patterns": {
                            "yui2-": {
                                "group": "yui2",
                                "configFn": yui1ConfigFn
                            }
                        }
                    },
                    "moodle": {
                        "name": "moodle",
                        "base": "https:\/\/lms.nirmauni.ac.in\/theme\/yui_combo.php?m\/1689588549\/",
                        "combine": true,
                        "comboBase": "https:\/\/lms.nirmauni.ac.in\/theme\/yui_combo.php?",
                        "ext": false,
                        "root": "m\/1689588549\/",
                        "patterns": {
                            "moodle-": {
                                "group": "moodle",
                                "configFn": yui2ConfigFn
                            }
                        },
                        "filter": null,
                        "modules": {
                            "moodle-core-event": {
                                "requires": ["event-custom"]
                            },
                            "moodle-core-maintenancemodetimer": {
                                "requires": ["base", "node"]
                            },
                            "moodle-core-formchangechecker": {
                                "requires": ["base", "event-focus", "moodle-core-event"]
                            },
                            "moodle-core-handlebars": {
                                "condition": {
                                    "trigger": "handlebars",
                                    "when": "after"
                                }
                            },
                            "moodle-core-actionmenu": {
                                "requires": ["base", "event", "node-event-simulate"]
                            },
                            "moodle-core-languninstallconfirm": {
                                "requires": ["base", "node", "moodle-core-notification-confirm", "moodle-core-notification-alert"]
                            },
                            "moodle-core-dragdrop": {
                                "requires": ["base", "node", "io", "dom", "dd", "event-key", "event-focus", "moodle-core-notification"]
                            },
                            "moodle-core-chooserdialogue": {
                                "requires": ["base", "panel", "moodle-core-notification"]
                            },
                            "moodle-core-tooltip": {
                                "requires": ["base", "node", "io-base", "moodle-core-notification-dialogue", "json-parse", "widget-position", "widget-position-align", "event-outside", "cache-base"]
                            },
                            "moodle-core-popuphelp": {
                                "requires": ["moodle-core-tooltip"]
                            },
                            "moodle-core-blocks": {
                                "requires": ["base", "node", "io", "dom", "dd", "dd-scroll", "moodle-core-dragdrop", "moodle-core-notification"]
                            },
                            "moodle-core-lockscroll": {
                                "requires": ["plugin", "base-build"]
                            },
                            "moodle-core-notification": {
                                "requires": ["moodle-core-notification-dialogue", "moodle-core-notification-alert", "moodle-core-notification-confirm", "moodle-core-notification-exception", "moodle-core-notification-ajaxexception"]
                            },
                            "moodle-core-notification-dialogue": {
                                "requires": ["base", "node", "panel", "escape", "event-key", "dd-plugin", "moodle-core-widget-focusafterclose", "moodle-core-lockscroll"]
                            },
                            "moodle-core-notification-alert": {
                                "requires": ["moodle-core-notification-dialogue"]
                            },
                            "moodle-core-notification-confirm": {
                                "requires": ["moodle-core-notification-dialogue"]
                            },
                            "moodle-core-notification-exception": {
                                "requires": ["moodle-core-notification-dialogue"]
                            },
                            "moodle-core-notification-ajaxexception": {
                                "requires": ["moodle-core-notification-dialogue"]
                            },
                            "moodle-core_availability-form": {
                                "requires": ["base", "node", "event", "event-delegate", "panel", "moodle-core-notification-dialogue", "json"]
                            },
                            "moodle-backup-confirmcancel": {
                                "requires": ["node", "node-event-simulate", "moodle-core-notification-confirm"]
                            },
                            "moodle-backup-backupselectall": {
                                "requires": ["node", "event", "node-event-simulate", "anim"]
                            },
                            "moodle-course-dragdrop": {
                                "requires": ["base", "node", "io", "dom", "dd", "dd-scroll", "moodle-core-dragdrop", "moodle-core-notification", "moodle-course-coursebase", "moodle-course-util"]
                            },
                            "moodle-course-management": {
                                "requires": ["base", "node", "io-base", "moodle-core-notification-exception", "json-parse", "dd-constrain", "dd-proxy", "dd-drop", "dd-delegate", "node-event-delegate"]
                            },
                            "moodle-course-categoryexpander": {
                                "requires": ["node", "event-key"]
                            },
                            "moodle-course-util": {
                                "requires": ["node"],
                                "use": ["moodle-course-util-base"],
                                "submodules": {
                                    "moodle-course-util-base": {},
                                    "moodle-course-util-section": {
                                        "requires": ["node", "moodle-course-util-base"]
                                    },
                                    "moodle-course-util-cm": {
                                        "requires": ["node", "moodle-course-util-base"]
                                    }
                                }
                            },
                            "moodle-form-shortforms": {
                                "requires": ["node", "base", "selector-css3", "moodle-core-event"]
                            },
                            "moodle-form-dateselector": {
                                "requires": ["base", "node", "overlay", "calendar"]
                            },
                            "moodle-form-passwordunmask": {
                                "requires": []
                            },
                            "moodle-question-preview": {
                                "requires": ["base", "dom", "event-delegate", "event-key", "core_question_engine"]
                            },
                            "moodle-question-chooser": {
                                "requires": ["moodle-core-chooserdialogue"]
                            },
                            "moodle-question-searchform": {
                                "requires": ["base", "node"]
                            },
                            "moodle-availability_completion-form": {
                                "requires": ["base", "node", "event", "moodle-core_availability-form"]
                            },
                            "moodle-availability_date-form": {
                                "requires": ["base", "node", "event", "io", "moodle-core_availability-form"]
                            },
                            "moodle-availability_grade-form": {
                                "requires": ["base", "node", "event", "moodle-core_availability-form"]
                            },
                            "moodle-availability_group-form": {
                                "requires": ["base", "node", "event", "moodle-core_availability-form"]
                            },
                            "moodle-availability_grouping-form": {
                                "requires": ["base", "node", "event", "moodle-core_availability-form"]
                            },
                            "moodle-availability_mobileapp-form": {
                                "requires": ["base", "node", "event", "moodle-core_availability-form"]
                            },
                            "moodle-availability_profile-form": {
                                "requires": ["base", "node", "event", "moodle-core_availability-form"]
                            },
                            "moodle-mod_assign-history": {
                                "requires": ["node", "transition"]
                            },
                            "moodle-mod_attendance-groupfilter": {
                                "requires": ["base", "node"]
                            },
                            "moodle-mod_customcert-rearrange": {
                                "requires": ["dd-delegate", "dd-drag"]
                            },
                            "moodle-mod_quiz-dragdrop": {
                                "requires": ["base", "node", "io", "dom", "dd", "dd-scroll", "moodle-core-dragdrop", "moodle-core-notification", "moodle-mod_quiz-quizbase", "moodle-mod_quiz-util-base", "moodle-mod_quiz-util-page", "moodle-mod_quiz-util-slot", "moodle-course-util"]
                            },
                            "moodle-mod_quiz-modform": {
                                "requires": ["base", "node", "event"]
                            },
                            "moodle-mod_quiz-questionchooser": {
                                "requires": ["moodle-core-chooserdialogue", "moodle-mod_quiz-util", "querystring-parse"]
                            },
                            "moodle-mod_quiz-quizbase": {
                                "requires": ["base", "node"]
                            },
                            "moodle-mod_quiz-autosave": {
                                "requires": ["base", "node", "event", "event-valuechange", "node-event-delegate", "io-form"]
                            },
                            "moodle-mod_quiz-util": {
                                "requires": ["node", "moodle-core-actionmenu"],
                                "use": ["moodle-mod_quiz-util-base"],
                                "submodules": {
                                    "moodle-mod_quiz-util-base": {},
                                    "moodle-mod_quiz-util-slot": {
                                        "requires": ["node", "moodle-mod_quiz-util-base"]
                                    },
                                    "moodle-mod_quiz-util-page": {
                                        "requires": ["node", "moodle-mod_quiz-util-base"]
                                    }
                                }
                            },
                            "moodle-mod_quiz-toolboxes": {
                                "requires": ["base", "node", "event", "event-key", "io", "moodle-mod_quiz-quizbase", "moodle-mod_quiz-util-slot", "moodle-core-notification-ajaxexception"]
                            },
                            "moodle-message_airnotifier-toolboxes": {
                                "requires": ["base", "node", "io"]
                            },
                            "moodle-filter_glossary-autolinker": {
                                "requires": ["base", "node", "io-base", "json-parse", "event-delegate", "overlay", "moodle-core-event", "moodle-core-notification-alert", "moodle-core-notification-exception", "moodle-core-notification-ajaxexception"]
                            },
                            "moodle-filter_mathjaxloader-loader": {
                                "requires": ["moodle-core-event"]
                            },
                            "moodle-editor_atto-editor": {
                                "requires": ["node", "transition", "io", "overlay", "escape", "event", "event-simulate", "event-custom", "node-event-html5", "node-event-simulate", "yui-throttle", "moodle-core-notification-dialogue", "moodle-core-notification-confirm", "moodle-editor_atto-rangy", "handlebars", "timers", "querystring-stringify"]
                            },
                            "moodle-editor_atto-plugin": {
                                "requires": ["node", "base", "escape", "event", "event-outside", "handlebars", "event-custom", "timers", "moodle-editor_atto-menu"]
                            },
                            "moodle-editor_atto-menu": {
                                "requires": ["moodle-core-notification-dialogue", "node", "event", "event-custom"]
                            },
                            "moodle-editor_atto-rangy": {
                                "requires": []
                            },
                            "moodle-report_eventlist-eventfilter": {
                                "requires": ["base", "event", "node", "node-event-delegate", "datatable", "autocomplete", "autocomplete-filters"]
                            },
                            "moodle-report_loglive-fetchlogs": {
                                "requires": ["base", "event", "node", "io", "node-event-delegate"]
                            },
                            "moodle-report_overviewstats-charts": {
                                "requires": ["base", "node", "charts", "charts-legend"]
                            },
                            "moodle-gradereport_history-userselector": {
                                "requires": ["escape", "event-delegate", "event-key", "handlebars", "io-base", "json-parse", "moodle-core-notification-dialogue"]
                            },
                            "moodle-qbank_editquestion-chooser": {
                                "requires": ["moodle-core-chooserdialogue"]
                            },
                            "moodle-tool_capability-search": {
                                "requires": ["base", "node"]
                            },
                            "moodle-tool_lp-dragdrop-reorder": {
                                "requires": ["moodle-core-dragdrop"]
                            },
                            "moodle-tool_monitor-dropdown": {
                                "requires": ["base", "event", "node"]
                            },
                            "moodle-assignfeedback_editpdf-editor": {
                                "requires": ["base", "event", "node", "io", "graphics", "json", "event-move", "event-resize", "transition", "querystring-stringify-simple", "moodle-core-notification-dialog", "moodle-core-notification-alert", "moodle-core-notification-warning", "moodle-core-notification-exception", "moodle-core-notification-ajaxexception"]
                            },
                            "moodle-atto_accessibilitychecker-button": {
                                "requires": ["color-base", "moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_accessibilityhelper-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_align-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_bold-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_charmap-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_clear-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_collapse-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_emojipicker-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_emoticon-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_equation-button": {
                                "requires": ["moodle-editor_atto-plugin", "moodle-core-event", "io", "event-valuechange", "tabview", "array-extras"]
                            },
                            "moodle-atto_fullscreen-button": {
                                "requires": ["event-resize", "moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_h5p-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_html-beautify": {},
                            "moodle-atto_html-button": {
                                "requires": ["promise", "moodle-editor_atto-plugin", "moodle-atto_html-beautify", "moodle-atto_html-codemirror", "event-valuechange"]
                            },
                            "moodle-atto_html-codemirror": {
                                "requires": ["moodle-atto_html-codemirror-skin"]
                            },
                            "moodle-atto_image-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_indent-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_italic-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_justify-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_link-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_managefiles-usedfiles": {
                                "requires": ["node", "escape"]
                            },
                            "moodle-atto_managefiles-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_media-button": {
                                "requires": ["moodle-editor_atto-plugin", "moodle-form-shortforms"]
                            },
                            "moodle-atto_noautolink-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_orderedlist-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_preview-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_recordrtc-recording": {
                                "requires": ["moodle-atto_recordrtc-button"]
                            },
                            "moodle-atto_recordrtc-button": {
                                "requires": ["moodle-editor_atto-plugin", "moodle-atto_recordrtc-recording"]
                            },
                            "moodle-atto_rtl-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_sketch-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_strike-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_subscript-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_superscript-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_table-button": {
                                "requires": ["moodle-editor_atto-plugin", "moodle-editor_atto-menu", "event", "event-valuechange"]
                            },
                            "moodle-atto_title-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_underline-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_undo-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_unorderedlist-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-atto_wiris-button": {
                                "requires": ["moodle-editor_atto-plugin", "get"]
                            },
                            "moodle-atto_wordimport-button": {
                                "requires": ["moodle-editor_atto-plugin"]
                            },
                            "moodle-tinymce_mathslate-textool": {
                                "requires": ["dd-drag", "dd-proxy", "dd-drop", "event", "json"]
                            },
                            "moodle-tinymce_mathslate-snippeteditor": {
                                "requires": ["json"]
                            },
                            "moodle-tinymce_mathslate-mathjaxeditor": {
                                "requires": ["moodle-tinymce_mathslate-snippeteditor", "dd-drop"]
                            },
                            "moodle-tinymce_mathslate-dialogue": {
                                "requires": ["escape", "moodle-local_mathslate-editor", "moodle-tinymce_mathslate-editor"]
                            },
                            "moodle-tinymce_mathslate-editor": {
                                "requires": ["dd-drag", "dd-proxy", "dd-drop", "event", "tabview", "io-base", "json", "moodle-tinymce_mathslate-textool", "moodle-tinymce_mathslate-mathjaxeditor"]
                            }
                        }
                    },
                    "gallery": {
                        "name": "gallery",
                        "base": "https:\/\/lms.nirmauni.ac.in\/lib\/yuilib\/gallery\/",
                        "combine": true,
                        "comboBase": "https:\/\/lms.nirmauni.ac.in\/theme\/yui_combo.php?",
                        "ext": false,
                        "root": "gallery\/1689588549\/",
                        "patterns": {
                            "gallery-": {
                                "group": "gallery"
                            }
                        }
                    }
                },
                "modules": {
                    "core_filepicker": {
                        "name": "core_filepicker",
                        "fullpath": "https:\/\/lms.nirmauni.ac.in\/lib\/javascript.php\/1689588549\/repository\/filepicker.js",
                        "requires": ["base", "node", "node-event-simulate", "json", "async-queue", "io-base", "io-upload-iframe", "io-form", "yui2-treeview", "panel", "cookie", "datatable", "datatable-sort", "resize-plugin", "dd-plugin", "escape", "moodle-core_filepicker", "moodle-core-notification-dialogue"]
                    },
                    "core_comment": {
                        "name": "core_comment",
                        "fullpath": "https:\/\/lms.nirmauni.ac.in\/lib\/javascript.php\/1689588549\/comment\/comment.js",
                        "requires": ["base", "io-base", "node", "json", "yui2-animation", "overlay", "escape"]
                    },
                    "mathjax": {
                        "name": "mathjax",
                        "fullpath": "https:\/\/cdn.jsdelivr.net\/npm\/mathjax@2.7.9\/MathJax.js?delayStartupUntil=configured"
                    }
                }
            };
            M.yui.loader = {
                modules: {}
            };

            //]]>
        </script>
        <meta name="moodle-validation" content="9025d426b6d728911f3ee8c10b1dd0f3">
        <strong>
            <center style="color:#0090FF;">Mozilla Firefox is recommended for best experience    </center>
        </strong>
        <h3 style="color:#0090FF;">
            <strong>
                <center>Moodle - Learning Management System (LMS)    </center>
            </strong>
        </h3>
        <meta name="robots" content="noindex"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body id="page-login-index" class="format-site  path-login chrome dir-ltr lang-en yui-skin-sam yui3-skin-sam lms-nirmauni-ac-in pagelayout-login course-1 context-2 notloggedin ">
        <div class="toast-wrapper mx-auto py-0 fixed-top" role="status" aria-live="polite"></div>
        <div id="page-wrapper">
            <div>
                <a class="sr-only sr-only-focusable" href="#maincontent">Skip to main content</a>
            </div>
            <script src="https://lms.nirmauni.ac.in/lib/javascript.php/1689588549/lib/polyfills/polyfill.js"></script>
            <script src="https://lms.nirmauni.ac.in/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.js"></script>
            <script src="https://lms.nirmauni.ac.in/lib/javascript.php/1689588549/lib/javascript-static.js"></script>
            <script>
                //<![CDATA[
                document.body.className += ' jsenabled';
                //]]>
            </script>
            <div id="page" class="container-fluid pt-5 mt-0">
                <div id="page-content" class="row">
                    <div id="region-main-box" class="col-12">
                        <section id="region-main" class="col-12 h-100" aria-label="Content">
                            <div class="login-wrapper">
                                <div class="login-container">
                                    <div role="main">
                                        <span id="maincontent"></span>
                                        <div class="loginform">
                                            <div id="loginlogo" class="login-logo">
                                                <img id="logoimage" src="https://lms.nirmauni.ac.in/pluginfile.php/2/core_admin/logo/0x200/1689588549/Nirma-Uni-Logo.jpg" class="img-fluid" alt="Nirma University  LMS"/>
                                                <h1 class="login-heading sr-only">Log in to Nirma University  LMS</h1>
                                            </div>
                                            <form class="login-form" action="https://lms.nirmauni.ac.in/login/index.php" method="post" id="login">
                                                <input id="anchor" type="hidden" name="anchor" value="">
                                                <script>
                                                    document.getElementById('anchor').value = location.hash;
                                                </script>
                                                <input type="hidden" name="logintoken" value="ABO8ivJlVQdMFHk81fUk79H8y3wY6lNV">
                                                <div class="login-form-username form-group">
                                                    <label for="username" class="sr-only">Username
            </label>
                                                    <input type="text" name="username" id="username" class="form-control form-control-lg" value="20bce057@nirmauni.ac.in" placeholder="Username" autocomplete="username">
                                                </div>
                                                <div class="login-form-password form-group">
                                                    <label for="password" class="sr-only">Password</label>
                                                    <input type="password" name="password" id="password" value="" class="form-control form-control-lg" placeholder="Password" autocomplete="current-password">
                                                </div>
                                                <div class="login-form-submit form-group">
                                                    <button class="btn btn-primary btn-lg" type="submit" id="loginbtn">Log in</button>
                                                </div>
                                                <div class="login-form-forgotpassword form-group">
                                                    <a href="https://lms.nirmauni.ac.in/login/forgot_password.php">Lost password?</a>
                                                </div>
                                            </form>
                                            <div class="login-divider"></div>
                                            <div class="d-flex">
                                                <button type="button" class="btn btn-secondary" data-modal="alert" data-modal-title-str='["cookiesenabled", "core"]' data-modal-content-str='["cookiesenabled_help_html", "core"]'>Cookies notice</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>
                    </div>
                </div>
            </div>
            <footer id="page-footer" class="footer-popover bg-white">
                <div data-region="footer-container-popover">
                    <button class="btn btn-icon bg-secondary icon-no-margin btn-footer-popover" data-action="footer-popover" aria-label="Show footer">
                        <i class="icon fa fa-question fa-fw " aria-hidden="true"></i>
                    </button>
                </div>
                <div class="footer-content-popover container" data-region="footer-content-popover">
                    <div class="footer-section p-3 border-bottom">
                        <div class="logininfo">
                            <div class="logininfo">You are not logged in.</div>
                        </div>
                        <div class="tool_usertours-resettourcontainer"></div>
                        <div class="tool_dataprivacy">
                            <a href="https://lms.nirmauni.ac.in/admin/tool/dataprivacy/summary.php">Data retention summary</a>
                        </div>
                        <a class="mobilelink" href="https://download.moodle.org/mobile?version=2022112804.03&amp;lang=en&amp;iosappid=633359593&amp;androidappid=com.moodle.moodlemobile">Get the mobile app</a>
                        <strong>
                            <p style="color:#0080FF;">
                                For Support Contact <a href="mailto:lms@nirmauni.ac.in">lms@nirmauni.ac.in</a>
                            </p>
                        </strong>
                        <script>
                            //<![CDATA[
                            var require = {
                                baseUrl: 'https://lms.nirmauni.ac.in/lib/requirejs.php/1689588549/',
                                // We only support AMD modules with an explicit define() statement.
                                enforceDefine: true,
                                skipDataMain: true,
                                waitSeconds: 0,

                                paths: {
                                    jquery: 'https://lms.nirmauni.ac.in/lib/javascript.php/1689588549/lib/jquery/jquery-3.6.1.min',
                                    jqueryui: 'https://lms.nirmauni.ac.in/lib/javascript.php/1689588549/lib/jquery/ui-1.13.2/jquery-ui.min',
                                    jqueryprivate: 'https://lms.nirmauni.ac.in/lib/javascript.php/1689588549/lib/requirejs/jquery-private'
                                },

                                // Custom jquery config map.
                                map: {
                                    // '*' means all modules will get 'jqueryprivate'
                                    // for their 'jquery' dependency.
                                    '*': {
                                        jquery: 'jqueryprivate'
                                    },
                                    // Stub module for 'process'. This is a workaround for a bug in MathJax (see MDL-60458).
                                    '*': {
                                        process: 'core/first'
                                    },

                                    // 'jquery-private' wants the real jQuery module
                                    // though. If this line was not here, there would
                                    // be an unresolvable cyclic dependency.
                                    jqueryprivate: {
                                        jquery: 'jquery'
                                    }
                                }
                            };

                            //]]>
                        </script>
                        <script src="https://lms.nirmauni.ac.in/lib/javascript.php/1689588549/lib/requirejs/require.min.js"></script>
                        <script>
                            //<![CDATA[
                            M.util.js_pending("core/first");
                            require(['core/first'], function() {
                                require(['core/prefetch']);
                                require(["media_videojs/loader"], function(loader) {
                                    loader.setUp('en');
                                });
                                ;
                                require(['theme_boost/footer-popover'], function(FooterPopover) {
                                    FooterPopover.init();
                                });
                                ;
                                M.util.js_pending('theme_boost/loader');
                                require(['theme_boost/loader'], function() {
                                    M.util.js_complete('theme_boost/loader');
                                });
                                ;
                                require(['core_form/submit'], function(Submit) {
                                    Submit.init("loginbtn");
                                });
                                ;M.util.js_pending('core/notification');
                                require(['core/notification'], function(amd) {
                                    amd.init(2, []);
                                    M.util.js_complete('core/notification');
                                });
                                ;M.util.js_pending('core/log');
                                require(['core/log'], function(amd) {
                                    amd.setConfig({
                                        "level": "warn"
                                    });
                                    M.util.js_complete('core/log');
                                });
                                ;M.util.js_pending('core/page_global');
                                require(['core/page_global'], function(amd) {
                                    amd.init();
                                    M.util.js_complete('core/page_global');
                                });
                                ;M.util.js_pending('core/utility');
                                require(['core/utility'], function(amd) {
                                    M.util.js_complete('core/utility');
                                });
                                M.util.js_complete("core/first");
                            });
                            //]]>
                        </script>
                        <script>
                            //<![CDATA[
                            M.str = {
                                "moodle": {
                                    "lastmodified": "Last modified",
                                    "name": "Name",
                                    "error": "Error",
                                    "info": "Information",
                                    "yes": "Yes",
                                    "no": "No",
                                    "cancel": "Cancel",
                                    "confirm": "Confirm",
                                    "areyousure": "Are you sure?",
                                    "closebuttontitle": "Close",
                                    "unknownerror": "Unknown error",
                                    "file": "File",
                                    "url": "URL",
                                    "collapseall": "Collapse all",
                                    "expandall": "Expand all"
                                },
                                "repository": {
                                    "type": "Type",
                                    "size": "Size",
                                    "invalidjson": "Invalid JSON string",
                                    "nofilesattached": "No files attached",
                                    "filepicker": "File picker",
                                    "logout": "Logout",
                                    "nofilesavailable": "No files available",
                                    "norepositoriesavailable": "Sorry, none of your current repositories can return files in the required format.",
                                    "fileexistsdialogheader": "File exists",
                                    "fileexistsdialog_editor": "A file with that name has already been attached to the text you are editing.",
                                    "fileexistsdialog_filemanager": "A file with that name has already been attached",
                                    "renameto": "Rename to \"{$a}\"",
                                    "referencesexist": "There are {$a} links to this file",
                                    "select": "Select"
                                },
                                "admin": {
                                    "confirmdeletecomments": "You are about to delete comments, are you sure?",
                                    "confirmation": "Confirmation"
                                },
                                "debug": {
                                    "debuginfo": "Debug info",
                                    "line": "Line",
                                    "stacktrace": "Stack trace"
                                },
                                "langconfig": {
                                    "labelsep": ": "
                                }
                            };
                            //]]>
                        </script>
                        <script>
                            //<![CDATA[
                            (function() {
                                Y.use("moodle-filter_mathjaxloader-loader", function() {
                                    M.filter_mathjaxloader.configure({
                                        "mathjaxconfig": "MathJax.Hub.Config({\r\n    config: [\"Accessible.js\", \"Safe.js\"],\r\n    errorSettings: { message: [\"!\"] },\r\n    skipStartupTypeset: true,\r\n    messageStyle: \"none\",\r\n   TeX: { extensions:  [\"AMSmath.js\",\"AMSsymbols.js\",\"mhchem.js\",\"noErrors.js\",\"noUndefined.js\"] }\r\n});",
                                        "lang": "en"
                                    });
                                });
                                M.util.help_popups.setup(Y);
                                M.util.js_pending('random64bdeff13dee22');
                                Y.on('domready', function() {
                                    M.util.js_complete("init");
                                    M.util.js_complete('random64bdeff13dee22');
                                });
                            }
                            )();
                            //]]>
                        </script>
                    </div>
                    <div class="footer-section p-3">
                        <div>
                            Powered by <a href="https://moodle.com">Moodle</a>
                        </div>
                    </div>
                </div>
                <div class="footer-content-debugging footer-dark bg-dark text-light">
                    <div class="container-fluid footer-dark-inner"></div>
                </div>
            </footer>
        </div>
    </body>
</html>
