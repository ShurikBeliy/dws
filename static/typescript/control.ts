import {config} from './config'

class ControlElement {

  private selector:string = null;
  private element:HTMLElement = null;

  constructor(selector?:string, element?:HTMLElement) {
    this.selector = selector!;
    this.element = element!;
    this.init(this.selector);
  }

  public init(selector?:string){
    this.selector = selector!;
    if(this.selector != null)
      this.element = document.querySelector(this.selector) as HTMLElement;
  }
}

class CheckboxElement extends ControlElement {

  public init(selector?:string){
    super.init(selector!);
    this.getValue();
  }

  public getValue(): string | number {
    if( this.element != null )
      return this.element.value;
    return "";
  }

  public setValue(value: string | number) {
    if( this.element != null )
      this.element.value = value;
  }
}

export class Control {

  private controlFilterElements: Array<ControlElement> = [];

  constructor(){
    this.init();
  }

  public init(){
    this.controlFilterElements = this.initFilter();
  }

  private initFilter():Array<ControlElement> {
    const filterSelector:string = config.selector.filter.selector;
    const checkboxSelector:string = config.selector.filter.input.checkbox.selector;
    const chekboxElements:Array<HTMLElement> = document.querySelectorAll(`${filterSelector} ${checkboxSelector}`);
    let filterElements:Array<CheckboxElement> = [];

    for( let element of chekboxElements ) {
      filterElements.push(new CheckboxElement(null, element));
    }

    return filterElements;
  }
}
