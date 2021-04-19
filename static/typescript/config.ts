export const config = {
  selector: { // our selectors for different elements
    selector:'html',
    filter: { // our selectors for filters
      selector:'.filter',
      input:{ // selectors for input wrapers element
        selector:'.filter__input',
        checkbox:{ // selector for checkbox
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
}
