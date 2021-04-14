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

  var Control = /** @class */ (function () {
      function Control() {
          console.log('Control');
      }
      return Control;
  }());

  (function () {
      var control = new Control();
      var app = new App(control);
      app.run();
  })();

}());
//# sourceMappingURL=main.js.map
