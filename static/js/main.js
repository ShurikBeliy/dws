(function () {
  'use strict';

  var App = /** @class */ (function () {
      function App(control) {
          this.control = null;
          this.control = control;
      }
      /* Run app */
      App.prototype.run = function () {
          console.log('Run app.');
      };
      return App;
  }());

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
          }
      },
  };

  var ControlElement = /** @class */ (function () {
      function ControlElement(selector, element) {
          this.selector = null;
          this.element = null;
          this.selector = selector;
          this.element = element;
          this.init(this.selector);
      }
      ControlElement.prototype.init = function (selector) {
          this.selector = selector;
          if (this.selector != null)
              this.element = document.querySelector(this.selector);
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
      return CheckboxElement;
  }(ControlElement));
  var Control = /** @class */ (function () {
      function Control() {
          this.controlFilterElements = [];
          this.init();
      }
      Control.prototype.init = function () {
          this.controlFilterElements = this.initFilter();
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
      return Control;
  }());

  (function () {
      var control = new Control();
      var app = new App(control);
      app.run();
  })();

}());
//# sourceMappingURL=main.js.map
