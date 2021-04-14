export class App {
  private control:Control = null;

  constructor(control:Control){
    this.control = control;
  }

  /* Run app */
  public run() {
    console.log('Run app.');
  }
}
