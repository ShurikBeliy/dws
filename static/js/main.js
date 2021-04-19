(function () {
    'use strict';

    /*! *****************************************************************************
    Copyright (c) Microsoft Corporation.

    Permission to use, copy, modify, and/or distribute this software for any
    purpose with or without fee is hereby granted.

    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
    REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
    AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
    INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
    LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
    OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
    PERFORMANCE OF THIS SOFTWARE.
    ***************************************************************************** */
    /* global Reflect, Promise */

    var extendStatics = function(d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };

    function __extends(d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    }

    function __awaiter(thisArg, _arguments, P, generator) {
        function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
        return new (P || (P = Promise))(function (resolve, reject) {
            function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
            function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
            function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
            step((generator = generator.apply(thisArg, _arguments || [])).next());
        });
    }

    function __generator(thisArg, body) {
        var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
        return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
        function verb(n) { return function (v) { return step([n, v]); }; }
        function step(op) {
            if (f) throw new TypeError("Generator is already executing.");
            while (_) try {
                if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
                if (y = 0, t) op = [op[0] & 2, t.value];
                switch (op[0]) {
                    case 0: case 1: t = op; break;
                    case 4: _.label++; return { value: op[1], done: false };
                    case 5: _.label++; y = op[1]; op = [0]; continue;
                    case 7: op = _.ops.pop(); _.trys.pop(); continue;
                    default:
                        if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                        if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                        if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                        if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                        if (t[2]) _.ops.pop();
                        _.trys.pop(); continue;
                }
                op = body.call(thisArg, _);
            } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
            if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
        }
    }

    var config = {
        selector: {
            selector: 'html',
            filter: {
                selector: '.filter',
                input: {
                    selector: '.filter__input',
                    checkbox: {
                        selector: '.checkbox',
                    }
                }
            },
            catalog: {
                selector: '.catalog',
                item: {
                    selector: '.catalog__item',
                }
            }
        },
        request: {
            json_path: 'json/',
            catalog: {
                filter_name: 'filter',
            }
        }
    };

    function http(request) {
        return __awaiter(this, void 0, Promise, function () {
            var response, _a;
            return __generator(this, function (_b) {
                switch (_b.label) {
                    case 0: return [4 /*yield*/, fetch(request)];
                    case 1:
                        response = _b.sent();
                        _b.label = 2;
                    case 2:
                        _b.trys.push([2, 4, , 5]);
                        _a = response;
                        return [4 /*yield*/, response.json()];
                    case 3:
                        _a.parsedBody = _b.sent();
                        return [3 /*break*/, 5];
                    case 4:
                        _b.sent();
                        return [3 /*break*/, 5];
                    case 5:
                        if (!response.ok) {
                            throw new Error(response.statusText);
                        }
                        return [2 /*return*/, response];
                }
            });
        });
    }
    function get(path, args) {
        if (args === void 0) { args = { method: "get" }; }
        return __awaiter(this, void 0, Promise, function () {
            return __generator(this, function (_a) {
                switch (_a.label) {
                    case 0: return [4 /*yield*/, http(new Request(path, args))];
                    case 1: return [2 /*return*/, _a.sent()];
                }
            });
        });
    }
    function getCurrentUrl() {
        return window.location.pathname;
    }

    var App = /** @class */ (function () {
        function App(control) {
            this.control = null;
            this.control = control;
        }
        /* Run app */
        App.prototype.run = function () {
            console.log('Run app.');
            this.control.setFilterCallback(this.runFilterCallback);
        };
        App.prototype.runFilterCallback = function (filters) {
            return __awaiter(this, void 0, void 0, function () {
                var query, divider, _i, filters_1, filter, response, e_1;
                return __generator(this, function (_a) {
                    switch (_a.label) {
                        case 0:
                            query = '';
                            divider = '';
                            // collect filters for request
                            for (_i = 0, filters_1 = filters; _i < filters_1.length; _i++) {
                                filter = filters_1[_i];
                                if (filter.isChecked())
                                    query = "" + query + divider + config.request.catalog.filter_name + "[]=" + filter.getValue();
                                if (divider == '')
                                    divider = '&';
                            }
                            query = "" + getCurrentUrl() + config.request.json_path + "?" + query;
                            _a.label = 1;
                        case 1:
                            _a.trys.push([1, 3, , 4]);
                            return [4 /*yield*/, get(query)];
                        case 2:
                            response = _a.sent();
                            changeCatalog(response);
                            return [3 /*break*/, 4];
                        case 3:
                            e_1 = _a.sent();
                            console.error(e_1);
                            return [3 /*break*/, 4];
                        case 4: return [2 /*return*/];
                    }
                });
            });
        };
        App.prototype.changeCatalog = function (catalog) {
            var catalogElement = document.querySelector(config.selector.catalog.selector + " " + config.selector.catalog.item.selector);
            if (catalogElement != null)
                catalogElement.innerHTML = catalog.html;
        };
        return App;
    }());

    var ControlElement = /** @class */ (function () {
        function ControlElement(selector, element) {
            this.selector = null;
            this.element = null;
            this.filterCallbackHandler = null;
            this.selector = selector;
            this.element = element;
            this.init(this.selector);
        }
        ControlElement.prototype.init = function (selector) {
            this.selector = selector;
            if (this.selector != null)
                this.element = document.querySelector(this.selector);
        };
        ControlElement.prototype.getElement = function () {
            return this.element;
        };
        return ControlElement;
    }());
    var CheckboxElement = /** @class */ (function (_super) {
        __extends(CheckboxElement, _super);
        function CheckboxElement() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        CheckboxElement.prototype.init = function (selector) {
            _super.prototype.init.call(this, selector);
            this.getValue();
        };
        CheckboxElement.prototype.getValue = function () {
            if (this.element != null)
                return this.element.value;
            return "";
        };
        CheckboxElement.prototype.setValue = function (value) {
            if (this.element != null)
                this.element.value = value;
        };
        CheckboxElement.prototype.isChecked = function () {
            if (this.element != null)
                return this.element.checked;
            return null;
        };
        return CheckboxElement;
    }(ControlElement));
    var Control = /** @class */ (function () {
        function Control() {
            this.controlFilterElements = [];
            this.init();
        }
        Control.prototype.init = function () {
            this.controlFilterElements = this.initFilter();
            this.listenFilter();
        };
        Control.prototype.initFilter = function () {
            var filterSelector = config.selector.filter.selector;
            var checkboxSelector = config.selector.filter.input.checkbox.selector;
            var chekboxElements = document.querySelectorAll(filterSelector + " " + checkboxSelector);
            var filterElements = [];
            for (var _i = 0, chekboxElements_1 = chekboxElements; _i < chekboxElements_1.length; _i++) {
                var element = chekboxElements_1[_i];
                filterElements.push(new CheckboxElement(null, element));
            }
            return filterElements;
        };
        Control.prototype.listenFilter = function () {
            var _this = this;
            for (var _i = 0, _a = this.controlFilterElements; _i < _a.length; _i++) {
                var filter = _a[_i];
                filter.getElement().addEventListener("change", function () { return _this.runFilterCallback(); });
            }
        };
        Control.prototype.runFilterCallback = function () {
            if (this.filterCallbackHandler != null)
                this.filterCallbackHandler(this.controlFilterElements);
        };
        Control.prototype.setFilterCallback = function (callback) {
            this.filterCallbackHandler = callback;
        };
        return Control;
    }());

    (function () {
        var control = new Control();
        var app = new App(control);
        app.run();
    })();

}());
//# sourceMappingURL=main.js.map
