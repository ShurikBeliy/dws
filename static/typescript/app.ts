import {ControlElement} from './control'
import {config} from './config'
import {get, getCurrentUrl} from './utils'

type catalogResponse = {
  id: number,
  html: string
}

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

  private async runFilterCallback(filters:Array<ControlElement>) {
    let query = '';
    let divider='';
    // collect filters for request
    for( const filter of filters ) {
      if( filter.isChecked() )
        query = `${query}${divider}${config.request.catalog.filter_name}[]=${filter.getValue()}`;
      if( divider == '' )
        divider = '&'
    }
    query = `${getCurrentUrl()}${config.request.json_path}?${query}`;
    try {
      let response = await get<catalogResponse>(query);
      changeCatalog(response);
    } catch(e) {
      console.error(e);
    }
  }

  private changeCatalog(catalog: catalogResponse) {
    const catalogElement:HTMLElement = document.querySelector(`${config.selector.catalog.selector} ${config.selector.catalog.item.selector}`);
    if(catalogElement != null)
      catalogElement.innerHTML = catalog.html;
  }
}
