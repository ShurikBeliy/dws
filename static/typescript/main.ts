import {App} from './app'
import {Control} from './control'

((): void => {
  const control:Control = new Control();
  const app:App = new App(control);
  app.run();
})();
