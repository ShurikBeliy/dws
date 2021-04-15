import {ControlElement} from './control'

export class App {
  private control:Control = null;

  constructor(control:Control){
    this.control = control;
  }

  /* Run app */
  public run() {
    console.log('Run app.');
    this.control.setFilterCallback(this.runFilterCallback);
  }

  private runFilterCallback(filters:Array<ControlElement>) {
    console.log(filters);
  }
}
